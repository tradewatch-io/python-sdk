# CryptoConversionQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **str** |  | 
**amount** | **float** |  | [optional] [default to 10]
**precision** | **int** |  | [optional] [default to 8]

## Example

```python
from tradewatch.models.crypto_conversion_query import CryptoConversionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoConversionQuery from a JSON string
crypto_conversion_query_instance = CryptoConversionQuery.from_json(json)
# print the JSON string representation of the object
print(CryptoConversionQuery.to_json())

# convert the object into a dict
crypto_conversion_query_dict = crypto_conversion_query_instance.to_dict()
# create an instance of CryptoConversionQuery from a dict
crypto_conversion_query_from_dict = CryptoConversionQuery.from_dict(crypto_conversion_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


