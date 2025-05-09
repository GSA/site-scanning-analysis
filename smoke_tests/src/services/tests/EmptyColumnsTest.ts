import logger from 'services/logger/logger';
import { SnapshotLoader } from '../SnapshotLoader';
import { GithubIssueService } from '../GithubIssueService';

export class EmptyColumnsTest {
  name = 'EmptyColumnsTest';
  private snapshotPath: string;
  private issueCreator: GithubIssueService;
  private excludedColumns: Set<string>;

  constructor(snapshotPath: string, excludedColumns: string[] = []) {
    this.snapshotPath = snapshotPath;
    this.issueCreator = new GithubIssueService();
    this.excludedColumns = new Set(excludedColumns);
  }

  async runTest(): Promise<boolean> {
    const snapshotLoader = new SnapshotLoader(this.snapshotPath);
    const snapshotDf = await snapshotLoader.load();
    const columns = snapshotDf.listColumns();

    const emptyColumns: string[] = [];

    for (const col of columns) {
      if (this.excludedColumns.has(col)) {
        logger.info(`Skipping excluded column "${col}".`);
        continue;
      }
      
      const values = snapshotDf.select(col).toArray().map(row => row[0]);
      const allNullOrEmpty = values.every(value => value === null || value === undefined || value === '');
      if (allNullOrEmpty) {
        emptyColumns.push(col);
        logger.warn(`Column "${col}" is completely empty or null.`);
      }
    }

    if (emptyColumns.length > 0) {
      const title = `Empty or Null Columns Detected`;
      const body = `❗ The following columns are completely empty or contain only null/empty values:\n\n- ${emptyColumns.join('\n- ')}\n\nPlease investigate the source of this issue.`;

      await this.issueCreator.createIssue(title, body);
      logger.error(`Empty or null columns found: ${emptyColumns.join(', ')}`);
      return false;
    }

    logger.info('Empty columns check passed.');
    return true;
  }
}