# CryptoConversion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ConversionInfo**](ConversionInfo.md) |  | 
**query** | [**CryptoConversionQuery**](CryptoConversionQuery.md) |  | 
**result** | **float** |  | 

## Example

```python
from tradewatch.models.crypto_conversion import CryptoConversion

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoConversion from a JSON string
crypto_conversion_instance = CryptoConversion.from_json(json)
# print the JSON string representation of the object
print(CryptoConversion.to_json())

# convert the object into a dict
crypto_conversion_dict = crypto_conversion_instance.to_dict()
# create an instance of CryptoConversion from a dict
crypto_conversion_from_dict = CryptoConversion.from_dict(crypto_conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


