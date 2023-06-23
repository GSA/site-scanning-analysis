import os


dirname = os.path.dirname(__file__)

config = {
    # snapshots
    'primary_snapshot_url': 'https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot.csv',
    'all_snapshot_url': 'https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot-all.csv',
    'target_url_list_url': 'https://raw.githubusercontent.com/GSA/federal-website-index/main/data/site-scanning-target-url-list.csv',
    # report file locations
    'primary_snapshot_report_location': os.path.join(dirname, './reports/snapshot-primary.csv'),
    'all_snapshot_report_location': os.path.join(dirname, './reports/snapshot-all.csv'),
    'unique_url_report_location': os.path.join(dirname, './reports/unique-url.csv'),
    'unique_website_report_location': os.path.join(dirname, './reports/unique-website.csv'),
    'target_url_list_report_location': os.path.join(dirname, './reports/target-url-list.csv'),
    # unique url and website file locations
    'initial_dataset_location': os.path.join(dirname, './unique_website_list/results/initial_dataset.csv'),
    'unique_final_urls_location': os.path.join(dirname, './unique_website_list/results/weekly-snapshot-unique-final-urls.csv'),
    'unique_final_websites_location': os.path.join(dirname, './unique_website_list/results/weekly-snapshot-unique-final-websites.csv'),
    'removed_final_urls_location': os.path.join(dirname, './unique_website_list/results/removed-final-urls.csv'),
    'removed_final_url_websites_location': os.path.join(dirname, './unique_website_list/results/removed-final-url-websites.csv'),
}
