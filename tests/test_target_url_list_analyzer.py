import pandas as pd
import unittest
import os
from analyzer.target_url_list_analyzer import TargetUrlListAnalyzer


class SnapshotAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.snapshot_analyzer = TargetUrlListAnalyzer(pd.read_csv(os.path.join(os.path.dirname(__file__), './test_target_url_list.csv')))

    def test_num_records(self):
        result = self.snapshot_analyzer.num_records()
        self.assertEqual(result, 1)

    def test_num_na(self):
        result = self.snapshot_analyzer.num_na('target_url')
        self.assertEqual(result, 0)

    def test_num_unique(self):
        result = self.snapshot_analyzer.num_unique('base_domain')
        self.assertEqual(result, 1)

    def test_num_true_has_results(self):
        result = self.snapshot_analyzer.num_true('source_list_federal_domains')
        self.assertEqual(result, 1)

    def test_num_true_has_no_results(self):
        result = self.snapshot_analyzer.num_true('source_list_dap')
        self.assertEqual(result, 0)
