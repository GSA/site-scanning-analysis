import logger from 'services/logger/logger';
import { SnapshotLoader } from '../SnapshotLoader';
import { GithubIssueService } from '../GithubIssueService';

export class NoTrueIn404Test {
  name = 'NoTrueIn404Test';
  private snapshotPath: string;
  private issueCreator: GithubIssueService;

  constructor(snapshotPath: string) {
    this.snapshotPath = snapshotPath;
    this.issueCreator = new GithubIssueService();
  }

  async runTest(): Promise<boolean> {
    const snapshotLoader = new SnapshotLoader(this.snapshotPath);
    const snapshotDf = await snapshotLoader.load();

    const columnName = '404_test';

    if (!snapshotDf.listColumns().includes(columnName)) {
      logger.error(`Column "${columnName}" not found in snapshot.`);
      await this.issueCreator.createIssue(
        `Missing Column: ${columnName}`,
        `The column \`${columnName}\` is missing from the snapshot. This test expects this column to be present and contain at least one TRUE value.`
      );
      return false;
    }

    const values = snapshotDf.select(columnName).toArray().map(row => row[0]);

    const hasTrue = values.some(value => {
      if (typeof value === 'string') {
        return value.trim().toLowerCase() === 'true';
      }
      return value === true;
    });

    if (hasTrue) {
      logger.info(`At least one "TRUE" found in column "${columnName}". Test passed.`);
      return true;
    }

    const title = `❗ No "TRUE" values found in "${columnName}"`;
    const body = `The column \`${columnName}\` is either empty or contains no "TRUE" values.\n\nThis indicates that no 404 errors were detected, which may be unexpected. Please investigate.`;

    await this.issueCreator.createIssue(title, body);
    logger.error(`No "TRUE" values found in column "${columnName}".`);
    return false;
  }
}