def cryptofeed_available():
    try:
        import cryptofeed  # noqa: F401
        return True
    except ImportError:
        return False


def cryptofeed_status():
    return {
        'available': cryptofeed_available(),
        'status': 'ready_to_wire' if cryptofeed_available() else 'dependency_missing',
        'note': 'Install cryptofeed and connect callbacks to streaming.normalize_stream_event.',
    }


def planned_channels():
    return ['trades', 'book', 'ticker']
