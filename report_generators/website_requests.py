import pandas as pd


class WebsiteRequests:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        df = self.df.copy()
        columns_to_keep = ['initial_url', 'initial_domain', 'url', 'domain', 'agency', 'bureau']

        results = []

        # 1. Suspected meta redirect
        redirect_check = df[(df['redirect'] == True) & df['pageviews'].notna()]
        redirect_check = redirect_check[columns_to_keep].copy()
        redirect_check['issue'] = 'suspected meta redirect'
        results.append(redirect_check)

        # 2. SSL issue
        ssl_statuses = ['invalid_ss_cert', 'ssl_protocol_error', 'ssl_version_cipher_mismatch']
        ssl_check = df[df['primary_scan_status'].isin(ssl_statuses)]
        ssl_check = ssl_check[columns_to_keep].copy()
        ssl_check['issue'] = 'SSL'
        results.append(ssl_check)

        # 3. 404 test
        not_found_check = df[df['404_test'] == True]
        not_found_check = not_found_check[columns_to_keep].copy()
        not_found_check['issue'] = '404'
        results.append(not_found_check)

        # 4. www-required
        www_required_check = df[
            ((df['status_code'] >= 400) & (df['status_code'] < 600)) &
            ((df['www_status_code'] >= 200) & (df['www_status_code'] < 300))
        ]
        www_required_check = www_required_check[columns_to_keep].copy()
        www_required_check['issue'] = 'www-required'
        results.append(www_required_check)

        # 5. www-forbidden
        www_forbidden_check = df[
            (df['initial_domain'] == df['initial_base_domain']) &
            ((df['www_status_code'] >= 400) & (df['www_status_code'] < 600)) &
            ((df['status_code'] >= 200) & (df['status_code'] < 300))
        ]
        www_forbidden_check = www_forbidden_check[columns_to_keep].copy()
        www_forbidden_check['issue'] = 'www-forbidden'
        results.append(www_forbidden_check)

        # 6. Blocking scans (title contains specific string)
        blocking_scans_check = df[df['title'].str.contains(
            "This site has determined a security issue with your request",
            case=False, na=False
        )]
        blocking_scans_check = blocking_scans_check[columns_to_keep].copy()
        blocking_scans_check['issue'] = 'blocking scans'
        results.append(blocking_scans_check)

        # Combine all matched rows
        final_results = pd.concat(results, ignore_index=True)

        return final_results