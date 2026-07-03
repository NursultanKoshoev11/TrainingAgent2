import xml.etree.ElementTree as ET

from app.net_client import read_text


def fetch_public_rss(url, source='rss', limit=20):
    text = read_text(url)
    root = ET.fromstring(text)
    items = []
    for item in root.findall('.//item')[:limit]:
        items.append({
            'source': source,
            'title': item.findtext('title') or 'Untitled',
            'url': item.findtext('link'),
            'published_at': item.findtext('pubDate'),
            'type': 'rss_item',
        })
    return items
