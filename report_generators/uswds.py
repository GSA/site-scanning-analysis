import pandas as pd


class Uswds:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        groups = [
            'All sites scanned',
            'All live sites',
            'All live, filtered sites',
            'All live, filtered, non-redirecting sites',
            'Executive sites scanned',
            'Executive live sites',
            'Executive live, filtered sites',
            'Executive live, filtered, non-redirecting sites',
            'Legislative sites scanned',
            'Legislative live sites',
            'Legislative live, filtered sites',
            'Legislative live, filtered, non-redirecting sites',
            'Judicial sites scanned',
            'Judicial live sites',
            'Judicial live, filtered sites',
            'Judicial live, filtered, non-redirecting sites',
            'IDEA sites scanned',
            'IDEA live sites',
            'IDEA live, filtered sites',
            'IDEA live, filtered, non-redirecting sites',
        ]

        results = []
        for group in groups:
            group_df = self._get_group_df(group)
            version_series = group_df['uswds_semantic_version']
            results.append({
                'Group': group,
                'count': len(group_df),
                'Agencies': group_df['agency'].nunique(),
                'semantic version': version_series.notna().sum(),
                'Agencies_sv': group_df.loc[version_series.notna(), 'agency'].nunique(),
                'v1.x': version_series.str.startswith('v1.', na=False).sum(),
                'Agencies_v1': group_df.loc[version_series.str.startswith('v1.', na=False), 'agency'].nunique(),
                'v2.x': version_series.str.startswith('v2.', na=False).sum(),
                'Agencies_v2': group_df.loc[version_series.str.startswith('v2.', na=False), 'agency'].nunique(),
                'v3.x': version_series.str.startswith('v3.', na=False).sum(),
                'Agencies_v3': group_df.loc[version_series.str.startswith('v3.', na=False), 'agency'].nunique(),
                'banner': (group_df['uswds_banner_heres_how'] == True).sum(),
                'Agencies_banner': group_df.loc[group_df['uswds_banner_heres_how'] == True, 'agency'].nunique(),
                'usa-class': group_df['uswds_usa_class_list'].notna().sum(),
                'Agencies_usa_class': group_df.loc[group_df['uswds_usa_class_list'].notna(), 'agency'].nunique(),
            })
        result_df = pd.DataFrame(results)

        return result_df

    def _get_group_df(self, group_name):
        # Start with full dataset or branch subset
        if group_name.startswith('Executive'):
            df = self.df[self.df['branch'].str.lower() == 'executive']
        elif group_name.startswith('Legislative'):
            df = self.df[self.df['branch'].str.lower() == 'legislative']
        elif group_name.startswith('Judicial'):
            df = self.df[self.df['branch'].str.lower() == 'judicial']
        elif group_name.startswith('IDEA'):
            df = self.df[self.df['source_list'].astype(str).str.contains('omb_idea', case=False, na=False)]
        else:
            df = self.df

        # Apply filtering based on scan type
        if 'live, filtered, non-redirecting sites' in group_name:
            return df[(df['live'] == True) & (df['filter'] == True) & (df['redirect'] != True)]
        elif 'live, filtered sites' in group_name:
            return df[(df['live'] == True) & (df['filter'] == True)]
        elif 'live sites' in group_name:
            return df[df['live'] == True]
        else:
            return df
