# AGENTS.md

Analysis scripts for the GSA Site Scanning program. Pulls public CSV snapshots from `api.gsa.gov` and writes summary reports back into the repo (which CI auto-commits).

## Two sub-projects

- **Root (Python 3.9, pandas-only):** report generators driven by `main.py`.
- **`smoke_tests/` (Bun + TypeScript):** independent suite that validates the published snapshot data and files GitHub issues on failure. Has its own `package.json`, `README.md`, and CI workflow. Do not mix it with the Python code.

## Run a report

```sh
pip install -r requirements.txt
python3 main.py <command>
```

Valid commands live in the `valid_commands` dict in `main.py:127-145`. They are the source of truth — names are not all `generate-*` (e.g. `federal-standards-snapshot-report`, `website-requests-report`).

Most commands fetch a remote CSV (URLs in `config.py`) so they need network access. There is no local data seeding step.

`main.py:123` disables SSL verification globally (`ssl._create_default_https_context = ssl._create_unverified_context`). Leave it unless you have a reason; CI relies on it.

## Tests

```sh
python3 -m unittest discover tests
```

Stdlib `unittest`, not pytest. Fixtures are committed CSVs next to the tests (`tests/test_*.csv`). CI (`.github/workflows/test.yml`) pins Python 3.9.

Smoke tests are separate:

```sh
cd smoke_tests && bun install && bun run src/main.ts
```

`ISSUE_TOKEN` is required — without it the runner logs an error and exits before running any tests (it doesn't just skip issue creation). Register new smoke tests in `smoke_tests/src/services/tests/AllTests.ts`.

## Report output paths are tracked artifacts

CSV outputs in `reports/`, `snapshots/`, and `unique_website_list/results/` are committed back to `main` by the scheduled workflows in `.github/workflows/generate-*.yml` (via `git-auto-commit-action`). Treat them as generated but versioned — don't hand-edit, and expect noisy diffs after a local run.

`reports/drafts/` and `reports/website-requests/` (with their own READMEs) are curated content, not pure outputs.

## Adding a new report

1. Add a generator class under `report_generators/` (mirror the existing pattern: take a `df` in `__init__`, expose `generate_report()`).
2. Add the input URL and output path to `config.py`.
3. Add a wrapper function in `main.py` and register it in `valid_commands`.
4. Add the command to the relevant workflow under `.github/workflows/` if it should run on schedule.
5. Add a `tests/test_*.py` with a small fixture CSV.

## Architecture notes

- `main.py` is a thin dispatcher: read remote CSV → instantiate generator → write CSV. Almost all logic lives in `report_generators/`.
- The "snapshot" report (`Snapshot` class) is a question→answer dict serialized via `save_to_csv` with `['question', 'answer']` columns. Other generators (`Idea`, `Standards`, `Baseline`, etc.) return a DataFrame and write it directly. Don't conflate the two output shapes.
- `unique_website_list/unique_website_list.py` is invoked via `main.py generate-unique-website-list` and produces the dedup'd CSVs that several downstream reports consume (`unique_final_websites_location`).
