from fastapi import APIRouter

from app.advisor_core import final_advice, score_market

router = APIRouter()


@router.get('/ping')
def ping():
    return {'ok': True, 'mode': 'advisory-only'}


@router.get('/api/demo-advice')
def demo_advice():
    closes = [100, 101, 101.5, 102, 103, 104, 103.5, 105, 106, 107, 108, 108.5, 109, 110, 111, 112, 113, 112.5, 114, 115, 116, 117, 118, 119, 120, 121]
    volumes = [10, 11, 12, 13, 12, 14, 15, 15, 16, 17, 20, 19, 18, 21, 22, 23, 22, 24, 25, 26, 27, 28, 30, 31, 33, 35]
    market = score_market(closes, volumes)
    risk_score = 28
    sentiment_score = 58
    advice = final_advice(market['score'], sentiment_score, risk_score)
    return {
        'symbol': 'BTC/USDT',
        'recommendation': advice['label'],
        'final_score': advice['final_score'],
        'market_score': market['score'],
        'sentiment_score': sentiment_score,
        'risk_score': risk_score,
        'market': market,
        'disclaimer': 'Advisory-only analytics. This is not financial advice.'
    }
