import pandas as pd


class Idea:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        result_df = self.df.groupby('target_url_agency_owner').agg(
            total_records=('target_url_agency_owner', 'size'),
            dap_count=('dap_detected_final_url', lambda x: x[x == True].count()),
            dap_percentage=('dap_detected_final_url', lambda x: round((x[x == True].count() / x.count() * 100), 2)),
            uswds_count=('uswds_semantic_version', lambda x: x.notna().sum()),
            uswds_percentage=('uswds_semantic_version', lambda x: ((x.notna().sum() / x.count()) * 100).round(2) if x.count() > 0 else 0)
        ).reset_index()


        totals_row = pd.DataFrame({'target_url_agency_owner': ['Total'],
                    'total_records': [sum(result_df['total_records'])],
                    'dap_count': [sum(result_df['dap_count'])],
                    'dap_percentage': [round((sum(result_df['dap_count'] / sum(result_df['total_records']))) * 100, 2)],
                    'uswds_count': [sum(result_df['uswds_count'])],
                    'uswds_percentage': [round((sum(result_df['uswds_count'] / sum(result_df['total_records']))) * 100, 2)],
        })

        result_df = pd.concat([result_df, totals_row], ignore_index=True)

        column_mapping = {'target_url_agency_owner': 'Agency',
                        'total_records': 'Number of Websites',
                        'dap_count': 'Number of Websites with DAP',
                        'dap_percentage': 'Percent with DAP',
                        'uswds_count': 'Number of Websites with USWDS Semantic Version',
                        'uswds_percentage': 'Percent of Websites with USWDS Semantic Version'}

        result_df = result_df.rename(columns=column_mapping)

        return result_df

    def generate_bureaus_report(self):
        result_df = self.df.groupby(['target_url_agency_owner', 'target_url_bureau_owner']).agg(
            total_records=('target_url_bureau_owner', 'size'),
            dap_count=('dap_detected_final_url', lambda x: x[x == True].count()),
            dap_percentage=('dap_detected_final_url', lambda x: round((x[x == True].count() / x.count() * 100), 2)),
            uswds_count=('uswds_semantic_version', lambda x: x.notna().sum()),
            uswds_percentage=('uswds_semantic_version', lambda x: ((x.notna().sum() / x.count()) * 100).round(2) if x.count() > 0 else 0)
        ).reset_index()

        column_mapping = {'target_url_agency_owner': 'Agency',
                        'target_url_bureau_owner': 'Bureau',
                        'total_records': 'Number of Websites',
                        'dap_count': 'Number of Websites with DAP',
                        'dap_percentage': 'Percent with DAP',
                        'uswds_count': 'Number of Websites with USWDS Semantic Version',
                        'uswds_percentage': 'Percent of Websites with USWDS Semantic Version'}

        result_df = result_df.rename(columns=column_mapping)

        return result_df
