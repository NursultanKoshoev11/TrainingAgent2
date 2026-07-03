from app.advisor_core import final_advice
from app.data_quality import build_quality_flags
from app.event_risk import detect_event_risk
from app.liquidity import estimate_liquidity
from app.macro import neutral_macro_context
from app.market_service import build_market_snapshot
from app.news_data import latest_news
from app.risk import calculate_risk
from app.sentiment import aggregate, enrich_news
from app.social import neutral_social_context


def build_advice(symbol='BTC/USDT', exchange='binance', timeframe='1h', news_limit=12):
    market = build_market_snapshot(symbol=symbol, exchange=exchange, timeframe=timeframe)
    news = enrich_news(latest_news(symbol=symbol, limit=news_limit))
    sentiment_score = aggregate(news)
    liquidity = estimate_liquidity(market)
    event_risk = detect_event_risk(news)
    macro = neutral_macro_context()
    social = neutral_social_context()
    risk = calculate_risk(market, news)
    combined_risk = min(100, risk['risk_score'] + event_risk['event_risk_score'] * 0.25 + max(0, 50 - liquidity['liquidity_score']) * 0.2)
    adjusted_sentiment = round((sentiment_score * 0.75) + (social['social_score'] * 0.15) + (macro['macro_score'] * 0.10), 2)
    advice = final_advice(market['score'], adjusted_sentiment, combined_risk)
    quality_flags = build_quality_flags(market, news)
    context_flags = macro['macro_flags'] + social['social_flags']
    confidence = round(min(95, max(5, abs(advice['final_score'] - 50) + (100 - combined_risk) * 0.35 - len(quality_flags) * 3 - len(context_flags) * 2)), 2)
    return {
        'exchange': exchange,
        'symbol': symbol,
        'timeframe': timeframe,
        'recommendation': advice['label'],
        'confidence': confidence,
        'final_score': advice['final_score'],
        'market_score': market['score'],
        'sentiment_score': adjusted_sentiment,
        'news_sentiment_score': sentiment_score,
        'macro_score': macro['macro_score'],
        'social_score': social['social_score'],
        'risk_score': round(combined_risk, 2),
        'base_risk_score': risk['risk_score'],
        'liquidity_score': liquidity['liquidity_score'],
        'event_risk_score': event_risk['event_risk_score'],
        'risk_flags': risk['risk_flags'] + liquidity['liquidity_flags'],
        'event_risk_flags': event_risk['event_risk_flags'],
        'quality_flags': quality_flags,
        'context_flags': context_flags,
        'summary': f"{advice['label']}: market score {market['score']}, sentiment score {adjusted_sentiment}, risk score {round(combined_risk, 2)}.",
        'market': market,
        'news': news,
        'macro': macro,
        'social': social,
        'disclaimer': 'Advisory-only analytics. This is not financial advice.'
    }
