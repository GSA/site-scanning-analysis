import os


dirname = os.path.dirname(__file__)

config = {
    'primary_snapshot_url': 'https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot.json',
    'all_snapshot_url': 'https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot-all.json',
    'primary_snapshot_report_location': os.path.join(dirname, './reports/snapshot-primary'),
    'all_snapshot_report_location': os.path.join(dirname, './reports/snapshot-all'),
}
