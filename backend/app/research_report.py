def summarize_forward_returns(rows):
    if not rows:
        return {
            'signal_count': 0,
            'average_forward_return': 0,
            'positive_rate': 0,
        }
    returns = [row.get('forward_return', 0) for row in rows]
    positive = [value for value in returns if value > 0]
    return {
        'signal_count': len(rows),
        'average_forward_return': round(sum(returns) / len(returns), 4),
        'positive_rate': round(len(positive) / len(rows), 4),
    }


def build_research_report(name, rows):
    summary = summarize_forward_returns(rows)
    return {
        'report_name': name,
        'summary': summary,
        'rows': rows,
        'note': 'Research report only. It is not proof of future performance.'
    }
