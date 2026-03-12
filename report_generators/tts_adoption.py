import pandas as pd


class TtsAdoption:
    def __init__(self, df):
        self.df = df

    def _base(self):
        df = self.df
        return df[
            (df['live'] == True) &
            (df['redirect'] == False) &
            (df['filter'] == False)
        ]

    def _count_agencies(self, filtered_df):
        return filtered_df['agency'].nunique()

    def generate_report(self):
        base = self._base()

        dap = base[base['dap'] == True]
        uswds = base[base['uswds_banner_heres_how'] == True]
        cloud_gov = base[base['hostname'].str.contains('cloud.gov', na=False)]
        cloud_gov_pages = base[base['cms'].str.lower().str.strip() == 'cloud.gov pages']
        login_gov = base[base['login_provider'].str.contains('login.gov', na=False)]
        logins = base[base['login'].notna() & (base['login'].str.strip() != '')]
        search_gov = base[base['search_dot_gov'] == True]
        search = base[base['site_search'] == True]
        touchpoints = base[base['third_party_service_domains'].str.contains('touchpoints', na=False)]

        report = {
            'Live, Production, Unique Websites': len(base),
            'Agencies': self._count_agencies(base),
            'DAP_websites': len(dap),
            'DAP_agencies': self._count_agencies(dap),
            'uswds_websites': len(uswds),
            'uswds_agencies': self._count_agencies(uswds),
            'cloud.gov_websites': len(cloud_gov),
            'cloud.gov_agencies': self._count_agencies(cloud_gov),
            'cloud.gov-pages_websites': len(cloud_gov_pages),
            'cloud.gov-pages_agencies': self._count_agencies(cloud_gov_pages),
            'login.gov_websites': len(login_gov),
            'login.gov_agencies': self._count_agencies(login_gov),
            'logins': len(logins),
            'logins_agencies': self._count_agencies(logins),
            'search.gov_websites': len(search_gov),
            'search.gov_agencies': self._count_agencies(search_gov),
            'search_websites': len(search),
            'search_agencies': self._count_agencies(search),
            'touchpoints_websites': len(touchpoints),
            'touchpoints_agencies': self._count_agencies(touchpoints),
            'data.gov_websites': 868,
            'data.gov_agencies': 50,
            'api.data.gov_endpoints': 663,
            'api.data.gov_agencies': 25,
        }

        return pd.DataFrame(
            list(report.items()),
            columns=['metric', 'value']
        )
