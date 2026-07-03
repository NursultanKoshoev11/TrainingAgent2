import os
import urllib.parse


def gdelt_enabled():
    return os.getenv('GDELT_ENABLED', 'false').lower() == 'true'


def build_gdelt_query_url(query, max_records=20):
    params = urllib.parse.urlencode({
        'query': query,
        'mode': 'artlist',
        'format': 'json',
        'maxrecords': max_records,
    })
    return 'https://api.gdeltproject.org/api/v2/doc/doc?' + params


def gdelt_status():
    return {
        'enabled': gdelt_enabled(),
        'status': 'configured' if gdelt_enabled() else 'disabled',
        'note': 'GDELT adapter URL builder is ready. Fetching can be enabled after provider review.',
    }
