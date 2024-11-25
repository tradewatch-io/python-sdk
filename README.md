<a href="https://tradewatch.io/">
<img src="https://pub-e8bb70a6cc1844138d6a55fa4a44ba42.r2.dev/logo-purple.png" alt="TradeWatch.io logo" title="TradeWatch.io" align="right" height="60" />
</a>

# TradeWatch.io Python SDK

[TradeWatch.io](https://tradewatch.io) offers a comprehensive financial data API designed for developers and businesses. The platform provides real-time access to market data, covering a wide range of assets such as currencies, cryptocurrencies, stocks, indices, and commodities. It emphasizes seamless integration, reliability, and scalability, making it ideal for building financial tools and services. Additional features include serverless functions, customizable API domains, and webhook notifications for market events, all aimed at enhancing business efficiency and informed decision-making.

## Table of Contents
- [Quick start](#-quick-start)
- [Requirements](#-requirements)
- [Installation & usage](#-installation--usage)
- [Feedback and Contributions](#-feedback-and-contributions)
- [License](#-license)
- [Contact and Support](#-contact-and-support)

## 🚀 Quick start

Visit our [Dashboard](https://dash.tradewatch.io/register) and register a free account.

Follow the [Getting started](https://tradewatch.io/docs/platform/getting-started) section in our Developer Portal.

## 📝 Requirements

Python 3.8+

## 🔨 Installation & usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/tradewatch-io/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/tradewatch-io/python-sdk.git`)

Then import the package:
```python
import tradewatch
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tradewatch
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import tradewatch
from tradewatch.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tradewatch.io
# See configuration.py for a list of all supported configuration parameters.
configuration = tradewatch.Configuration(
    host = "https://api.tradewatch.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key_query
configuration.api_key['api_key_query'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_query'] = 'Bearer'

# Configure API key authorization: api_key_header
configuration.api_key['api_key_header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key_header'] = 'Bearer'


# Enter a context with an instance of the API client
with tradewatch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tradewatch.AccountApi(api_client)
    limit = 56 # int |  (optional)
    interval = tradewatch.AccountUsageStatisticsInterval() # AccountUsageStatisticsInterval |  (optional)

    try:
        # Usage statistics
        api_response = api_instance.getUsage(limit=limit, interval=interval)
        print("The response of AccountApi->getUsage:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->getUsage: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.tradewatch.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**getUsage**](docs/AccountApi.md#getusage) | **GET** /account/usage | Usage statistics
*CommoditiesApi* | [**getQuote**](docs/CommoditiesApi.md#getquote) | **GET** /commodities/symbols/{symbol} | Last Quote
*CommoditiesApi* | [**getSymbols**](docs/CommoditiesApi.md#getsymbols) | **GET** /commodities/symbols | Available Symbols
*CommoditiesApi* | [**getTypes**](docs/CommoditiesApi.md#gettypes) | **GET** /commodities/types | Available Types
*CryptoApi* | [**convert**](docs/CryptoApi.md#convert) | **GET** /crypto/convert/{from}/{to} | Conversion
*CryptoApi* | [**getQuote**](docs/CryptoApi.md#getquote) | **GET** /crypto/symbols/{symbol} | Last Quote
*CryptoApi* | [**getSymbols**](docs/CryptoApi.md#getsymbols) | **GET** /crypto/symbols | Available Symbols
*CurrenciesApi* | [**convert**](docs/CurrenciesApi.md#convert) | **GET** /currencies/convert/{from}/{to} | Conversion
*CurrenciesApi* | [**getQuote**](docs/CurrenciesApi.md#getquote) | **GET** /currencies/symbols/{symbol} | Last Quote
*CurrenciesApi* | [**getSymbols**](docs/CurrenciesApi.md#getsymbols) | **GET** /currencies/symbols | Available Symbols
*IndicesApi* | [**getQuote**](docs/IndicesApi.md#getquote) | **GET** /indices/symbols/{symbol} | Last Quote
*IndicesApi* | [**getSymbols**](docs/IndicesApi.md#getsymbols) | **GET** /indices/symbols | Available Symbols
*StocksApi* | [**getCountries**](docs/StocksApi.md#getcountries) | **GET** /stocks/countries | Available Countries
*StocksApi* | [**getQuote**](docs/StocksApi.md#getquote) | **GET** /stocks/symbols/{symbol} | Last Quote
*StocksApi* | [**getSymbols**](docs/StocksApi.md#getsymbols) | **GET** /stocks/symbols | Available Symbols


## Documentation For Models

 - [AccountUsageStatisticsInterval](docs/AccountUsageStatisticsInterval.md)
 - [ApiUsageDataTransfer](docs/ApiUsageDataTransfer.md)
 - [ApiUsageEntry](docs/ApiUsageEntry.md)
 - [CommodityType](docs/CommodityType.md)
 - [CommodityTypeObj](docs/CommodityTypeObj.md)
 - [CommodityTypesList](docs/CommodityTypesList.md)
 - [Conversion](docs/Conversion.md)
 - [ConversionInfo](docs/ConversionInfo.md)
 - [ConversionQuery](docs/ConversionQuery.md)
 - [CountriesList](docs/CountriesList.md)
 - [Country](docs/Country.md)
 - [CountryObj](docs/CountryObj.md)
 - [CryptoConversion](docs/CryptoConversion.md)
 - [CryptoConversionQuery](docs/CryptoConversionQuery.md)
 - [CursorPageTCustomizedSymbolsOutFull](docs/CursorPageTCustomizedSymbolsOutFull.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [ErrorResponseBody](docs/ErrorResponseBody.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LastQuote](docs/LastQuote.md)
 - [SymbolsListMode](docs/SymbolsListMode.md)
 - [SymbolsOutFull](docs/SymbolsOutFull.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="api_key_header"></a>
### api_key_header

- **Type**: API key
- **API key parameter name**: api-key
- **Location**: HTTP header

<a id="api_key_query"></a>
### api_key_query

- **Type**: API key
- **API key parameter name**: api-key
- **Location**: URL query string


## Author





## 🤝 Feedback and Contributions

We appreciate your support and look forward to making our product even better with your help!

## ©️ License

This project is licensed under the [MIT License](http://opensource.org/licenses/MIT).

## 🗨️ Contact and Support

For more details about our products, services, or any general information, feel free to reach out to us.

See the list of available [Support Channels](https://tradewatch.io/docs/support/channels).
