# CommodityTypeObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Commodity type name | 

## Example

```python
from tradewatch.models.commodity_type_obj import CommodityTypeObj

# TODO update the JSON string below
json = "{}"
# create an instance of CommodityTypeObj from a JSON string
commodity_type_obj_instance = CommodityTypeObj.from_json(json)
# print the JSON string representation of the object
print(CommodityTypeObj.to_json())

# convert the object into a dict
commodity_type_obj_dict = commodity_type_obj_instance.to_dict()
# create an instance of CommodityTypeObj from a dict
commodity_type_obj_from_dict = CommodityTypeObj.from_dict(commodity_type_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


