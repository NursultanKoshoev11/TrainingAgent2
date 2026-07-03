from app.diagnostics import diagnostics_report
from app.readiness import readiness_report
from app.provider_health import provider_health


def deep_health_report():
    diagnostics = diagnostics_report()
    readiness = readiness_report()
    providers = provider_health()
    status = 'ok' if diagnostics.get('required_ok') else 'degraded'
    return {
        'status': status,
        'diagnostics': diagnostics,
        'readiness': readiness,
        'providers': providers,
    }
