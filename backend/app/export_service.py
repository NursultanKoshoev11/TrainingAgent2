import json


def signals_as_json(signals):
    return json.dumps(signals, indent=2)


def signals_as_lines(signals):
    rows = []
    for item in signals:
        rows.append(
            f"{item.get('id')} | {item.get('created_at')} | {item.get('symbol')} | {item.get('recommendation')} | final={item.get('final_score')} | risk={item.get('risk_score')}"
        )
    return '\n'.join(rows)
