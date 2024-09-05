# CountriesList

A list of Countries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CountryObj]**](CountryObj.md) |  | 

## Example

```python
from tradewatch.models.countries_list import CountriesList

# TODO update the JSON string below
json = "{}"
# create an instance of CountriesList from a JSON string
countries_list_instance = CountriesList.from_json(json)
# print the JSON string representation of the object
print(CountriesList.to_json())

# convert the object into a dict
countries_list_dict = countries_list_instance.to_dict()
# create an instance of CountriesList from a dict
countries_list_from_dict = CountriesList.from_dict(countries_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


