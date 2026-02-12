import pandas as pd


URLS_THAT_ALWAYS_ERROR_OUT_CSV_PATH = './your/file/path/always-execution-context-destroyed.csv'
RESULTS_OVER_TIME_CSV_PATH = './your/file/path/results-over-time.csv'


def get_df(db_name: str):
    """
    This function could be set up to pull data from a local copy of the postgres
    database. It could also be reworked to pull from the publicly hosted snapshot CSV
    if we move from weekly to daily snapshot generation.
    """
    pass


def get_urls_that_always_error_out(dfs: list):
    combined_df = pd.concat(dfs)
    grouped = combined_df.groupby('url')['primaryScanStatus'].apply(lambda x: (x == 'execution_context_destroyed').all())
    filtered_urls = grouped[grouped].index

    url_series = pd.Series(filtered_urls)
    url_series.to_csv(URLS_THAT_ALWAYS_ERROR_OUT_CSV_PATH, index=False)


def get_status_over_time(dfs: list):
    relevant_url_df = pd.concat([df[df['primaryScanStatus'] == 'execution_context_destroyed'] for df in dfs])['url'].drop_duplicates().reset_index(drop=True)
    result_df = pd.DataFrame(relevant_url_df, columns=['url'])

    def add_status_columns(df, result_df, df_name):
        status_df = df[['url', 'primaryScanStatus']].rename(columns={
            'primaryScanStatus': f'{df_name}_primaryScanStatus',
        })
        return result_df.merge(status_df, on='url', how='left')

    for i, df in enumerate(dfs):
        result_df = add_status_columns(df, result_df, f'df{i+1}')

    result_df.to_csv(RESULTS_OVER_TIME_CSV_PATH, index=False)


def main():
    print('running execution_context_destroyed script')
    databases = [
        # names of local database backups go here
    ]
    dfs = []
    for db in databases:
        dfs.append(get_df(db))

    get_status_over_time(dfs)
    get_urls_that_always_error_out(dfs)


if __name__ == '__main__':
    main()
