def advisory_rules(advice):
    rules = []
    if advice.get('risk_score', 0) >= 70:
        rules.append({'rule': 'risk_block', 'passed': False, 'message': 'Risk score is too high for a positive advisory setup.'})
    else:
        rules.append({'rule': 'risk_block', 'passed': True, 'message': 'Risk score is below the hard block threshold.'})

    if advice.get('confidence', 0) < 30:
        rules.append({'rule': 'confidence_check', 'passed': False, 'message': 'Confidence is low; recommendation should be treated as weak.'})
    else:
        rules.append({'rule': 'confidence_check', 'passed': True, 'message': 'Confidence is acceptable for advisory display.'})

    if advice.get('quality_flags'):
        rules.append({'rule': 'data_quality', 'passed': False, 'message': 'Quality flags exist; review supporting data before acting.'})
    else:
        rules.append({'rule': 'data_quality', 'passed': True, 'message': 'No quality flags were detected.'})

    return rules
