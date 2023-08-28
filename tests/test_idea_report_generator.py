import pandas as pd
import unittest
import os
from report_generators.idea import Idea


class IdeaReportGeneratorTest(unittest.TestCase):
    def setUp(self):
        idea = Idea(pd.read_csv(os.path.join(os.path.dirname(__file__), './test_idea_report.csv')))
        self.result = idea.generate_report()

    def test_idea_report(self):
        self.assertEqual(len(self.result), 3)
        self.assertEqual((self.result['Number of Websites with DAP'] == 1).sum(), 2)
        self.assertEqual((self.result['Number of Websites with USWDS Semantic Version'] == 1).sum(), 2)

if __name__ == '__main__':
    unittest.main()
