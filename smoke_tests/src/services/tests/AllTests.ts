import { ITest }  from 'types/config';
import { RowCountTest } from './RowCountTest';
import { EmptyColumnsTest } from './EmptyColumnsTest';

const snapshotUrl = 'https://api.gsa.gov/technology/site-scanning/data/site-scanning-latest.csv';
const indexUrl = 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/site-scanning-target-url-list.csv';

export const getAllTests = (): ITest[] => [
  new RowCountTest(indexUrl, snapshotUrl),
  new EmptyColumnsTest(snapshotUrl),
];