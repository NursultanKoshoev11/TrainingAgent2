ALERT_LEVELS = {
    'STRONG_POSITIVE_SETUP': 'watch',
    'POSITIVE_SETUP': 'watch',
    'WAIT': 'info',
    'NEGATIVE_SETUP': 'risk',
    'HIGH_RISK_AVOID': 'critical',
}


def build_alert(advice):
    label = advice.get('recommendation', 'WAIT')
    risk_score = advice.get('risk_score', 0)
    level = ALERT_LEVELS.get(label, 'info')
    if risk_score >= 75:
        level = 'critical'
    return {
        'symbol': advice.get('symbol'),
        'level': level,
        'recommendation': label,
        'final_score': advice.get('final_score'),
        'risk_score': risk_score,
        'message': f"{advice.get('symbol')} {label}: final score {advice.get('final_score')}, risk {risk_score}",
    }


def build_alerts(items):
    return [build_alert(item) for item in items if 'recommendation' in item]
