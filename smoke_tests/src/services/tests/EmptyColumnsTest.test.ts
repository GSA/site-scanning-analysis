import { describe, test, expect } from 'bun:test';
import { EmptyColumnsTest } from './EmptyColumnsTest';
import { SnapshotLoader } from '../SnapshotLoader';
import { GithubIssueService } from '../GithubIssueService';
import { DataFrame } from 'dataframe-js';

function makeDataFrame(rows: Record<string, unknown>[]): DataFrame {
  return new DataFrame(rows);
}

type IssueCaptured = { title: string; body: string };

function stubServices(df: DataFrame | 'throw'): {
  issues: IssueCaptured[];
  patch: () => void;
  restore: () => void;
} {
  const issues: IssueCaptured[] = [];

  const origLoad = SnapshotLoader.prototype.load;
  // GithubIssueService constructor throws without ISSUE_TOKEN. It needs a stub for tests.
  const origCtor = GithubIssueService.prototype.constructor;

  const patch = () => {
    // @ts-ignore
    GithubIssueService.prototype.constructor = function () {};

    SnapshotLoader.prototype.load = async () => {
      if (df === 'throw') throw new Error('Network failure');
      return df;
    };
  };

  const restore = () => {
    SnapshotLoader.prototype.load = origLoad;
    // @ts-ignore
    GithubIssueService.prototype.constructor = origCtor;
  };

  return { issues, patch, restore };
}

describe('EmptyColumnsTest', () => {
  async function runCase(
    df: DataFrame | 'throw',
    excludedColumns: string[],
    expected: {
      result: boolean;
      issueCount: number;
      titleContains?: string;
      bodyContains?: string[];
    }
  ) {
    const { issues, patch, restore } = stubServices(df);
    patch();

    let result: boolean = false;
    try {
      const instance = Object.create(EmptyColumnsTest.prototype) as EmptyColumnsTest;
      // @ts-ignore — directly set private fields
      instance.snapshotPath = 'stub://snapshot.csv';
      // @ts-ignore
      instance.excludedColumns = new Set(excludedColumns);
      // @ts-ignore
      instance.issueCreator = new (class FakeIssueCreator {
        async createIssue(title: string, body: string) {
          issues.push({ title, body });
        }
      })();

      result = await instance.runTest();
    } finally {
      restore();
    }

    const errors: string[] = [];

    if (result !== expected.result) {
      errors.push(`return value: got ${result}, want ${expected.result}`);
    }
    if (issues.length !== expected.issueCount) {
      errors.push(`issue count: got ${issues.length}, want ${expected.issueCount}`);
    }
    if (expected.titleContains && issues[0] && !issues[0].title.includes(expected.titleContains)) {
      errors.push(`issue title "${issues[0].title}" does not contain "${expected.titleContains}"`);
    }
    if (expected.bodyContains) {
      const body = issues[0]?.body ?? '';
      for (const fragment of expected.bodyContains) {
        if (!body.includes(fragment)) {
          errors.push(`issue body missing fragment: "${fragment}"`);
        }
      }
    }

    expect(errors, `Failures:\n${errors.join('\n')}`).toHaveLength(0);
  }

  test(
    'all columns have data → returns true, no issue filed',
    async () => {
      await runCase(
        makeDataFrame([
          { https_enforced: 'TRUE', hsts: 'TRUE', pageviews: 100, visits: 50 },
          { https_enforced: 'FALSE', hsts: 'FALSE', pageviews: 0, visits: 10 },
        ]),
        [],
        { result: true, issueCount: 0 }
      );
    }
  );

  test(
    'one column entirely empty → returns false, 1 issue filed',
    async () => {
      await runCase(
        makeDataFrame([
          { https_enforced: '', hsts: 'TRUE', pageviews: 100, visits: 50 },
          { https_enforced: '', hsts: 'FALSE', pageviews: 0, visits: 10 },
        ]),
        [],
        {
          result: false,
          issueCount: 1,
          titleContains: 'Empty or Null Columns',
          bodyContains: ['https_enforced'],
        }
      );
    }
  );

  test(
    'multiple empty columns → returns false, 1 issue listing all',
    async () => {
      await runCase(
        makeDataFrame([
          { https_enforced: 'TRUE', hsts: 'TRUE', pageviews: '', visits: '' },
          { https_enforced: 'FALSE', hsts: 'FALSE', pageviews: '', visits: '' },
        ]),
        [],
        {
          result: false,
          issueCount: 1,
          titleContains: 'Empty or Null Columns',
          bodyContains: ['pageviews', 'visits'],
        }
      );
    }
  );

  test(
    'excluded column is empty → returns true, no issue filed',
    async () => {
      await runCase(
        makeDataFrame([
          { https_enforced: 'TRUE', hsts: '', pageviews: 100, visits: 50 },
          { https_enforced: 'FALSE', hsts: '', pageviews: 0, visits: 10 },
        ]),
        ['hsts'],
        { result: true, issueCount: 0 }
      );
    }
  );

  test(
    // NOTE: unlike ColumnValuePresenceTest, EmptyColumnsTest does not catch load
    // errors — the thrown error propagates to the caller.
    'snapshot load throws → propagates the error',
    async () => {
      const { patch, restore } = stubServices('throw');
      patch();
      try {
        await expect(async () => {
          const instance = Object.create(EmptyColumnsTest.prototype) as EmptyColumnsTest;
          // @ts-ignore
          instance.snapshotPath = 'stub://snapshot.csv';
          // @ts-ignore
          instance.excludedColumns = new Set([]);
          // @ts-ignore
          instance.issueCreator = new (class FakeIssueCreator {
            async createIssue(_title: string, _body: string) {}
          })();
          await instance.runTest();
        }).toThrow('Network failure');
      } finally {
        restore();
      }
    }
  );
});
