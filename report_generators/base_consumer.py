import pandas as pd


class BaseConsumer:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
      column_mappings = {
          'name': 'website',
          'base_domain': 'domain',
          'agency': 'agency',
          'bureau': 'bureau',
          'visits': 'visits',
          'pageviews': 'pageviews',
          'search_dot_gov': 'search.gov',
          'hostname': 'cloud provider',
          'cms': 'CMS provider',
          'login_provider': 'login provider',
          'login': 'has a login',
          'dap': 'dap',
          'third_party_service_domains': 'third_party_service_domains',
          'uswds_banner_heres_how': 'uswds_banner_heres_how',
          'site_search': 'site_search'
      }
      columns_to_keep = list(column_mappings.keys())
      result_df = self.df[columns_to_keep].copy()

      result_df['cloud.gov'] = result_df['hostname'].apply(lambda x: 'TRUE' if 'cloud.gov' in str(x) else '')
      result_df['cloud.gov pages'] = result_df['cms'].apply(lambda x: 'TRUE' if str(x).lower() == 'cloud.gov pages' else '')
      result_df['login.gov'] = result_df['login_provider'].apply(lambda x: 'TRUE' if 'login.gov' in str(x) else '')
      result_df['dap'] = result_df['dap'].apply(lambda x: 'TRUE' if str(x).upper() == 'TRUE' else '')
      result_df['touchpoints'] = result_df['third_party_service_domains'].apply(lambda x: x if pd.notna(x) and x != '' else '')
      result_df['uswds'] = result_df['uswds_banner_heres_how'].apply(lambda x: 'TRUE' if str(x).upper() == 'TRUE' else '')
      result_df['has site search'] = result_df['site_search'].apply(lambda x: 'TRUE' if str(x).upper() == 'TRUE' else '')

      # Rename the columns
      result_df = result_df.rename(columns=column_mappings)

      final_columns = [
          'website', 'domain', 'agency', 'bureau', 'visits', 'pageviews', 'search.gov', 
          'cloud provider', 'CMS provider', 'login provider', 'has a login', 'cloud.gov', 
          'cloud.gov pages', 'login.gov', 'dap', 'touchpoints', 'uswds', 'has site search'
      ]

      result_df = result_df[final_columns]

      return result_df