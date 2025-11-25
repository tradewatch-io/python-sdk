# TradeWatch.io Python SDK

![](https://tradewatch.io/)

<a href="https://tradewatch.io/">
  <img src="https://pub-e8bb70a6cc1844138d6a55fa4a44ba42.r2.dev/logo-purple.png" alt="TradeWatch.io logo" title="TradeWatch.io" align="right" height="60" />
</a>

Official SDK for the [TradeWatch.io API](https://tradewatch.io/docs/api-reference/introduction).

## Other SDKs
[![TypeScript SDK](https://img.shields.io/badge/TypeScript_SDK-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://github.com/tradewatch-io/typescript-sdk)
[![.NET SDK](https://img.shields.io/badge/.NET_SDK-512BD4?style=flat-square&logo=dotnet&logoColor=white)](https://github.com/tradewatch-io/dotnet-sdk)
[![PHP SDK](https://img.shields.io/badge/PHP_SDK-777BB4?style=flat-square&logo=php&logoColor=white)](https://github.com/tradewatch-io/php-sdk)
[![Java SDK](https://img.shields.io/badge/Java_SDK-ED8B00?style=flat-square&logo=openjdk&logoColor=white)](https://github.com/tradewatch-io/java-sdk)
[![Go SDK](https://img.shields.io/badge/Go_SDK-00ADD8?style=flat-square&logo=go&logoColor=white)](https://github.com/tradewatch-io/go-sdk)
[![Ruby SDK](https://img.shields.io/badge/Ruby_SDK-CC342D?style=flat-square&logo=ruby&logoColor=white)](https://github.com/tradewatch-io/ruby-sdk)
[![Swift SDK](https://img.shields.io/badge/Swift_SDK-FA7343?style=flat-square&logo=swift&logoColor=white)](https://github.com/tradewatch-io/swift-sdk)
[![Rust SDK](https://img.shields.io/badge/Rust_SDK-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/tradewatch-io/rust-sdk)
## What is TradeWatch.io?
TradeWatch.io is a market data platform and API for real-time and historical prices across crypto, stocks, indices, currencies, and commodities.

## Try the Interactive API Playground
Want to test endpoints without writing code first? Use the [TradeWatch Interactive API Playground](https://dash.tradewatch.io/api-explorer) to run requests directly in your browser.

[![TradeWatch Interactive API Playground](https://tradewatch.io/api-playground.png)](https://dash.tradewatch.io/api-explorer)

## Resources

- REST API reference: [https://tradewatch.io/docs/api-reference/introduction](https://tradewatch.io/docs/api-reference/introduction)
- WebSocket API reference: [https://tradewatch.io/docs/websocket-api/introduction](https://tradewatch.io/docs/websocket-api/introduction)
- Support channels: [https://tradewatch.io/docs/platform/support](https://tradewatch.io/docs/platform/support)

## Quick Start
1. Create an API key in the [TradeWatch Dashboard](https://dash.tradewatch.io/register).
2. Follow platform setup docs: [Getting started](https://tradewatch.io/docs/quickstart).

## Code examples

```python
from tradewatch import TradewatchApi

client = TradewatchApi(
    api_key="YOUR_API_KEY",
)
client.account.get_usage()
```

```python
import asyncio

from tradewatch import AsyncTradewatchApi

client = AsyncTradewatchApi(
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.account.get_usage()


asyncio.run(main())
```

```python
from tradewatch import TradewatchApi

client = TradewatchApi(
    api_key="YOUR_API_KEY",
)
client.commodities.get_quotes(
    symbols="symbols",
)
```

## Available Methods

### `account`

| Method | Required Params | Summary | Description |
| --- | --- | --- | --- |
| [`get_usage()`](https://tradewatch.io/docs/api-reference/account/usage-statistics) | - | Usage statistics | Get the usage statistics of your API account |

### `currencies`

| Method | Required Params | Summary | Description |
| --- | --- | --- | --- |
| [`convert(from_, to)`](https://tradewatch.io/docs/api-reference/currencies/conversion) | from_, to | Conversion | Convert one symbol to another |
| [`get_historical_ohlc(symbol, resolution, start, end)`](https://tradewatch.io/docs/api-reference/currencies/get-historical-ohlc) | symbol, resolution, start, end | Get Historical Ohlc | Get historical OHLC candles for a symbol in a selected resolution and time range. |
| [`get_historical_ticks(symbol, start, end)`](https://tradewatch.io/docs/api-reference/currencies/get-historical-ticks) | symbol, start, end | Get Historical Ticks | Get raw historical ticks for a symbol in a selected time range using cursor pagination. |
| [`get_insights()`](https://tradewatch.io/docs/api-reference/currencies/get-insights) | - | Get Insights | Get recent currencies insights. |
| [`get_quote(symbol)`](https://tradewatch.io/docs/api-reference/currencies/last-quote) | symbol | Last Quote | Get the last quote tick for the provided symbol. |
| [`get_quotes(symbols)`](https://tradewatch.io/docs/api-reference/currencies/last-quotes) | symbols | Last Quotes | Get the last quote tick for the provided symbols. |
| [`get_symbols()`](https://tradewatch.io/docs/api-reference/currencies/available-symbols) | - | Available Symbols | Get list of available symbols |

### `crypto`

| Method | Required Params | Summary | Description |
| --- | --- | --- | --- |
| [`convert(from_, to)`](https://tradewatch.io/docs/api-reference/crypto/conversion) | from_, to | Conversion | Convert one symbol to another |
| [`get_exchanges()`](https://tradewatch.io/docs/api-reference/crypto/available-exchanges) | - | Available Exchanges | Get list of available cryptocurrency exchanges |
| [`get_historical_ohlc(symbol, resolution, start, end)`](https://tradewatch.io/docs/api-reference/crypto/get-historical-ohlc) | symbol, resolution, start, end | Get Historical Ohlc | Get historical OHLC candles for a symbol in a selected resolution and time range. |
| [`get_historical_ticks(symbol, start, end)`](https://tradewatch.io/docs/api-reference/crypto/get-historical-ticks) | symbol, start, end | Get Historical Ticks | Get raw historical ticks for a symbol in a selected time range using cursor pagination. |
| [`get_insights()`](https://tradewatch.io/docs/api-reference/crypto/get-insights) | - | Get Insights | Get recent crypto insights. |
| [`get_quote(symbol)`](https://tradewatch.io/docs/api-reference/crypto/last-quote) | symbol | Last Quote | Get the last quote tick for the provided symbol. |
| [`get_quotes(symbols)`](https://tradewatch.io/docs/api-reference/crypto/last-quotes) | symbols | Last Quotes | Get the last quote tick for the provided symbols. |
| [`get_symbols()`](https://tradewatch.io/docs/api-reference/crypto/available-symbols) | - | Available Symbols | Get list of available symbols |

### `indices`

| Method | Required Params | Summary | Description |
| --- | --- | --- | --- |
| [`get_historical_ohlc(symbol, resolution, start, end)`](https://tradewatch.io/docs/api-reference/indices/get-historical-ohlc) | symbol, resolution, start, end | Get Historical Ohlc | Get historical OHLC candles for a symbol in a selected resolution and time range. |
| [`get_historical_ticks(symbol, start, end)`](https://tradewatch.io/docs/api-reference/indices/get-historical-ticks) | symbol, start, end | Get Historical Ticks | Get raw historical ticks for a symbol in a selected time range using cursor pagination. |
| [`get_insights()`](https://tradewatch.io/docs/api-reference/indices/get-insights) | - | Get Insights | Get recent indices insights. |
| [`get_quote(symbol)`](https://tradewatch.io/docs/api-reference/indices/last-quote) | symbol | Last Quote | Get the last quote tick for the provided symbol. |
| [`get_quotes(symbols)`](https://tradewatch.io/docs/api-reference/indices/last-quotes) | symbols | Last Quotes | Get the last quote tick for the provided symbols. |
| [`get_symbols()`](https://tradewatch.io/docs/api-reference/indices/available-symbols) | - | Available Symbols | Get list of available symbols |

### `stocks`

| Method | Required Params | Summary | Description |
| --- | --- | --- | --- |
| [`get_historical_ohlc(symbol, resolution, start, end)`](https://tradewatch.io/docs/api-reference/stocks/get-historical-ohlc) | symbol, resolution, start, end | Get Historical Ohlc | Get historical OHLC candles for a symbol in a selected resolution and time range. |
| [`get_historical_ticks(symbol, start, end)`](https://tradewatch.io/docs/api-reference/stocks/get-historical-ticks) | symbol, start, end | Get Historical Ticks | Get raw historical ticks for a symbol in a selected time range using cursor pagination. |
| [`get_insights()`](https://tradewatch.io/docs/api-reference/stocks/get-insights) | - | Get Insights | Get recent stocks insights. |
| [`get_market_holidays(start, end)`](https://tradewatch.io/docs/api-reference/stocks/get-market-holidays) | start, end | Get Market Holidays | Get market holidays. It takes half-days into account. |
| [`get_market_status()`](https://tradewatch.io/docs/api-reference/stocks/get-market-status) | - | Get Market Status | Get the current status (open or closed) of a market. It takes holidays and half-days into account but does not factor in circuit breakers or halts. |
| [`get_markets()`](https://tradewatch.io/docs/api-reference/stocks/get-markets) | - | Get Markets | Get details about the markets available in this API. |
| [`get_quote(symbol)`](https://tradewatch.io/docs/api-reference/stocks/last-quote) | symbol | Last Quote | Get the last quote tick for the provided symbol. |
| [`get_quotes(symbols)`](https://tradewatch.io/docs/api-reference/stocks/last-quotes) | symbols | Last Quotes | Get the last quote tick for the provided symbols. |
| [`get_stock_data(symbol)`](https://tradewatch.io/docs/api-reference/stocks/get-stock-data) | symbol | Get Stock Data | Get Stock Data |
| [`get_symbols()`](https://tradewatch.io/docs/api-reference/stocks/available-symbols) | - | Available Symbols | Get list of available symbols |
| [`get_trading_hours(start, end)`](https://tradewatch.io/docs/api-reference/stocks/get-trading-hours) | start, end | Get Trading Hours | Get trading hours. It takes half-days into account. |
| [`stock_get_countries()`](https://tradewatch.io/docs/api-reference/stocks/available-countries) | - | Available Countries | Get list of available countries |

### `commodities`

| Method | Required Params | Summary | Description |
| --- | --- | --- | --- |
| [`get_historical_ohlc(symbol, resolution, start, end)`](https://tradewatch.io/docs/api-reference/commodities/get-historical-ohlc) | symbol, resolution, start, end | Get Historical Ohlc | Get historical OHLC candles for a symbol in a selected resolution and time range. |
| [`get_historical_ticks(symbol, start, end)`](https://tradewatch.io/docs/api-reference/commodities/get-historical-ticks) | symbol, start, end | Get Historical Ticks | Get raw historical ticks for a symbol in a selected time range using cursor pagination. |
| [`get_insights()`](https://tradewatch.io/docs/api-reference/commodities/get-insights) | - | Get Insights | Get recent commodities insights. |
| [`get_quote(symbol)`](https://tradewatch.io/docs/api-reference/commodities/last-quote) | symbol | Last Quote | Get the last quote tick for the provided symbol. |
| [`get_quotes(symbols)`](https://tradewatch.io/docs/api-reference/commodities/last-quotes) | symbols | Last Quotes | Get the last quote tick for the provided symbols. |
| [`get_symbols()`](https://tradewatch.io/docs/api-reference/commodities/available-symbols) | - | Available Symbols | Get list of available symbols |
| [`get_types()`](https://tradewatch.io/docs/api-reference/commodities/available-types) | - | Available Types | Get list of available commodity types |
