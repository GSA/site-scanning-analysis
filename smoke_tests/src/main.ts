import logger from 'services/logger/logger';
import { getAllTests } from 'services/tests/AllTests';

async function main() {
  logger.info('Starting smoke tests...');

  const tests = getAllTests();

  for (const test of tests) {
    logger.info(`Running test: ${test.name}`);
    const result = await test.runTest();
    if (!result) {
      logger.error(`${test.name} failed.`);
    } else {
      logger.info(`${test.name} passed.`);
    }
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

