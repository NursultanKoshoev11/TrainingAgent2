import json
import urllib.request

USER_AGENT = 'CryptoAIAdvisor/0.1'


def read_text(url, timeout_seconds=20):
    request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
        return response.read().decode('utf-8')


def read_json(url, timeout_seconds=20):
    return json.loads(read_text(url, timeout_seconds=timeout_seconds))
