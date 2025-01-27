# Site Scanning - Analysis Repo

The [Site Scanning program](https://digital.gov/site-scanning/) automates a wide range of scans of public federal websites and generates data about website health and best practices.

This repository serves as a hub for various analysis reports, which provide summary and analytical data about the information that the Site Scanning program generates.

To ask a question or leave feedback for the program, please [file an issue here](https://github.com/GSA/site-scanning/issues) or email us at site-scanning@gsa.gov.

### Important Links

- [Program Website](https://digital.gov/site-scanning)
- [API Documentation](https://open.gsa.gov/api/site-scanning-api/)
- [Central Project Repository](https://github.com/GSA/site-scanning)
- [Program Documentation Repository](https://github.com/GSA/site-scanning-documentation)
- [Federal Website Index Repository](https://github.com/GSA/federal-website-index)
- [Site Scanning Engine Repository](https://github.com/GSA/site-scanning-engine)
- [Snapshots Repository](https://github.com/GSA/site-scanning-snapshots)
- [Extensive List of Links to Technical Details, Snapshots, Analysis Reports, and More](https://digital.gov/guides/site-scanning/technical-details/) (if in doubt, look here)

### Primary Reports and Analysis
- [Most Reports](https://github.com/GSA/site-scanning-analysis/tree/main/reports)
- [Draft Reports](https://github.com/GSA/site-scanning-analysis/tree/main/reports/drafts)
- [Suggested Improvements to Websites](https://github.com/GSA/site-scanning-analysis/tree/main/reports/website-requests)
- [Unique Website and Unique Final URL Reports](https://github.com/GSA/site-scanning-analysis/tree/main/unique_website_list/results)

### Development

These reports are generated on a continual basis by the following workflows:

- [Generate snapshot and target URL reports](https://github.com/GSA/site-scanning-analysis/blob/main/.github/workflows/generate-all-reports.yml)
- [Generate IDEA reports](https://github.com/GSA/site-scanning-analysis/blob/main/.github/workflows/generate-idea-reports.yml)
- [Generate unique website list](https://github.com/GSA/site-scanning-analysis/blob/main/.github/workflows/generate-unique-website-list.yml)

To run locally, install the necessary dependencies and call the entry point with
a valid command. For example, to generate the report that collects data for all
live websites:

```shell
pip install -r requirements.txt
python3 main.py generate-primary-snapshot-report
```
