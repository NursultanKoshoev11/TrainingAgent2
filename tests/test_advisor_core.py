import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend'))

from app.advisor_core import final_advice, percent_change, score_market, volatility


class AdvisorCoreTests(unittest.TestCase):
    def test_percent_change(self):
        self.assertEqual(percent_change(100, 110), 10)
        self.assertEqual(percent_change(0, 110), 0)

    def test_volatility_returns_number(self):
        self.assertGreaterEqual(volatility([100, 101, 99, 102]), 0)

    def test_score_market_range(self):
        closes = [100 + index for index in range(40)]
        volumes = [10 + index for index in range(40)]
        result = score_market(closes, volumes)
        self.assertGreaterEqual(result['score'], 0)
        self.assertLessEqual(result['score'], 100)

    def test_final_advice_range(self):
        result = final_advice(70, 60, 30)
        self.assertIn('label', result)
        self.assertGreaterEqual(result['final_score'], 0)
        self.assertLessEqual(result['final_score'], 100)


if __name__ == '__main__':
    unittest.main()
