import logger from 'services/logger/logger';
import fetch from 'node-fetch';
import { GithubIssueResponse } from '../types/config';

export class GithubIssueService {
  private token: string;

  constructor() {
    if (!process.env.ISSUE_TOKEN) {
      logger.error('ISSUE_TOKEN environment variable is not set');
      throw new Error('ISSUE_TOKEN environment variable is not set');
    }
    this.token = process.env.ISSUE_TOKEN;
  }

  async createIssue(title: string, body: string): Promise<void> {
    const url = `https://api.github.com/repos/GSA/site-scanning/issues`;

    const res = await fetch(url, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.token}`,
        'Accept': 'application/vnd.github+json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ title, body })
    });

    if (!res.ok) {
      const errorText = await res.text();
      // Log status only. The raw response body may contain auth details
      logger.error(`Failed to create GitHub issue: HTTP ${res.status}`);
      throw new Error(`Failed to create GitHub issue: HTTP ${res.status} - ${errorText}`);
    }

    const json = await res.json() as GithubIssueResponse;
    logger.info(`Issue created: ${json.html_url}`);
  }
}