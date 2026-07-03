from app.forced_flow import neutral_forced_flow_context
from app.funding import neutral_funding_context
from app.open_interest import neutral_open_interest_context


def combined_derivatives_context():
    funding = neutral_funding_context()
    open_interest = neutral_open_interest_context()
    forced_flow = neutral_forced_flow_context()
    flags = []
    flags.extend(funding.get('funding_flags', []))
    flags.extend(open_interest.get('open_interest_flags', []))
    flags.extend(forced_flow.get('forced_flow_flags', []))
    score = round((funding['funding_score'] + open_interest['open_interest_score'] + forced_flow['forced_flow_score']) / 3, 2)
    return {
        'derivatives_score': score,
        'derivatives_flags': flags,
        'funding': funding,
        'open_interest': open_interest,
        'forced_flow': forced_flow,
    }
