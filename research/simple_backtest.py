from app.advisor_core import final_advice, score_market


def run_window_backtest(candles, sentiment_score=50, risk_score=30, window=40):
    results = []
    for index in range(window, len(candles)):
        sample = candles[index - window:index]
        closes = [item['close'] for item in sample]
        volumes = [item['volume'] for item in sample]
        market = score_market(closes, volumes)
        advice = final_advice(market['score'], sentiment_score, risk_score)
        results.append({
            'index': index,
            'close': closes[-1],
            'market_score': market['score'],
            'final_score': advice['final_score'],
            'label': advice['label'],
        })
    return results
