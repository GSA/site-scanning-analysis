import logger from 'services/logger/logger';
import { Test } from 'types/config';
import { DataFrame } from 'dataframe-js';
import { SnapshotLoader } from '../SnapshotLoader';
import { GithubIssueService } from '../GithubIssueService';

export class RowCountTest implements Test {
  name = 'RowCountTest';
  private indexPath: string;
  private snapshotPath: string;
  private issueCreator: GithubIssueService;

  constructor(indexPath: string, snapshotPath: string) {
    this.indexPath = indexPath;
    this.snapshotPath = snapshotPath;
    this.issueCreator = new GithubIssueService();
  }


  async runTest(): Promise<boolean> {
    const indexDf = await DataFrame.fromCSV(this.indexPath);
    const snapshotLoader = new SnapshotLoader(this.snapshotPath);
    const snapshotDf = await snapshotLoader.load();

    const indexCount = indexDf.count();
    logger.debug(`Index row count: ${indexCount}`);
    const snapshotCount = snapshotDf.count();
    logger.debug(`Snapshot row count: ${snapshotCount}`);

    const threshold = indexCount * 0.95;

    logger.info(`Expected ≥ ${Math.floor(threshold)} rows, found ${snapshotCount}`);

    if (snapshotCount < threshold) {
      const title = `Row count below 95% threshold`;
      const body = `❗ Row count anomaly detected:\n\n- **Expected rows:** ${indexCount}\n- **Snapshot rows:** ${snapshotCount}\n- **Threshold (95%):** ${Math.floor(threshold)}\n\nPlease investigate.`;

      await this.issueCreator.createIssue(title, body);
      logger.error(`Row count anomaly detected: ${snapshotCount} < ${Math.floor(threshold)}`);
      return false;
    } else {
      logger.info('Row count check passed.');
      return true;
    }
  }
}