# Conversion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ConversionInfo**](ConversionInfo.md) |  | 
**query** | [**ConversionQuery**](ConversionQuery.md) |  | 
**result** | **float** |  | 

## Example

```python
from tradewatch.models.conversion import Conversion

# TODO update the JSON string below
json = "{}"
# create an instance of Conversion from a JSON string
conversion_instance = Conversion.from_json(json)
# print the JSON string representation of the object
print(Conversion.to_json())

# convert the object into a dict
conversion_dict = conversion_instance.to_dict()
# create an instance of Conversion from a dict
conversion_from_dict = Conversion.from_dict(conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


