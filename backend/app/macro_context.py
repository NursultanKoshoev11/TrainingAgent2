MACRO_FLAGS = [
    'major rate decision window',
    'high inflation print window',
    'major regulatory announcement window',
    'large exchange outage window'
]


def macro_context_status():
    return {
        'status': 'manual_or_external_source_required',
        'planned_inputs': MACRO_FLAGS,
        'current_macro_risk_score': 0,
        'current_macro_flags': [],
    }
