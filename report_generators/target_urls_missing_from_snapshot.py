import pandas as pd


class TargetUrlsMissingFromSnapshot:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        target_url_list = self.df[['initial_url']].copy()
        snapshot_url_list = pd.read_csv('https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot-all.csv', usecols=['initial_domain'])

        target_url_list['initial_url'] = target_url_list['initial_url'].str.strip().str.lower()
        snapshot_url_list['initial_domain'] = snapshot_url_list['initial_domain'].str.strip().str.lower()

        print(f"Target URL Count: {len(target_url_list)}")
        print(f"Snapshot URL Count: {len(snapshot_url_list)}")

        missing_urls = target_url_list[~target_url_list['initial_url'].isin(snapshot_url_list['initial_domain'])]

        print(f"Missing URLs Count: {len(missing_urls)}")

        missing_urls = missing_urls.rename(columns={'initial_url': 'missing_url'})

        return missing_urls