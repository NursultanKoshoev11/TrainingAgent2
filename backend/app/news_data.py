import xml.etree.ElementTree as ET
import urllib.request

RSS_URLS = [
    'https://cointelegraph.com/rss',
    'https://www.coindesk.com/arc/outboundfeeds/rss/'
]

ASSETS = {
    'BTC': ['btc', 'bitcoin'],
    'ETH': ['eth', 'ethereum'],
    'SOL': ['sol', 'solana'],
    'BNB': ['bnb', 'binance'],
    'XRP': ['xrp', 'ripple']
}


def asset_from_symbol(symbol):
    return symbol.upper().replace('/', '').replace('USDT', '')


def related_assets(title):
    text = title.lower()
    result = []
    for asset, keys in ASSETS.items():
        if any(key in text for key in keys):
            result.append(asset)
    return result


def fetch_rss(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'TrainingAgent2/0.1'})
    with urllib.request.urlopen(request, timeout=20) as response:
        root = ET.fromstring(response.read())
    items = []
    for item in root.findall('.//item'):
        title = item.findtext('title') or 'Untitled'
        items.append({
            'title': title,
            'url': item.findtext('link'),
            'published_at': item.findtext('pubDate'),
            'related_assets': related_assets(title),
        })
    return items


def latest_news(symbol='BTC/USDT', limit=12):
    asset = asset_from_symbol(symbol)
    output = []
    for url in RSS_URLS:
        try:
            rows = fetch_rss(url)
        except Exception:
            continue
        for row in rows:
            if row['related_assets'] and asset not in row['related_assets']:
                continue
            output.append(row)
            if len(output) >= limit:
                return output
    return output[:limit]
