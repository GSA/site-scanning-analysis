import logger from 'services/logger/logger';
import { SnapshotLoader } from 'services/SnapshotLoader';
import { RowCountTest } from 'services/tests/RowCountTest';

async function main() {
  logger.info('Starting smoke tests...');

  logger.info('Loading snapshot data...');
  const rowCountTest = new RowCountTest(
    'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/site-scanning-target-url-list.csv',
    'https://api.gsa.gov/technology/site-scanning/data/site-scanning-latest.csv'
  );
  const rowCountResult = await rowCountTest.runTest();
  if (!rowCountResult) {
    logger.error('Row count test failed.');
  }

};

main()
  .then(() => {
    logger.info('Smoke tests completed successfully.');
    process.exit(0);
  })
  .catch((error) => {
    logger.error('Smoke tests failed:', error);
    process.exit(1);
  });

