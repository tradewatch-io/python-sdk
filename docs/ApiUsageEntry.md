# ApiUsageEntry

Usage history entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **int** |  | 
**data** | [**ApiUsageDataTransfer**](ApiUsageDataTransfer.md) |  | 

## Example

```python
from tradewatch.models.api_usage_entry import ApiUsageEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsageEntry from a JSON string
api_usage_entry_instance = ApiUsageEntry.from_json(json)
# print the JSON string representation of the object
print(ApiUsageEntry.to_json())

# convert the object into a dict
api_usage_entry_dict = api_usage_entry_instance.to_dict()
# create an instance of ApiUsageEntry from a dict
api_usage_entry_from_dict = ApiUsageEntry.from_dict(api_usage_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


