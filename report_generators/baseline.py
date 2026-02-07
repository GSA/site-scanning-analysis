import pandas as pd


class Baseline:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
      ##### Start website count analysis #####
      # Get a unique url count for all branch websites that are live
      websites_all_df = self.df[self.df['live'] == True]
      websites_all_url_count = websites_all_df['url'].nunique()
      print(f"Total number of unique URLs: {websites_all_url_count}")

      # Get a unique url count for all branch websites that are live and the branch = executive
      websites_executive_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'executive')]
      websites_executive_url_count = websites_executive_df['url'].nunique()
      print(f"Total number of unique URLs for executive branch: {websites_executive_url_count}")

      # Get a unique url count for all branch websites that are live and the branch = legislative
      websites_legislative_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'legislative')]
      websites_legislative_url_count = websites_legislative_df['url'].nunique()
      print(f"Total number of unique URLs for legislative branch: {websites_legislative_url_count}")

      # Get a unique url count for all branch websites that are live and the branch = judicial
      websites_judicial_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'judicial')]
      websites_judicial_url_count = websites_judicial_df['url'].nunique()
      print(f"Total number of unique URLs for judicial branch: {websites_judicial_url_count}")

      ##### End website count analysis #####

      ##### Start base_domains count analysis #####
      # Get a unique base_domain count for all websites that are live
      domains_all_df = self.df[self.df['live'] == True]
      domains_all_url_count = domains_all_df['base_domain'].nunique()
      print(f"Total number of unique base_domains: {domains_all_url_count}")

      # Get a unique base_domain count for all websites that are live and the branch = executive
      domains_executive_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'executive')]
      domains_executive_url_count = domains_executive_df['base_domain'].nunique()
      print(f"Total number of unique base_domains for executive branch: {domains_executive_url_count}")

      # Get a unique base_domain count for all websites that are live and the branch = legislative
      domains_legislative_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'legislative')]
      domains_legislative_url_count = domains_legislative_df['base_domain'].nunique()
      print(f"Total number of unique base_domains for legislative branch: {domains_legislative_url_count}")

      # Get a unique base_domain count for all websites that are live and the branch = judicial
      domains_judicial_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'judicial')]
      domains_judicial_url_count = domains_judicial_df['base_domain'].nunique()
      print(f"Total number of unique base_domains for judicial branch: {domains_judicial_url_count}")

      ##### End Domains count analysis #####

      ##### Start Agencies count analysis #####
      # Get a unique agency count for all websites that are live
      agencies_all_df = self.df[self.df['live'] == True]
      agencies_all_url_count = agencies_all_df['agency'].nunique()
      print(f"Total number of unique agencies: {agencies_all_url_count}")

      # Get a unique agency count for all websites that are live and the branch = executive
      agencies_executive_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'executive')]
      agencies_executive_url_count = agencies_executive_df['agency'].nunique()
      print(f"Total number of unique agencies for executive branch: {agencies_executive_url_count}")

      # Get a unique agency count for all websites that are live and the branch = legislative
      agencies_legislative_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'legislative')]
      agencies_legislative_url_count = agencies_legislative_df['agency'].nunique()
      print(f"Total number of unique agencies for legislative branch: {agencies_legislative_url_count}")

      # Get a unique agency count for all websites that are live and the branch = judicial
      agencies_judicial_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'judicial')]
      agencies_judicial_url_count = agencies_judicial_df['agency'].nunique()
      print(f"Total number of unique agencies for judicial branch: {agencies_judicial_url_count}")

      ##### End Agencies count analysis #####

      ##### Start Bureaus count analysis #####
      # Get a unique bureau count for all branch websites that are live
      bureaus_all_df = self.df[self.df['live'] == True]
      bureaus_all_url_count = bureaus_all_df['bureau'].nunique()
      print(f"Total number of unique bureaus: {bureaus_all_url_count}")

      # Get a unique bureau count for all websites that are live and the branch = executive
      bureaus_executive_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'executive')]
      bureaus_executive_url_count = bureaus_executive_df['bureau'].nunique()
      print(f"Total number of unique bureaus for executive branch: {bureaus_executive_url_count}")

      # Get a unique bureau count for all websites that are live and the branch = legislative
      bureaus_legislative_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'legislative')]
      bureaus_legislative_url_count = bureaus_legislative_df['bureau'].nunique()
      print(f"Total number of unique bureaus for legislative branch: {bureaus_legislative_url_count}")

      # Get a unique bureau count for all websites that are live and the branch = judicial
      bureaus_judicial_df = self.df[(self.df['live'] == True) & (self.df['branch'].str.lower() == 'judicial')]
      bureaus_judicial_url_count = bureaus_judicial_df['bureau'].nunique()
      print(f"Total number of unique bureaus for judicial branch: {bureaus_judicial_url_count}")

      ##### End Bureaus count analysis #####

      ##### Start websites with logins analysis #####
      # Get a count of websites that are live and have a value in either or both of login_provider and login
      websites_login_df = self.df[(self.df['live'] == True) & (self.df['login_provider'].notna() | self.df['login'].notna())]
      websites_login_url_count = websites_login_df['url'].nunique()
      print(f"Total number of websites with logins: {websites_login_url_count}")

      # Get a count of websites that are live and have a value in either or both of login_provider and login and the branch = executive
      websites_login_executive_df = self.df[(self.df['live'] == True) & (self.df['login_provider'].notna() | self.df['login'].notna()) & (self.df['branch'].str.lower() == 'executive')]
      websites_login_executive_url_count = websites_login_executive_df['url'].nunique()
      print(f"Total number of websites with logins for executive branch: {websites_login_executive_url_count}")

      # Get a count of websites that are live and have a value in either or both of login_provider and login and the branch = legislative
      websites_login_legislative_df = self.df[(self.df['live'] == True) & (self.df['login_provider'].notna() | self.df['login'].notna()) & (self.df['branch'].str.lower() == 'legislative')]
      websites_login_legislative_url_count = websites_login_legislative_df['url'].nunique()
      print(f"Total number of websites with logins for legislative branch: {websites_login_legislative_url_count}")

      # Get a count of websites that are live and have a value in either or both of login_provider and login and the branch = judicial
      websites_login_judicial_df = self.df[(self.df['live'] == True) & (self.df['login_provider'].notna() | self.df['login'].notna()) & (self.df['branch'].str.lower() == 'judicial')]
      websites_login_judicial_url_count = websites_login_judicial_df['url'].nunique()
      print(f"Total number of websites with logins for judicial branch: {websites_login_judicial_url_count}")

      ##### End websites with logins analysis #####

      # Build the new DataFrame
      categories = ['Websites', 'Domains', 'Agencies', 'Bureaus', 'Websites with Logins']
      data = {
          'Name': categories,
          'All Branches': [websites_all_url_count, domains_all_url_count, agencies_all_url_count, bureaus_all_url_count, websites_login_url_count],
          'Executive': [websites_executive_url_count, domains_executive_url_count, agencies_executive_url_count, bureaus_executive_url_count, websites_login_executive_url_count],
          'Legislative': [websites_legislative_url_count, domains_legislative_url_count, agencies_legislative_url_count, bureaus_legislative_url_count, websites_login_legislative_url_count],
          'Judicial': [websites_judicial_url_count, domains_judicial_url_count, agencies_judicial_url_count, bureaus_judicial_url_count, websites_login_judicial_url_count]
      }

      result_df = pd.DataFrame(data)
      
      return result_df