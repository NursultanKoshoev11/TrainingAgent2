from app.advisor_core import final_advice, score_market


def summarize_labels(rows):
    counts = {}
    for row in rows:
        label = row.get('label', 'unknown')
        counts[label] = counts.get(label, 0) + 1
    return counts


def run_signal_replay(candles, sentiment_score=50, risk_score=30, window=40):
    results = []
    for index in range(window, len(candles)):
        sample = candles[index - window:index]
        closes = [item['close'] for item in sample]
        volumes = [item['volume'] for item in sample]
        market = score_market(closes, volumes)
        advice = final_advice(market['score'], sentiment_score, risk_score)
        next_close = candles[index]['close'] if index < len(candles) else closes[-1]
        current_close = closes[-1]
        forward_return = 0 if current_close == 0 else round(((next_close - current_close) / current_close) * 100, 3)
        results.append({
            'index': index,
            'close': current_close,
            'next_close': next_close,
            'forward_return_percent': forward_return,
            'market_score': market['score'],
            'final_score': advice['final_score'],
            'label': advice['label'],
        })
    return results


def build_backtest_report(candles, sentiment_score=50, risk_score=30, window=40):
    rows = run_signal_replay(candles, sentiment_score=sentiment_score, risk_score=risk_score, window=window)
    if not rows:
        return {'count': 0, 'labels': {}, 'average_forward_return_percent': 0, 'rows': []}
    avg_return = round(sum(row['forward_return_percent'] for row in rows) / len(rows), 3)
    return {
        'count': len(rows),
        'labels': summarize_labels(rows),
        'average_forward_return_percent': avg_return,
        'rows': rows,
    }
