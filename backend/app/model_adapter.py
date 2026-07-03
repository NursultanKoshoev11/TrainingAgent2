import json
import os
import urllib.request


def external_model_enabled():
    return bool(os.getenv('SENTIMENT_MODEL_URL'))


def score_with_external_model(text):
    url = os.getenv('SENTIMENT_MODEL_URL')
    if not url:
        return None
    payload = json.dumps({'text': text}).encode('utf-8')
    request = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode('utf-8'))
