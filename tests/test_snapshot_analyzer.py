import pandas as pd
import unittest
import os
from analyzer.snapshot_analyzer import SnapshotAnalyzer


class SnapshotAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.snapshot_analyzer = SnapshotAnalyzer(pd.read_csv(os.path.join(os.path.dirname(__file__), './test_snapshot.csv')))

    def test_num_true(self):
        result = self.snapshot_analyzer.num_true('final_url_live')
        self.assertEqual(result, 1)

    def test_num_false(self):
        result = self.snapshot_analyzer.num_false('final_url_live')
        self.assertEqual(result, 0)

    def test_num_completed(self):
        result = self.snapshot_analyzer.num_completed('not_found_scan_status')
        self.assertEqual(result, 1)

    def test_num_not_completed(self):
        result = self.snapshot_analyzer.num_not_completed('not_found_scan_status')
        self.assertEqual(result, 0)

    def test_num_status_200(self):
        result = self.snapshot_analyzer.num_status_200('final_url_status_code')
        self.assertEqual(result, 1)

    def test_num_status_300(self):
        result = self.snapshot_analyzer.num_status_300('final_url_status_code')
        self.assertEqual(result, 0)

    def test_num_status_400(self):
        result = self.snapshot_analyzer.num_status_400('robots_txt_final_url_status_code')
        self.assertEqual(result, 1)

    def test_num_status_500(self):
        result = self.snapshot_analyzer.num_status_500('final_url_status_code')
        self.assertEqual(result, 0)

    def test_num_na(self):
        result = self.snapshot_analyzer.num_na('robots_txt_sitemap_locations')
        self.assertEqual(result, 1)

    def test_num_not_na(self):
        result = self.snapshot_analyzer.num_not_na('robots_txt_final_url_mimetype')
        self.assertEqual(result, 1)

    def test_num_unique(self):
        result = self.snapshot_analyzer.num_unique('target_url')
        self.assertEqual(result, 1)

    def test_num_between(self):
        result = self.snapshot_analyzer.num_between('uswds_count', 0, 50)
        self.assertEqual(result, 1)

    def test_target_url_branch(self):
        result = self.snapshot_analyzer.target_url_branch('Executive')
        self.assertEqual(result, 1)

    def test_urls_scanned(self):
        result = self.snapshot_analyzer.urls_scanned()
        self.assertEqual(result, 1)

    def test_failed_connection_refused(self):
        result = self.snapshot_analyzer.failed_connection_refused()
        self.assertEqual(result, 0)

    def test_failed_connection_reset(self):
        result = self.snapshot_analyzer.failed_connection_reset()
        self.assertEqual(result, 0)

    def test_failed_dns_resolution(self):
        result = self.snapshot_analyzer.failed_dns_resolution()
        self.assertEqual(result, 0)

    def test_failed_invalid_ssl(self):
        result = self.snapshot_analyzer.failed_invalid_ssl()
        self.assertEqual(result, 0)

    def test_failed_timeout(self):
        result = self.snapshot_analyzer.failed_timeout()
        self.assertEqual(result, 1)

    def test_failed_unkown(self):
        result = self.snapshot_analyzer.failed_unkown()
        self.assertEqual(result, 0)

    def test_final_url_mimetype_html(self):
        result = self.snapshot_analyzer.final_url_mimetype_html()
        self.assertEqual(result, 1)

    def test_final_url_mimetype_plain_text(self):
        result = self.snapshot_analyzer.final_url_mimetype_plain_text()
        self.assertEqual(result, 0)

    def test_final_url_mimetype_json(self):
        result = self.snapshot_analyzer.final_url_mimetype_json()
        self.assertEqual(result, 0)

    def test_final_url_mimetype_xml(self):
        result = self.snapshot_analyzer.final_url_mimetype_xml()
        self.assertEqual(result, 0)

    def test_final_url_mimetype_other(self):
        result = self.snapshot_analyzer.final_url_mimetype_other()
        self.assertEqual(result, 0)

    def test_has_og_title_no_description(self):
        result = self.snapshot_analyzer.has_og_title_no_description()
        self.assertEqual(result, 0)

    def test_has_og_description_no_title(self):
        result = self.snapshot_analyzer.has_og_description_no_title()
        self.assertEqual(result, 0)

    def test_robots_txt_is_txt(self):
        result = self.snapshot_analyzer.robots_txt_is_txt()
        self.assertEqual(result, 0)

    def test_robots_txt_is_not_txt(self):
        result = self.snapshot_analyzer.robots_txt_is_not_txt()
        self.assertEqual(result, 1)

    def test_sitemap_xml_is_xml(self):
        result = self.snapshot_analyzer.sitemap_xml_is_xml()
        self.assertEqual(result, 0)

    def test_sitemap_xml_is_not_xml(self):
        result = self.snapshot_analyzer.sitemap_xml_is_not_xml()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
