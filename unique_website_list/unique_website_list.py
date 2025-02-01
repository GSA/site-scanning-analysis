from config import config
import pandas as pd


def generate_unique_website_list():
    # Load snapshot CSV and save
    df = pd.read_csv(config['primary_snapshot_url'], low_memory=False)
    df.to_csv(config['initial_dataset_location'], index=False)

    # Drop rows with duplicate final_url values and save
    removed_df = df.loc[df.duplicated('url')]
    removed_df.to_csv(config['removed_final_urls_location'], index=False)
    df = df.drop_duplicates('url', keep='first')
    df.to_csv(config['unique_final_urls_location'], index=False)

    # Reindex by length of final_url
    s = df.url.str.len().sort_values().index
    df = df.reindex(s)

    # Drop rows with duplicate final_url_website values and save
    blank_final_url_website_df = df[df['domain'].isna()]
    df = df[~df['domain'].isna()]
    removed_df = df.loc[df.duplicated('domain')]
    removed_df.to_csv(config['removed_final_url_websites_location'], index=False)
    df = df.drop_duplicates('domain', keep='first')
    df = df.sort_values(by='domain')
    final_df = pd.concat([df, blank_final_url_website_df])
    final_df.to_csv(config['unique_final_websites_location'], index=False)
