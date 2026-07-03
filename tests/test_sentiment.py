import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'backend'))

from app.sentiment import aggregate, enrich_news, local_score_text


class SentimentTests(unittest.TestCase):
    def test_local_score_shape(self):
        result = local_score_text('Bitcoin rally and institutional inflow')
        self.assertIn(result['label'], ['positive', 'neutral', 'negative'])
        self.assertGreaterEqual(result['score'], 0)
        self.assertLessEqual(result['score'], 100)

    def test_enrich_news(self):
        items = enrich_news([{'title': 'Ethereum upgrade launch'}])
        self.assertEqual(len(items), 1)
        self.assertIn('sentiment_score', items[0])

    def test_aggregate_empty(self):
        self.assertEqual(aggregate([]), 50)


if __name__ == '__main__':
    unittest.main()
