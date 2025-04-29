export type GithubIssueResponse = {
  html_url: string;
  number: number;
  title: string;
}

export type ITest = {
  name: string;
  runTest(): Promise<boolean>;
}