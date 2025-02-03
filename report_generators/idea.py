import pandas as pd


class Idea:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        result_df = self.df.groupby('agency').agg(
            total_records=('agency', 'size'),
            dap_count=('dap', lambda x: x[x == True].count()),
            dap_percentage=('dap', lambda x: round((x[x == True].count() / x.count() * 100), 2)),
            uswds_count=('uswds_semantic_version', lambda x: x.notna().sum()),
            uswds_percentage=('uswds_semantic_version', lambda x: round((x.notna().sum() / len(x) * 100), 2)),
        ).reset_index()


        totals_row = pd.DataFrame({'agency': ['Total'],
                    'total_records': [sum(result_df['total_records'])],
                    'dap_count': [sum(result_df['dap_count'])],
                    'dap_percentage': [round((sum(result_df['dap_count'] / sum(result_df['total_records']))) * 100, 2)],
                    'uswds_count': [sum(result_df['uswds_count'])],
                    'uswds_percentage': [round((sum(result_df['uswds_count'] / sum(result_df['total_records']))) * 100, 2)],
        })

        result_df = pd.concat([result_df, totals_row], ignore_index=True)

        column_mapping = {'agency': 'Agency',
                        'total_records': 'Number of Websites',
                        'dap_count': 'Number of Websites with DAP',
                        'dap_percentage': 'Percent with DAP',
                        'uswds_count': 'Number of Websites with USWDS Semantic Version',
                        'uswds_percentage': 'Percent of Websites with USWDS Semantic Version'}

        result_df = result_df.rename(columns=column_mapping)

        return result_df

    def generate_bureaus_report(self):
        result_df = self.df.groupby(['agency', 'bureau']).agg(
            total_records=('bureau', 'size'),
            dap_count=('dap', lambda x: x[x == True].count()),
            dap_percentage=('dap', lambda x: round((x[x == True].count() / x.count() * 100), 2)),
            uswds_count=('uswds_semantic_version', lambda x: x.notna().sum()),
            uswds_percentage=('uswds_semantic_version', lambda x: round((x.notna().sum() / len(x) * 100), 2)),
        ).reset_index()

        column_mapping = {'agency': 'Agency',
                        'bureau': 'Bureau',
                        'total_records': 'Number of Websites',
                        'dap_count': 'Number of Websites with DAP',
                        'dap_percentage': 'Percent with DAP',
                        'uswds_count': 'Number of Websites with USWDS Semantic Version',
                        'uswds_percentage': 'Percent of Websites with USWDS Semantic Version'}

        result_df = result_df.rename(columns=column_mapping)

        return result_df
