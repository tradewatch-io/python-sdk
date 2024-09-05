# tradewatch.AccountApi

All URIs are relative to *https://api.tradewatch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUsage**](AccountApi.md#getUsage) | **GET** /account/usage | Usage statistics


# **getUsage**
> object getUsage(limit=limit, interval=interval)

Usage statistics

Get the usage statistics of your API account

### Example

* Api Key Authentication (api_key_query):
* Api Key Authentication (api_key_header):

```python
import tradewatch
from tradewatch.models.account_usage_statistics_interval import AccountUsageStatisticsInterval
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
    except Exception as e:
        print("Exception when calling AccountApi->getUsage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **interval** | [**AccountUsageStatisticsInterval**](.md)|  | [optional] 

### Return type

**object**

### Authorization

[api_key_query](../README.md#api_key_query), [api_key_header](../README.md#api_key_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

