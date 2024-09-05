# ApiUsageDataTransfer

Data transfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **int** |  | 
**response** | **int** |  | 

## Example

```python
from tradewatch.models.api_usage_data_transfer import ApiUsageDataTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsageDataTransfer from a JSON string
api_usage_data_transfer_instance = ApiUsageDataTransfer.from_json(json)
# print the JSON string representation of the object
print(ApiUsageDataTransfer.to_json())

# convert the object into a dict
api_usage_data_transfer_dict = api_usage_data_transfer_instance.to_dict()
# create an instance of ApiUsageDataTransfer from a dict
api_usage_data_transfer_from_dict = ApiUsageDataTransfer.from_dict(api_usage_data_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


