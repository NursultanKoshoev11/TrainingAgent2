def check_market_quality(market):
    flags = []
    if market.get('candle_count', 0) < 50:
        flags.append('Limited candle history; market score confidence is reduced.')
    if market.get('latest_price') is None:
        flags.append('Latest price is missing.')
    if not market.get('notes'):
        flags.append('Market service returned no explanatory notes.')
    return flags


def check_news_quality(news):
    flags = []
    if not news:
        flags.append('No news items were collected for this symbol.')
    if news and all(item.get('sentiment_engine') == 'local' for item in news):
        flags.append('Sentiment is using local keyword scoring, not an external financial language model.')
    return flags


def build_quality_flags(market, news):
    return check_market_quality(market) + check_news_quality(news)
