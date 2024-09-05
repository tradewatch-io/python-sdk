# ConversionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **int** |  | 
**rate** | **float** |  | 

## Example

```python
from tradewatch.models.conversion_info import ConversionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionInfo from a JSON string
conversion_info_instance = ConversionInfo.from_json(json)
# print the JSON string representation of the object
print(ConversionInfo.to_json())

# convert the object into a dict
conversion_info_dict = conversion_info_instance.to_dict()
# create an instance of ConversionInfo from a dict
conversion_info_from_dict = ConversionInfo.from_dict(conversion_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


