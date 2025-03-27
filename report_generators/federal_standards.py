import pandas as pd


class FederalStandardsSnapshot:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
      final_columns = [
        'name',
        'initial_domain',
        'initial_base_domain',
        'url',
        'domain',
        'base_domain',
        'agency',
        'bureau',
        'branch',
        'scan_date',
        'uswds_banner_heres_how',
        'title',
        'description'
      ]
      result_df = self.df[final_columns]
      
      return result_df