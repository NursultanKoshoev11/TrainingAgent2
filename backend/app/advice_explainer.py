from app.score_explainer import explain_advice
from app.strategy_rules import advisory_rules


def explain_full_advice(advice):
    return {
        'symbol': advice.get('symbol'),
        'recommendation': advice.get('recommendation'),
        'explanation_lines': explain_advice(advice),
        'rules': advisory_rules(advice),
    }
