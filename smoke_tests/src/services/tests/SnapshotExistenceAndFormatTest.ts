import logger from 'services/logger/logger';
import { DataFrame } from 'dataframe-js';
import { GithubIssueService } from '../GithubIssueService';
import { Test } from 'types/config';

export class SnapshotExistenceAndFormatTest implements Test {
  name = 'SnapshotExistenceAndFormatTest';
  private urls: string[];
  private issueCreator: GithubIssueService;

  constructor(urls: string[]) {
    this.urls = urls;
    this.issueCreator = new GithubIssueService();
  }

  async runTest(): Promise<boolean> {
    const failures: string[] = [];

    for (const url of this.urls) {
      try {
        logger.info(`Checking snapshot: ${url}`);
        const df = await DataFrame.fromCSV(url);

        if (df.count() === 0 || df.listColumns().length === 0) {
          logger.warn(`Snapshot at ${url} is accessible but appears to be empty or improperly structured.`);
          failures.push(`- Snapshot at ${url} is empty or has no columns.`);
        } else {
          logger.info(`Snapshot at ${url} is valid with ${df.count()} rows and ${df.listColumns().length} columns.`);
        }

      } catch (error: any) {
        logger.error(`Failed to load snapshot at ${url}:`, error);
        failures.push(`- Failed to load or parse CSV at ${url}: ${error.message}`);
      }
    }

    if (failures.length > 0) {
      const title = `Snapshot Existence or Format Error`;
      const body = `❗ One or more snapshot files are missing or not properly formatted as CSV:\n\n${failures.join('\n')}\n\nPlease investigate the source or data pipeline.`;

      //await this.issueCreator.createIssue(title, body);
      return false;
    }

    logger.info('All snapshot files exist and are properly formatted.');
    return true;
  }
}