from datetime import datetime, timezone

from app.overview_service import build_overview


def build_text_report(exchange='binance', timeframe='1h'):
    overview = build_overview(exchange=exchange, timeframe=timeframe)
    lines = []
    lines.append('Crypto AI Advisor Report')
    lines.append('Generated at: ' + datetime.now(timezone.utc).isoformat())
    lines.append('Exchange: ' + overview.get('exchange', exchange))
    lines.append('Timeframe: ' + overview.get('timeframe', timeframe))
    lines.append('Portfolio bias: ' + overview.get('portfolio', {}).get('portfolio_bias', 'unknown'))
    lines.append('')
    for item in overview.get('items', []):
        if 'recommendation' not in item:
            lines.append(f"{item.get('symbol')}: error - {item.get('service_error')}")
            continue
        lines.append(
            f"{item.get('symbol')}: {item.get('recommendation')} | final={item.get('final_score')} | risk={item.get('risk_score')} | confidence={item.get('confidence')}"
        )
    lines.append('')
    lines.append('This report is advisory-only and is not financial advice.')
    return '\n'.join(lines)


def build_json_report(exchange='binance', timeframe='1h'):
    return {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'overview': build_overview(exchange=exchange, timeframe=timeframe),
        'disclaimer': 'Advisory-only analytics. This is not financial advice.',
    }
