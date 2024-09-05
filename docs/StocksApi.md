# tradewatch.StocksApi

All URIs are relative to *https://api.tradewatch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCountries**](StocksApi.md#getCountries) | **GET** /stocks/countries | Available Countries
[**getQuote**](StocksApi.md#getQuote) | **GET** /stocks/symbols/{symbol} | Last Quote
[**getSymbols**](StocksApi.md#getSymbols) | **GET** /stocks/symbols | Available Symbols


# **getCountries**
> CountriesList getCountries()

Available Countries

Get list of available countries

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import tradewatch
from tradewatch.models.countries_list import CountriesList
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
    api_instance = tradewatch.StocksApi(api_client)

    try:
        # Available Countries
        api_response = api_instance.getCountries()
        print("The response of StocksApi->getCountries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StocksApi->getCountries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CountriesList**](CountriesList.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getQuote**
> LastQuote getQuote(symbol, precision=precision)

Last Quote

Get the last quote tick for the provided symbol.

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import tradewatch
from tradewatch.models.last_quote import LastQuote
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
    api_instance = tradewatch.StocksApi(api_client)
    symbol = 'symbol_example' # str | 
    precision = 5 # int |  (optional) (default to 5)

    try:
        # Last Quote
        api_response = api_instance.getQuote(symbol, precision=precision)
        print("The response of StocksApi->getQuote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StocksApi->getQuote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**|  | 
 **precision** | **int**|  | [optional] [default to 5]

### Return type

[**LastQuote**](LastQuote.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSymbols**
> CursorPageTCustomizedSymbolsOutFull getSymbols(mode, size=size, country=country, page=page, cursor=cursor)

Available Symbols

Get list of available symbols

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import tradewatch
from tradewatch.models.country import Country
from tradewatch.models.cursor_page_t_customized_symbols_out_full import CursorPageTCustomizedSymbolsOutFull
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
    api_instance = tradewatch.StocksApi(api_client)
    mode = tradewatch.SymbolsListMode() # SymbolsListMode | Listing mode
    size = 50 # int | Page offset (optional) (default to 50)
    country = tradewatch.Country() # Country |  (optional)
    page = 1 # int | Page number (optional) (default to 1)
    cursor = 'cursor_example' # str | Cursor for the next page (optional)

    try:
        # Available Symbols
        api_response = api_instance.getSymbols(mode, size=size, country=country, page=page, cursor=cursor)
        print("The response of StocksApi->getSymbols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StocksApi->getSymbols: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | [**SymbolsListMode**](.md)| Listing mode | 
 **size** | **int**| Page offset | [optional] [default to 50]
 **country** | [**Country**](.md)|  | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **cursor** | **str**| Cursor for the next page | [optional] 

### Return type

[**CursorPageTCustomizedSymbolsOutFull**](CursorPageTCustomizedSymbolsOutFull.md)

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

