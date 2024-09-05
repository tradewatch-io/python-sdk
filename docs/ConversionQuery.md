# ConversionQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**to** | **str** |  | 
**amount** | **float** |  | [optional] [default to 10]
**precision** | **int** |  | [optional] [default to 5]

## Example

```python
from tradewatch.models.conversion_query import ConversionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionQuery from a JSON string
conversion_query_instance = ConversionQuery.from_json(json)
# print the JSON string representation of the object
print(ConversionQuery.to_json())

# convert the object into a dict
conversion_query_dict = conversion_query_instance.to_dict()
# create an instance of ConversionQuery from a dict
conversion_query_from_dict = ConversionQuery.from_dict(conversion_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


