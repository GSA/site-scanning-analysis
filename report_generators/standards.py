import pandas as pd


class Standards:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        result_df = self.df.groupby('agency').agg(
            total_records=('agency', 'size'),
            title_count=('title', lambda x: (x.notna() & (x != '')).sum()),
            description_count=('description', lambda x: (x.notna() & (x != '')).sum()),
            uswds_true_count=('uswds_banner_heres_how', lambda x: int(x.sum())),
        ).reset_index()

        result_df['title_not_empty_pct'] = round(result_df['title_count'] / result_df['total_records'] * 100, 2)
        result_df['description_not_empty_pct'] = round(result_df['description_count'] / result_df['total_records'] * 100, 2)
        result_df['uswds_true_pct'] = round(result_df['uswds_true_count'] / result_df['total_records'] * 100, 2)

        totals_row = pd.DataFrame({'agency': ['Total'],
                    'total_records': [sum(result_df['total_records'])],
                    'title_count': [sum(result_df['title_count'])],
                    'description_count': [sum(result_df['description_count'])],
                    'uswds_true_count': [sum(result_df['uswds_true_count'])],
                    'title_not_empty_pct': [round((sum(result_df['title_count'] / sum(result_df['total_records']))) * 100, 2)],
                    'description_not_empty_pct': [round((sum(result_df['description_count'] / sum(result_df['total_records']))) * 100, 2)],
                    'uswds_true_pct': [round((sum(result_df['uswds_true_count'] / sum(result_df['total_records']))) * 100, 2)],
        })

        result_df = pd.concat([result_df, totals_row], ignore_index=True)

        column_mapping = {'agency': 'Agency',
                        'total_records': 'Number of Websites',
                        'title_count': 'Number of Websites With Page Title',
                        'description_count': 'Number of Websites With Page Description',
                        'uswds_true_count': 'Number of Websites with Government Banner',
                        'title_not_empty_pct': 'Percent of Websites With Page Title',
                        'description_not_empty_pct': 'Percent of Websites With Page Description',
                        'uswds_true_pct': 'Percent of Websites with Government Banner'}

        result_df = result_df.rename(columns=column_mapping)

        return result_df

    def generate_bureaus_report(self):
        result_df = self.df.groupby(['agency', 'bureau']).agg(
            total_records=('agency', 'size'),
            title_count=('title', lambda x: (x.notna() & (x != '')).sum()),
            description_count=('description', lambda x: (x.notna() & (x != '')).sum()),
            uswds_true_count=('uswds_banner_heres_how', 'sum'),
        ).reset_index()

        result_df['title_not_empty_pct'] = round(result_df['title_count'] / result_df['total_records'] * 100, 2)
        result_df['description_not_empty_pct'] = round(result_df['description_count'] / result_df['total_records'] * 100, 2)
        print(result_df.columns)
        result_df['uswds_true_pct'] = round(result_df['uswds_true_count'] / result_df['total_records'] * 100, 2)

        column_mapping = {'agency': 'Agency',
                        'bureau': 'Bureau',
                        'total_records': 'Number of Websites',
                        'title_count': 'Number of Websites With Page Title',
                        'description_count': 'Number of Websites With Page Description',
                        'uswds_true_count': 'Number of Websites with Government Banner',
                        'title_not_empty_pct': 'Percent of Websites With Page Title',
                        'description_not_empty_pct': 'Percent of Websites With Page Description',
                        'uswds_true_pct': 'Percent of Websites with Government Banner'}

        result_df = result_df.rename(columns=column_mapping)

        return result_df
