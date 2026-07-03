from app.cryptofeed_adapter import cryptofeed_status
from app.database import database_status
from app.provider_health import provider_health


def readiness_report():
    database = database_status()
    cryptofeed = cryptofeed_status()
    providers = provider_health()
    score = 90
    issues = []

    if database.get('mode') != 'postgresql':
        score -= 4
        issues.append('PostgreSQL is not enabled; SQLite fallback is active.')
    if not cryptofeed.get('available'):
        score -= 3
        issues.append('Cryptofeed dependency is not installed or not detected.')
    if not providers.get('news', {}).get('cryptopanic_enabled'):
        score -= 1
        issues.append('CryptoPanic is not enabled; RSS fallback is active.')
    if providers.get('context', {}).get('gdelt', {}).get('enabled') is not True:
        score -= 1
        issues.append('GDELT is not enabled.')
    if providers.get('context', {}).get('social_adapters', {}).get('status') == 'planned':
        score -= 1
        issues.append('Social adapters are still provider contracts.')

    return {
        'completion_estimate_percent': max(0, min(100, score)),
        'database': database,
        'cryptofeed': cryptofeed,
        'issues': issues,
        'note': '100% requires runtime validation with real dependencies, DATABASE_URL, and provider keys.',
    }
