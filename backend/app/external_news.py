import json
import os
import urllib.parse
import urllib.request


def cryptopanic_enabled():
    return bool(os.getenv('CRYPTOPANIC_API_KEY'))


def fetch_cryptopanic(symbol='BTC/USDT', limit=12):
    key = os.getenv('CRYPTOPANIC_API_KEY')
    if not key:
        return []
    asset = symbol.upper().replace('/', '').replace('USDT', '')
    query = urllib.parse.urlencode({'auth_token': key, 'currencies': asset, 'public': 'true'})
    request = urllib.request.Request('https://cryptopanic.com/api/v1/posts/?' + query, headers={'User-Agent': 'TrainingAgent2/0.1'})
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode('utf-8'))
    items = []
    for row in payload.get('results', [])[:limit]:
        source = row.get('source') or {}
        items.append({
            'title': row.get('title') or 'Untitled',
            'url': row.get('url'),
            'published_at': row.get('published_at'),
            'source': source.get('title'),
            'related_assets': [asset],
        })
    return items
