import pandas as pd


class Snapshot:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        return {
            'How many urls did we scan?': self.num_records(),
            'How many agency owners are represented?': self.num_unique('agency'),
            'How many bureau owners are represented?': self.num_unique('bureau'),
            'How many domains did we scan?': self.num_unique('initial_base_domain'),
            'How many final urls are represented?': self.num_unique('url'),
            'How many final domains are represented?': self.num_unique('base_domain'),
            'How many urls are from the executive branch?': self.branch('Executive'),
            'How many urls are from the legislative branch?': self.branch('Legislative'),
            'How many urls are from the judicial branch?': self.branch('Judicial'),
            'How many home scans completed?': self.num_completed('primary_scan_status'),
            'How many home scans failed?': self.num_not_completed('primary_scan_status'),
            'How many home scans failed because of a refused connection?': self.failed_connection_refused(),
            'How many home scans failed because of a reset connection?': self.failed_connection_reset(),
            'How many home scans failed because of dns resolution?': self.failed_dns_resolution(),
            'How many home scans failed because of invalid ssl certs?': self.failed_invalid_ssl(),
            'How many home scans failed because of timeouts?': self.failed_timeout(),
            'How many home scans failed for unknown reasons?': self.failed_unkown(),
            'How many home scans were aborted?': self.failed_aborted(),
            'How many home scans failed because address was unreachable?': self.failed_address_unreachable(),
            'How many home scans failed because connection was closed?': self.failed_connection_closed(),
            'How many home scans failed because of empty response?': self.failed_empty_response(),
            'How many home scans failed because execution context was destroyed?': self.failed_execution_context_destroyed(),
            'How many home scans failed because of http2 error?': self.failed_http2_error(),
            'How many home scans failed because of invalid auth credentials?': self.failed_invalid_auth_credentials(),
            'How many home scans failed because of invalid response?': self.failed_invalid_response(),
            'How many home scans failed because of ssl protocol error?': self.failed_ssl_protocol_error(),
            'How many home scans failed because of ssl version cipher mismatch?': self.failed_ssl_version_cipher_mismatch(),
            'How many home scans failed because of too many redirects?': self.failed_too_many_redirects(),
            'How many final urls are html files?': self.final_url_mimetype_html(),
            'How many final urls are text files?': self.final_url_mimetype_plain_text(),
            'How many final urls are json files?': self.final_url_mimetype_json(),
            'How many final urls are xml files?': self.final_url_mimetype_xml(),
            'How many final urls are another filetype?': self.final_url_mimetype_other(),
            # 'How many final urls are on the same domain as the target urls?': self.num_true('final_url_same_domain'),
            # 'How many final urls are on the same website as the target urls?': self.num_true('final_url_same_website'),
            'How many urls return a 2xx server code?': self.num_status_200('status_code'),
            'How many urls return a 3xx server code?': self.num_status_300('status_code'),
            'How many urls return a 4xx server code?': self.num_status_400('status_code'),
            'How many urls return a 5xx server code?': self.num_status_500('status_code'),
            'How many urls pass the 404 test?': self.num_true('404_test'),
            'How many urls fail the 404 test?': self.num_false('404_test'),
            'How many not found scans completed?': self.num_completed('not_found_scan_status'),
            'How many not found scans failed?': self.num_not_completed('not_found_scan_status'),
            'How many robots.txt scans completed?': self.num_completed('robots_txt_scan_status'),
            'How many robots.txt scans failed?': self.num_not_completed('robots_txt_scan_status'),
            'How many sitemap.xml scans completed?': self.num_completed('sitemap_xml_scan_status'),
            'How many sitemap.xml scans failed?': self.num_not_completed('sitemap_xml_scan_status'),
            'How many DNS scans completed?': self.num_completed('dns_scan_status'),
            'How many DNS scans failed?': self.num_not_completed('dns_scan_status'),
            'How many urls have a uswds count below 50?': self.num_between('uswds_count', 0, 50),
            'How many urls have a uswds count 51-100?': self.num_between('uswds_count', 51, 100),
            'How many urls have a uswds count 101-150?': self.num_between('uswds_count', 101, 150),
            'How many urls have a uswds count 151+?': self.num_between('uswds_count', 151, 1000),
            'How many urls have dap detected?': self.num_true('dap'),
            'How many urls don\'t have dap detected?': self.num_false('dap'),
            'How many urls weren\'t scanned for DAP (failed scans)?': self.num_na('dap'),
            'How many urls have an og_title?': self.num_not_na('og_title'),
            'How many urls have an og_description?': self.num_not_na('og_description'),
            'How many urls have an og_title but don\'t have an og_description?': self.has_og_title_no_description(),
            'How many urls have an og_description but don\'t have an og_title?': self.has_og_description_no_title(),
            'How many urls have an og_article_published?': self.num_not_na('og_article_published'),
            'How many urls have an og_article_modified?': self.num_not_na('og_article_modified'),
            'How many urls have a main_element_present?': self.num_true('main_element_present'),
            'How many urls don\'t have main_element_present_final_url?': self.num_false('main_element_present'),
            'How many urls have a robots.txt detected?': self.num_true('robots_txt_detected'),
            'How many urls return a 2xx server code for their robots.txt?': self.num_status_200('robots_txt_status_code'),
            'How many urls return a 3xx server code for their robots.txt?': self.num_status_300('robots_txt_status_code'),
            'How many urls return a 4xx server code for their robots.txt?': self.num_status_400('robots_txt_status_code'),
            'How many urls return a 5xx server code for their robots.txt?': self.num_status_500('robots_txt_status_code'),
            # 'How many urls have a LIVE robots.txt?': self.num_true('robots_txt_final_url_live'),
            # 'How many urls do not have a LIVE robots.txt?': self.num_false('robots_txt_final_url_live'),
            'How many urls\' robots.txt are text files?': self.robots_txt_is_txt(),
            'How many urls\' robots.txt are another file type?': self.robots_txt_is_not_txt(),
            # 'How many urls\' robots.txt redirect?': self.num_true('robots_txt_target_url_redirects'),
            'How many urls\' robots.txt file size were detected?': self.num_not_na('robots_txt_filesize'),
            'How many urls\' robots.txt have a crawl_delay?': self.num_not_na('robots_txt_crawl_delay'),
            'How many urls\' robots.txt link to sitemaps?': self.num_not_na('robots_txt_sitemap_locations'),
            'How many urls have a sitemap.xml detected?': self.num_true('sitemap_xml_detected'),
            'How many urls return a 2xx server code for their sitemap.xml?': self.num_status_200('sitemap_xml_status_code'),
            'How many urls return a 3xx server code for their sitemap.xml?': self.num_status_300('sitemap_xml_status_code'),
            'How many urls return a 4xx server code for their sitemap.xml?': self.num_status_400('sitemap_xml_status_code'),
            'How many urls return a 5xx server code for their sitemap.xml?': self.num_status_500('sitemap_xml_status_code'),
            # 'How many urls have a LIVE sitemap.xml?': self.num_true('sitemap_xml_final_url_live'),
            # 'How many urls do not have a LIVE sitemap.xml?': self.num_false('sitemap_xml_final_url_live'),
            # 'How many urls\' sitemap.xml redirect?': self.num_true('sitemap_xml_target_url_redirects'),
            'How many urls\' sitemap.xml file size were detected?': self.num_not_na('sitemap_xml_filesize'),
            'How many urls\' sitemap.xml are xml files?': self.sitemap_xml_is_xml(),
            'How many urls\' sitemap.xml are another file type?': self.sitemap_xml_is_xml(),
            'How many urls\' sitemap.xml have an item count?': self.num_not_na('sitemap_xml_count'),
            'How many urls\' sitemap.xml have a pdf count?': self.num_not_na('sitemap_xml_pdf_count'),
            'How many urls have an AAAA record (a.k.a. are likely IPv6 compliant)?': self.num_true('ipv6'),
            'How many urls do not have an AAAA record (a.k.a. are likely not IPv6 compliant)?': self.num_false('ipv6'),
            'How many urls have third party services?': self.num_not_na('third_party_service_domains'),
            'How many urls have 1-5 third party services?': self.num_between('third_party_service_count', 1, 5),
            'How many urls have 6-10 third party services?': self.num_between('third_party_service_count', 6, 10),
            'How many urls have 11-20 third party services?': self.num_between('third_party_service_count', 11, 20),
            'How many urls have over 20 third party services?': self.num_between('third_party_service_count', 20, 1000),
        }

    def num_records(self):
        return len(self.df.index)

    def num_true(self, field):
        return len(self.df.loc[self.df[field] == True])

    def num_false(self, field):
        return len(self.df.loc[self.df[field] == False])

    def num_completed(self, field):
        return len(self.df.loc[self.df[field] == 'completed'])

    def num_not_completed(self, field):
        return len(self.df.loc[self.df[field] != 'completed'])

    def num_status_200(self, field):
        return len(self.df.loc[self.df[field].between(200, 299)])

    def num_status_300(self, field):
        return len(self.df.loc[self.df[field].between(300, 399)])

    def num_status_400(self, field):
        return len(self.df.loc[self.df[field].between(400, 499)])

    def num_status_500(self, field):
        return len(self.df.loc[self.df[field].between(500, 599)])

    def num_na(self, field):
        return len(self.df.loc[self.df[field].isna()])

    def num_not_na(self, field):
        return len(self.df.loc[self.df[field].notna()])

    def num_unique(self, field):
        return len(pd.unique(self.df[field]))

    def num_between(self, field, low, high):
        return len(self.df.loc[self.df[field].between(low, high)])

    def branch(self, branch):
        return len(self.df.loc[self.df['branch'] == branch])

    def failed_connection_refused(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'connection_refused'])

    def failed_connection_reset(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'connection_reset'])

    def failed_dns_resolution(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'dns_resolution_error'])

    def failed_invalid_ssl(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'invalid_ssl_cert'])

    def failed_timeout(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'timeout'])

    def failed_unkown(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'unknown_error'])

    def failed_aborted(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'aborted'])

    def failed_address_unreachable(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'address_unreachable'])

    def failed_connection_closed(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'connection_closed'])

    def failed_empty_response(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'empty_response'])

    def failed_execution_context_destroyed(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'execution_context_destroyed'])

    def failed_http2_error(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'http2_error'])

    def failed_invalid_auth_credentials(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'invalid_auth_credentials'])

    def failed_invalid_response(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'invalid_response'])

    def failed_ssl_protocol_error(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'ssl_protocol_error'])

    def failed_ssl_version_cipher_mismatch(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'ssl_version_cipher_mismatch'])

    def failed_too_many_redirects(self):
        return len(self.df.loc[self.df['primary_scan_status'] == 'too_many_redirects'])

    def final_url_mimetype_html(self):
        return len(self.df.loc[self.df['media_type'] == 'text/html'])

    def final_url_mimetype_plain_text(self):
        return len(self.df.loc[self.df['media_type'].isin(['text/plain', 'plaintext'])])

    def final_url_mimetype_json(self):
        return len(self.df.loc[self.df['media_type'] == 'application/json'])

    def final_url_mimetype_xml(self):
        return len(self.df.loc[self.df['media_type'].isin(['application/xhtml', 'text/xml'])])

    def final_url_mimetype_other(self):
        return len(self.df.loc[~self.df['media_type'].isin(
            ['text/html', 'text/plain', 'application/json', 'application/xhtml', 'text/xml']
        )])

    def has_og_title_no_description(self):
        return len(self.df.loc[
            self.df['og_title'].notna() &
            self.df['og_description'].isna()
        ])

    def has_og_description_no_title(self):
        return len(self.df.loc[
            self.df['og_title'].isna() &
            self.df['og_description'].notna()
        ])

    def robots_txt_is_txt(self):
        return len(self.df.loc[self.df['robots_txt_media_type'].isin(['text/plain', 'plaintext'])])

    def robots_txt_is_not_txt(self):
        return len(self.df.loc[~self.df['robots_txt_media_type'].isin(['text/plain', 'plaintext'])])

    def sitemap_xml_is_xml(self):
        return len(self.df.loc[self.df['sitemap_xml_media_type'].isin(['application/xhtml', 'application/xml', 'text/xml'])])

    def sitemap_xml_is_not_xml(self):
        return len(self.df.loc[~self.df['sitemap_xml_media_type'].isin(['application/xhtml', 'application/xml', 'text/xml'])])
