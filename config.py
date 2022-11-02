import os


dirname = os.path.dirname(__file__)

config = {
    'primary_snapshot_url': 'https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot.json',
    'all_snapshot_url': 'https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot-all.json',
    'target_url_list_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/site-scanning-target-url-list.csv',
    'primary_snapshot_report_location': os.path.join(dirname, './reports/snapshot-primary.csv'),
    'all_snapshot_report_location': os.path.join(dirname, './reports/snapshot-all.csv'),
    'target_url_list_report_location': os.path.join(dirname, './reports/target-URL-list.csv'),
}
