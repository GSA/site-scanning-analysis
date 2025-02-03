import pandas as pd
import unittest
import os
from report_generators.target_url_list import TargetUrlList


class TargetUrlListReportGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.target_url_list = TargetUrlList(pd.read_csv(os.path.join(os.path.dirname(__file__), './test_target_url_list.csv')))

    def test_num_records(self):
        result = self.target_url_list.num_records()
        self.assertEqual(result, 1)

    def test_num_na(self):
        result = self.target_url_list.num_na('initial_domain')
        self.assertEqual(result, 0)

    def test_num_unique(self):
        result = self.target_url_list.num_unique('base_domain')
        self.assertEqual(result, 1)

    def test_num_true_has_results(self):
        result = self.target_url_list.num_true('source_list_federal_domains')
        self.assertEqual(result, 1)

    def test_num_true_has_no_results(self):
        result = self.target_url_list.num_true('source_list_dap')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
