# Site Scanning Smoke Tests

This TypeScript-based application runs automated smoke tests against the **output of the Site Scanning scans** to validate data quality, schema consistency, and detect anomalies early. It ensures that published snapshot data is complete, well-structured, and meets expected standards.

---

## Overview

These smoke tests focus on validating the **latest published snapshot data** retrieved from the [Site Scanning Snapshot](https://digital.gov/guides/site-scanning/data#content-start). Each test is encapsulated in a class and designed to run independently. If a test fails, the application automatically creates a GitHub issue to notify maintainers.

---

## Current Tests

- **RowCountTest**  
  Ensures the latest snapshot contains at least 95% of the rows found in the index reference file.

- **EmptyColumnsTest**  
  Detects any columns that are completely empty or contain only null or empty values.

- **ApiAvailabilityTest**
  Ensures the API is available and correctly responding to requests.

- **HttpsEnforcementTest**
  Verifies that all URLs in the snapshot use HTTPS, enforcing secure connections.

- **SnapshotExistenceAndFormatTest**
  Checks for the existence of required snapshots and ensures they follow the expected format.

---

## Prerequisites

- [Bun](https://bun.sh/) (JavaScript runtime)
- Node.js 18+ (for compatibility with some dependencies)
- GitHub token for issue creation

You must define the following environment variable:

```bash
GITHUB_TOKEN=your_github_token_here
```

## Getting Started

1. **Install Dependencies**
```bash
bun install
```
2. **Run all tests**
```bash 
bun run src/main.ts
```

## Add New Tests

**Create the Test File**
- Add your test implementation in the `src/services/tests/` directory.
- Ensure your test follows the structure and conventions used by existing tests.

**Register the Test**
- Add an import and include your test in the exported array in `src/services/tests/AllTests.ts`. This ensures it is picked up and executed as part of the test suite.