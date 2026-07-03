import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend'))

from app.risk import calculate_risk


class RiskTests(unittest.TestCase):
    def test_empty_news_adds_flag(self):
        market = {'volatility_percent': 1, 'volume_ratio': 1}
        result = calculate_risk(market, [])
        self.assertIn('risk_score', result)
        self.assertTrue(result['risk_flags'])

    def test_high_volatility_increases_risk(self):
        low = calculate_risk({'volatility_percent': 1, 'volume_ratio': 1}, [])
        high = calculate_risk({'volatility_percent': 5, 'volume_ratio': 1}, [])
        self.assertGreater(high['risk_score'], low['risk_score'])


if __name__ == '__main__':
    unittest.main()
