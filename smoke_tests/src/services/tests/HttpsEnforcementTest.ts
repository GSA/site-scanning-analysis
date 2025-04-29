import logger from 'services/logger/logger';
import { SnapshotLoader } from '../SnapshotLoader';
import { GithubIssueService } from '../GithubIssueService';
import { Test } from 'types/config';

export class HttpsEnforcementTest implements Test {
  name = 'HttpsEnforcementTest';
  private snapshotPath: string;
  private issueCreator: GithubIssueService;

  constructor(snapshotPath: string) {
    this.snapshotPath = snapshotPath;
    this.issueCreator = new GithubIssueService();
  }

  async runTest(): Promise<boolean> {
    const snapshotLoader = new SnapshotLoader(this.snapshotPath);
    const snapshotDf = await snapshotLoader.load();

    if (!snapshotDf.listColumns().includes('initial_url')) {
      logger.warn(`Column "initial_url" not found in snapshot.`);
      return true; // Graceful pass if column is missing
    }

    const urls = snapshotDf.select('initial_url').toArray().map(row => row[0]);
    const nonHttpsUrls = urls.filter(url => typeof url === 'string' && url.startsWith('http://'));

    if (nonHttpsUrls.length > 0) {
      const title = `Non-HTTPS URLs Found in "initial_url"`;
      const body = `❗ Detected ${nonHttpsUrls.length} entries in the \`initial_url\` column that start with \`http://\` instead of \`https://\`.\n\nExample URLs:\n\n${nonHttpsUrls.slice(0, 10).map(u => `- ${u}`).join('\n')}\n\nPlease ensure all URLs use HTTPS.`;

      await this.issueCreator.createIssue(title, body);
      logger.error(`Found ${nonHttpsUrls.length} non-HTTPS URLs in "initial_url" column.`);
      return false;
    }

    logger.info('HTTPS enforcement check passed.');
    return true;
  }
}