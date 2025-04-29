import { Test }  from 'types/config';
import { RowCountTest } from './RowCountTest';
import { EmptyColumnsTest } from './EmptyColumnsTest';
import { HttpsEnforcementTest } from './HttpsEnforcementTest';

const snapshotUrl = 'https://api.gsa.gov/technology/site-scanning/data/site-scanning-latest.csv';
const indexUrl = 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/site-scanning-target-url-list.csv';

export const getAllTests = (): Test[] => [
  new RowCountTest(indexUrl, snapshotUrl),
  new EmptyColumnsTest(snapshotUrl),
  new HttpsEnforcementTest(snapshotUrl),
];