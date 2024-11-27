# CryptoExchangesList

A list of cryptocurrency exchanges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CryptoExchangeItem]**](CryptoExchangeItem.md) |  | 

## Example

```python
from tradewatch.models.crypto_exchanges_list import CryptoExchangesList

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoExchangesList from a JSON string
crypto_exchanges_list_instance = CryptoExchangesList.from_json(json)
# print the JSON string representation of the object
print(CryptoExchangesList.to_json())

# convert the object into a dict
crypto_exchanges_list_dict = crypto_exchanges_list_instance.to_dict()
# create an instance of CryptoExchangesList from a dict
crypto_exchanges_list_from_dict = CryptoExchangesList.from_dict(crypto_exchanges_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


