# Backend Services

## app.market_data

Fetches public candle data from Binance and Bybit.

## app.market_service

Builds a normalized market snapshot with:

- latest price
- market score
- volatility
- volume ratio
- trend notes

## app.news_data

Reads RSS news feeds and extracts related assets.

## app.sentiment

Adds local sentiment labels and confidence scores to news headlines.

## app.risk

Calculates risk score and risk flags.

## app.advice_service

Combines market, sentiment, and risk into final advisory output.

## app.overview_service

Builds a ranked overview for all configured symbols.

## app.worker

Runs repeated overview checks from the command line.
