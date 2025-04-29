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
