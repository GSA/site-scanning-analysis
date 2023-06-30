import pandas as pd
import unittest
import os
from idea.idea_report_generator import IdeaReportGenerator


class IdeaReportGeneratorTest(unittest.TestCase):
    def setUp(self):
        idea_report_generator = IdeaReportGenerator(pd.read_csv(os.path.join(os.path.dirname(__file__), './test_idea_report.csv')))
        self.result = idea_report_generator.report()

    def test_idea_report(self):
        self.assertEqual(len(self.result), 2)
        self.assertEqual((self.result['Number of Websites with DAP'] == 1).sum(), 2)
        self.assertEqual((self.result['Number of Websites with USWDS Font'] == 1).sum(), 2)

if __name__ == '__main__':
    unittest.main()
