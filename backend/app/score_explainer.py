def explain_advice(advice):
    explanations = []
    explanations.append('Recommendation: ' + str(advice.get('recommendation')))
    explanations.append('Final score: ' + str(advice.get('final_score')))
    explanations.append('Market score: ' + str(advice.get('market_score')))
    explanations.append('Sentiment score: ' + str(advice.get('sentiment_score')))
    explanations.append('Risk score: ' + str(advice.get('risk_score')))
    for flag in advice.get('risk_flags', []):
        explanations.append('Risk flag: ' + flag)
    for flag in advice.get('quality_flags', []):
        explanations.append('Quality flag: ' + flag)
    return explanations
