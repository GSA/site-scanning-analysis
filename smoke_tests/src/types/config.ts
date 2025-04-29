export type GithubIssueResponse = {
  html_url: string;
  number: number;
  title: string;
}

export type Test = {
  name: string;
  runTest(): Promise<boolean>;
}