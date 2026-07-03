from app.advisor_core import final_advice
from app.data_quality import build_quality_flags
from app.market_service import build_market_snapshot
from app.news_data import latest_news
from app.risk import calculate_risk
from app.sentiment import aggregate, enrich_news


def build_advice(symbol='BTC/USDT', exchange='binance', timeframe='1h', news_limit=12):
    market = build_market_snapshot(symbol=symbol, exchange=exchange, timeframe=timeframe)
    news = enrich_news(latest_news(symbol=symbol, limit=news_limit))
    sentiment_score = aggregate(news)
    risk = calculate_risk(market, news)
    advice = final_advice(market['score'], sentiment_score, risk['risk_score'])
    quality_flags = build_quality_flags(market, news)
    confidence = round(min(95, max(5, abs(advice['final_score'] - 50) + (100 - risk['risk_score']) * 0.35 - len(quality_flags) * 3)), 2)
    return {
        'exchange': exchange,
        'symbol': symbol,
        'timeframe': timeframe,
        'recommendation': advice['label'],
        'confidence': confidence,
        'final_score': advice['final_score'],
        'market_score': market['score'],
        'sentiment_score': sentiment_score,
        'risk_score': risk['risk_score'],
        'risk_flags': risk['risk_flags'],
        'quality_flags': quality_flags,
        'summary': f"{advice['label']}: market score {market['score']}, sentiment score {sentiment_score}, risk score {risk['risk_score']}.",
        'market': market,
        'news': news,
        'disclaimer': 'Advisory-only analytics. This is not financial advice.'
    }
