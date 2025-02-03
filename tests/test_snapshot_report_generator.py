import pandas as pd
import unittest
import os
from report_generators.snapshot import Snapshot


class SnapshotReportGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.snapshot = Snapshot(pd.read_csv(os.path.join(os.path.dirname(__file__), './test_snapshot.csv')))

    def test_num_records(self):
        result = self.snapshot.num_records()
        self.assertEqual(result, 1)

    def test_num_true(self):
        result = self.snapshot.num_true('live')
        self.assertEqual(result, 1)

    def test_num_false(self):
        result = self.snapshot.num_false('live')
        self.assertEqual(result, 0)

    def test_num_completed(self):
        result = self.snapshot.num_completed('not_found_scan_status')
        self.assertEqual(result, 1)

    def test_num_not_completed(self):
        result = self.snapshot.num_not_completed('not_found_scan_status')
        self.assertEqual(result, 0)

    def test_num_status_200(self):
        result = self.snapshot.num_status_200('status_code')
        self.assertEqual(result, 1)

    def test_num_status_300(self):
        result = self.snapshot.num_status_300('status_code')
        self.assertEqual(result, 0)

    def test_num_status_400(self):
        result = self.snapshot.num_status_400('robots_txt_status_code')
        self.assertEqual(result, 1)

    def test_num_status_500(self):
        result = self.snapshot.num_status_500('status_code')
        self.assertEqual(result, 0)

    def test_num_na(self):
        result = self.snapshot.num_na('robots_txt_sitemap_locations')
        self.assertEqual(result, 1)

    def test_num_not_na(self):
        result = self.snapshot.num_not_na('robots_txt_media_type')
        self.assertEqual(result, 1)

    def test_num_unique(self):
        result = self.snapshot.num_unique('initial_domain')
        self.assertEqual(result, 1)

    def test_num_between(self):
        result = self.snapshot.num_between('uswds_count', 0, 50)
        self.assertEqual(result, 1)

    def test_target_url_branch(self):
        result = self.snapshot.branch('Executive')
        self.assertEqual(result, 1)

    def test_failed_connection_refused(self):
        result = self.snapshot.failed_connection_refused()
        self.assertEqual(result, 0)

    def test_failed_connection_reset(self):
        result = self.snapshot.failed_connection_reset()
        self.assertEqual(result, 0)

    def test_failed_dns_resolution(self):
        result = self.snapshot.failed_dns_resolution()
        self.assertEqual(result, 0)

    def test_failed_invalid_ssl(self):
        result = self.snapshot.failed_invalid_ssl()
        self.assertEqual(result, 0)

    def test_failed_timeout(self):
        result = self.snapshot.failed_timeout()
        self.assertEqual(result, 0)

    def test_failed_unkown(self):
        result = self.snapshot.failed_unkown()
        self.assertEqual(result, 0)

    def test_final_url_mimetype_html(self):
        result = self.snapshot.final_url_mimetype_html()
        self.assertEqual(result, 1)

    def test_final_url_mimetype_plain_text(self):
        result = self.snapshot.final_url_mimetype_plain_text()
        self.assertEqual(result, 0)

    def test_final_url_mimetype_json(self):
        result = self.snapshot.final_url_mimetype_json()
        self.assertEqual(result, 0)

    def test_final_url_mimetype_xml(self):
        result = self.snapshot.final_url_mimetype_xml()
        self.assertEqual(result, 0)

    def test_final_url_mimetype_other(self):
        result = self.snapshot.final_url_mimetype_other()
        self.assertEqual(result, 0)

    def test_has_og_title_no_description(self):
        result = self.snapshot.has_og_title_no_description()
        self.assertEqual(result, 0)

    def test_has_og_description_no_title(self):
        result = self.snapshot.has_og_description_no_title()
        self.assertEqual(result, 0)

    def test_robots_txt_is_txt(self):
        result = self.snapshot.robots_txt_is_txt()
        self.assertEqual(result, 1)

    def test_robots_txt_is_not_txt(self):
        result = self.snapshot.robots_txt_is_not_txt()
        self.assertEqual(result, 0)

    def test_sitemap_xml_is_xml(self):
        result = self.snapshot.sitemap_xml_is_xml()
        self.assertEqual(result, 1)

    def test_sitemap_xml_is_not_xml(self):
        result = self.snapshot.sitemap_xml_is_not_xml()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
