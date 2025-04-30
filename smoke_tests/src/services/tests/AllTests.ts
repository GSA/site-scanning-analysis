import { Test }  from 'types/config';
import { RowCountTest } from './RowCountTest';
import { EmptyColumnsTest } from './EmptyColumnsTest';
import { HttpsEnforcementTest } from './HttpsEnforcementTest';
import { ApiAvailabilityTest } from './ApiAvailibilityTest';
import { SnapshotExistenceAndFormatTest } from './SnapshotExistenceAndFormatTest';

const snapshotUrl = 'https://api.gsa.gov/technology/site-scanning/data/site-scanning-latest.csv';
const previousSnapshot = 'https://api.gsa.gov/technology/site-scanning/data/site-scanning-previous.csv';
const indexUrl = 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/site-scanning-target-url-list.csv';
const apiTestUrl = 'https://api.gsa.gov/technology/site-scanning/v1/websites/cms.gov?api_key=DEMO_KEY';

export const getAllTests = (): Test[] => [
  new RowCountTest(indexUrl, snapshotUrl),
  new EmptyColumnsTest(snapshotUrl),
  new HttpsEnforcementTest(snapshotUrl),
  new ApiAvailabilityTest(apiTestUrl),
  new SnapshotExistenceAndFormatTest([snapshotUrl, previousSnapshot]),
];