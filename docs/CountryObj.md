# CountryObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Country symbol | 

## Example

```python
from tradewatch.models.country_obj import CountryObj

# TODO update the JSON string below
json = "{}"
# create an instance of CountryObj from a JSON string
country_obj_instance = CountryObj.from_json(json)
# print the JSON string representation of the object
print(CountryObj.to_json())

# convert the object into a dict
country_obj_dict = country_obj_instance.to_dict()
# create an instance of CountryObj from a dict
country_obj_from_dict = CountryObj.from_dict(country_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


