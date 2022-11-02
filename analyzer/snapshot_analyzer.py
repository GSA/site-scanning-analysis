import pandas as pd


class SnapshotAnalyzer:
    def __init__(self, df):
        self.df = df

    def analyze(self):
        return {
            'How many urls did we scan?': self.num_records(),
            'How many agency owners are represented?': self.num_unique('target_url_agency_owner'),
            'How many bureau owners are represented?': self.num_unique('target_url_bureau_owner'),
            'How many domains did we scan?': self.num_unique('target_url_domain'),
            'How many final urls are represented?': self.num_unique('final_url'),
            'How many final domains are represented?': self.num_unique('final_url_domain'),
            'How many urls are from the executive branch?': self.target_url_branch('Executive'),
            'How many urls are from the legislative branch?': self.target_url_branch('Legislative'),
            'How many urls are from the judicial branch?': self.target_url_branch('Judicial'),
            'How many home scans completed?': self.num_completed('primary_scan_status'),
            'How many home scans failed?': self.num_not_completed('primary_scan_status'),
            'How many home scans failed because of a refused connection?': self.failed_connection_refused(),
            'How many home scans failed because of a reset connection?': self.failed_connection_reset(),
            'How many home scans failed because of dns resolution?': self.failed_dns_resolution(),
            'How many home scans failed because of invalid ssl certs?': self.failed_invalid_ssl(),
            'How many home scans failed because of timeouts?': self.failed_timeout(),
            'How many home scans failed for unknown reasons?': self.failed_unkown(),
            'How many final urls are html files?': self.final_url_mimetype_html(),
            'How many final urls are text files?': self.final_url_mimetype_plain_text(),
            'How many final urls are json files?': self.final_url_mimetype_json(),
            'How many final urls are xml files?': self.final_url_mimetype_xml(),
            'How many final urls are another filetype?': self.final_url_mimetype_other(),
            'How many final urls are on the same domain as the target urls?': self.num_true('final_url_same_domain'),
            'How many final urls are on the same website as the target urls?': self.num_true('final_url_same_website'),
            'How many urls return a 2xx server code?': self.num_status_200('final_url_status_code'),
            'How many urls return a 3xx server code?': self.num_status_300('final_url_status_code'),
            'How many urls return a 4xx server code?': self.num_status_400('final_url_status_code'),
            'How many urls return a 5xx server code?': self.num_status_500('final_url_status_code'),
            'How many urls pass the 404 test?': self.num_true('target_url_404_test'),
            'How many urls fail the 404 test?': self.num_false('target_url_404_test'),
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
            'How many urls have dap detected?': self.num_true('dap_detected_final_url'),
            'How many urls don\'t have dap detected?': self.num_false('dap_detected_final_url'),
            'How many urls weren\'t scanned for DAP (failed scans)?': self.num_na('dap_detected_final_url'),
            'How many urls have an og_title?': self.num_not_na('og_title_final_url'),
            'How many urls have an og_description?': self.num_not_na('og_description_final_url'),
            'How many urls have an og_title but don\'t have an og_description?': self.has_og_title_no_description(),
            'How many urls have an og_description but don\'t have an og_title?': self.has_og_description_no_title(),
            'How many urls have an og_article_published?': self.num_not_na('og_article_published_final_url'),
            'How many urls have an og_article_modified?': self.num_not_na('og_article_modified_final_url'),
            'How many urls have a main_element_present?': self.num_true('main_element_present_final_url'),
            'How many urls don\'t have main_element_present_final_url?': self.num_false('main_element_present_final_url'),
            'How many urls have a robots.txt detected?': self.num_true('robots_txt_detected'),
            'How many urls return a 2xx server code for their robots.txt?': self.num_status_200('robots_txt_final_url_status_code'),
            'How many urls return a 3xx server code for their robots.txt?': self.num_status_300('robots_txt_final_url_status_code'),
            'How many urls return a 4xx server code for their robots.txt?': self.num_status_400('robots_txt_final_url_status_code'),
            'How many urls return a 5xx server code for their robots.txt?': self.num_status_500('robots_txt_final_url_status_code'),
            'How many urls have a LIVE robots.txt?': self.num_true('robots_txt_final_url_live'),
            'How many urls do not have a LIVE robots.txt?': self.num_false('robots_txt_final_url_live'),
            'How many urls\' robots.txt are text files?': self.robots_txt_is_txt(),
            'How many urls\' robots.txt are another file type?': self.robots_txt_is_not_txt(),
            'How many urls\' robots.txt redirect?': self.num_true('robots_txt_target_url_redirects'),
            'How many urls\' robots.txt file size were detected?': self.num_not_na('robots_txt_final_url_filesize_in_bytes'),
            'How many urls\' robots.txt have a crawl_delay?': self.num_not_na('robots_txt_crawl_delay'),
            'How many urls\' robots.txt link to sitemaps?': self.num_not_na('robots_txt_sitemap_locations'),
            'How many urls have a sitemap.xml detected?': self.num_true('sitemap_xml_detected'),
            'How many urls return a 2xx server code for their sitemap.xml?': self.num_status_200('sitemap_xml_final_url_status_code'),
            'How many urls return a 3xx server code for their sitemap.xml?': self.num_status_300('sitemap_xml_final_url_status_code'),
            'How many urls return a 4xx server code for their sitemap.xml?': self.num_status_400('sitemap_xml_final_url_status_code'),
            'How many urls return a 5xx server code for their sitemap.xml?': self.num_status_500('sitemap_xml_final_url_status_code'),
            'How many urls have a LIVE sitemap.xml?': self.num_true('sitemap_xml_final_url_live'),
            'How many urls do not have a LIVE sitemap.xml?': self.num_false('sitemap_xml_final_url_live'),
            'How many urls\' sitemap.xml redirect?': self.num_true('sitemap_xml_target_url_redirects'),
            'How many urls\' sitemap.xml file size were detected?': self.num_not_na('sitemap_xml_final_url_filesize_in_bytes'),
            'How many urls\' sitemap.xml are xml files?': self.sitemap_xml_is_xml(),
            'How many urls\' sitemap.xml are another file type?': self.sitemap_xml_is_xml(),
            'How many urls\' sitemap.xml have an item count?': self.num_not_na('sitemap_xml_count'),
            'How many urls\' sitemap.xml have a pdf count?': self.num_not_na('sitemap_xml_pdf_count'),
            'How many urls have an AAAA record (a.k.a. are likely IPv6 compliant)?': self.num_true('dns_ipv6'),
            'How many urls do not have an AAAA record (a.k.a. are likely not IPv6 compliant)?': self.num_false('dns_ipv6'),
            'How many urls have third party services?': self.num_na('third_party_service_domains'),
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

    def target_url_branch(self, branch):
        return len(self.df.loc[self.df['target_url_branch'] == branch])

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

    def final_url_mimetype_html(self):
        return len(self.df.loc[self.df['final_url_mimetype'] == 'text/html'])

    def final_url_mimetype_plain_text(self):
        return len(self.df.loc[self.df['final_url_mimetype'].isin(['text/plain', 'plaintext'])])

    def final_url_mimetype_json(self):
        return len(self.df.loc[self.df['final_url_mimetype'] == 'application/json'])

    def final_url_mimetype_xml(self):
        return len(self.df.loc[self.df['final_url_mimetype'].isin(['application/xhtml', 'text/xml'])])

    def final_url_mimetype_other(self):
        return len(self.df.loc[~self.df['final_url_mimetype'].isin(
            ['text/html', 'text/plain', 'application/json', 'application/xhtml', 'text/xml']
        )])

    def has_og_title_no_description(self):
        return len(self.df.loc[
            self.df['og_title_final_url'].notna() &
            self.df['og_description_final_url'].isna()
        ])

    def has_og_description_no_title(self):
        return len(self.df.loc[
            self.df['og_title_final_url'].isna() &
            self.df['og_description_final_url'].notna()
        ])

    def robots_txt_is_txt(self):
        return len(self.df.loc[self.df['robots_txt_final_url_mimetype'].isin(['text/plain', 'plaintext'])])

    def robots_txt_is_not_txt(self):
        return len(self.df.loc[~self.df['robots_txt_final_url_mimetype'].isin(['text/plain', 'plaintext'])])

    def sitemap_xml_is_xml(self):
        return len(self.df.loc[self.df['sitemap_xml_final_url_mimetype'].isin(['application/xhtml', 'text/xml'])])

    def sitemap_xml_is_not_xml(self):
        return len(self.df.loc[~self.df['sitemap_xml_final_url_mimetype'].isin(['application/xhtml', 'text/xml'])])
