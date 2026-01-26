import pandas as pd
import unittest
import os
from report_generators.uswds import Uswds

class TargetUrlListReportGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.uswds = Uswds(pd.read_csv(os.path.join(os.path.dirname(__file__), './test_uswds_url_list.csv')))
        self.report = self.uswds.generate_report()

    def test_report_has_all_groups(self):
        """Verify all 20 expected groups are in the report"""
        expected_groups = [
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
        self.assertEqual(len(self.report), 20)
        self.assertEqual(list(self.report['Group']), expected_groups)

    def test_all_sites_scanned_count(self):
        """Verify 'All sites scanned' includes all rows"""
        all_sites = self.report[self.report['Group'] == 'All sites scanned'].iloc[0]
        self.assertEqual(all_sites['count'], 20)

    def test_live_sites_filtering(self):
        """Verify live filtering reduces count correctly"""
        all_sites = self.report[self.report['Group'] == 'All sites scanned'].iloc[0]['count']
        live_sites = self.report[self.report['Group'] == 'All live sites'].iloc[0]['count']
        self.assertLess(live_sites, all_sites)

    def test_filtered_sites_filtering(self):
        """Verify filter flag further reduces count"""
        live_sites = self.report[self.report['Group'] == 'All live sites'].iloc[0]['count']
        filtered_sites = self.report[self.report['Group'] == 'All live, filtered sites'].iloc[0]['count']
        self.assertLessEqual(filtered_sites, live_sites)

    def test_non_redirecting_sites_filtering(self):
        """Verify redirect exclusion further reduces count"""
        filtered_sites = self.report[self.report['Group'] == 'All live, filtered sites'].iloc[0]['count']
        non_redirecting = self.report[self.report['Group'] == 'All live, filtered, non-redirecting sites'].iloc[0]['count']
        self.assertLessEqual(non_redirecting, filtered_sites)

    def test_branch_filtering_executive(self):
        """Verify executive branch filtering works"""
        exec_scanned = self.report[self.report['Group'] == 'Executive sites scanned'].iloc[0]['count']
        self.assertGreater(exec_scanned, 0)
        self.assertLess(exec_scanned, 20)

    def test_branch_filtering_legislative(self):
        """Verify legislative branch filtering works"""
        leg_scanned = self.report[self.report['Group'] == 'Legislative sites scanned'].iloc[0]['count']
        self.assertGreater(leg_scanned, 0)
        self.assertLess(leg_scanned, 20)

    def test_branch_filtering_judicial(self):
        """Verify judicial branch filtering works"""
        jud_scanned = self.report[self.report['Group'] == 'Judicial sites scanned'].iloc[0]['count']
        self.assertGreater(jud_scanned, 0)
        self.assertLess(jud_scanned, 20)

    def test_idea_filtering(self):
        """Verify IDEA source list filtering works"""
        idea_scanned = self.report[self.report['Group'] == 'IDEA sites scanned'].iloc[0]['count']
        self.assertGreater(idea_scanned, 0)
        self.assertLess(idea_scanned, 20)

    def test_version_counts(self):
        """Verify semantic version counting works"""
        all_sites = self.report[self.report['Group'] == 'All sites scanned'].iloc[0]
        self.assertGreater(all_sites['semantic version'], 0)
        self.assertLessEqual(all_sites['semantic version'], all_sites['count'])

    def test_version_distribution(self):
        """Verify v1, v2, v3 versions are counted separately"""
        all_sites = self.report[self.report['Group'] == 'All sites scanned'].iloc[0]
        version_total = all_sites['v1.x'] + all_sites['v2.x'] + all_sites['v3.x']
        self.assertEqual(version_total, all_sites['semantic version'])

    def test_banner_count(self):
        """Verify banner flag is summed correctly"""
        all_sites = self.report[self.report['Group'] == 'All sites scanned'].iloc[0]
        self.assertGreaterEqual(all_sites['banner'], 0)
        self.assertLessEqual(all_sites['banner'], all_sites['count'])

    def test_usa_class_count(self):
        """Verify usa-class presence is counted"""
        all_sites = self.report[self.report['Group'] == 'All sites scanned'].iloc[0]
        self.assertGreaterEqual(all_sites['usa-class'], 0)
        self.assertLessEqual(all_sites['usa-class'], all_sites['count'])

    def test_report_columns(self):
        """Verify report has all expected columns"""
        expected_columns = ['Group', 'count', 'semantic version', 'v1.x', 'v2.x', 'v3.x', 'banner', 'usa-class']
        self.assertEqual(list(self.report.columns), expected_columns)

    def test_counts_are_non_negative(self):
        """Verify all counts are non-negative integers"""
        for col in ['count', 'semantic version', 'v1.x', 'v2.x', 'v3.x', 'banner', 'usa-class']:
            self.assertTrue((self.report[col] >= 0).all())

    def test_filtering_hierarchy(self):
        """Verify filtering creates proper subset hierarchy for each branch"""
        for branch in ['Executive', 'Legislative', 'Judicial']:
            scanned = self.report[self.report['Group'] == f'{branch} sites scanned'].iloc[0]['count']
            live = self.report[self.report['Group'] == f'{branch} live sites'].iloc[0]['count']
            filtered = self.report[self.report['Group'] == f'{branch} live, filtered sites'].iloc[0]['count']
            non_redir = self.report[self.report['Group'] == f'{branch} live, filtered, non-redirecting sites'].iloc[0]['count']

            self.assertLessEqual(live, scanned)
            self.assertLessEqual(filtered, live)
            self.assertLessEqual(non_redir, filtered)

if __name__ == '__main__':
    unittest.main()
