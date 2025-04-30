import logger from 'services/logger/logger';
import { GithubIssueService } from '../GithubIssueService';
import { Test } from 'types/config';

export class ApiAvailabilityTest implements Test {
  name = 'ApiAvailabilityTest';
  private apiUrl: string;
  private issueCreator: GithubIssueService;

  constructor(apiUrl: string) {
    this.apiUrl = apiUrl;
    this.issueCreator = new GithubIssueService();
  }

  async runTest(): Promise<boolean> {
    try {
      const response = await fetch(this.apiUrl);

      if (!response.ok) {
        const title = `Scan API returned status ${response.status}`;
        const body = `❗ The scan results API endpoint returned a non-success status:\n\n- **URL:** ${this.apiUrl}\n- **Status:** ${response.status} ${response.statusText}\n\nPlease investigate the API availability.`;

        await this.issueCreator.createIssue(title, body);
        logger.error(`API check failed: ${response.status} ${response.statusText}`);
        return false;
      }

      logger.info('API availability check passed.');
      return true;

    } catch (error: any) {
      const title = `Scan API request failed`;
      const body = `❗ Failed to connect to the scan results API endpoint:\n\n- **URL:** ${this.apiUrl}\n- **Error:** ${error.message}\n\nPlease investigate the connectivity issue.`;

      await this.issueCreator.createIssue(title, body);
      logger.error('API check failed with exception:', error);
      return false;
    }
  }
}