# CommodityTypesList

A list of commodity types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CommodityTypeObj]**](CommodityTypeObj.md) |  | 

## Example

```python
from tradewatch.models.commodity_types_list import CommodityTypesList

# TODO update the JSON string below
json = "{}"
# create an instance of CommodityTypesList from a JSON string
commodity_types_list_instance = CommodityTypesList.from_json(json)
# print the JSON string representation of the object
print(CommodityTypesList.to_json())

# convert the object into a dict
commodity_types_list_dict = commodity_types_list_instance.to_dict()
# create an instance of CommodityTypesList from a dict
commodity_types_list_from_dict = CommodityTypesList.from_dict(commodity_types_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


