# CryptoExchangeItem

A cryptocurrency exchange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Exchange identifier | 
**name** | **str** | Exchange name | 
**year_established** | **int** | Exchange established year | 

## Example

```python
from tradewatch.models.crypto_exchange_item import CryptoExchangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoExchangeItem from a JSON string
crypto_exchange_item_instance = CryptoExchangeItem.from_json(json)
# print the JSON string representation of the object
print(CryptoExchangeItem.to_json())

# convert the object into a dict
crypto_exchange_item_dict = crypto_exchange_item_instance.to_dict()
# create an instance of CryptoExchangeItem from a dict
crypto_exchange_item_from_dict = CryptoExchangeItem.from_dict(crypto_exchange_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


