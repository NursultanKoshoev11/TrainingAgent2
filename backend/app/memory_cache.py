import time

_CACHE = {}


def cache_get(key):
    item = _CACHE.get(key)
    if not item:
        return None
    expires_at, value = item
    if expires_at < time.time():
        _CACHE.pop(key, None)
        return None
    return value


def cache_set(key, value, ttl_seconds=60):
    _CACHE[key] = (time.time() + ttl_seconds, value)
    return value


def cache_status():
    return {'items': len(_CACHE)}
