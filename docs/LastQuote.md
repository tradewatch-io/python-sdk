# LastQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol name | 
**ask** | **float** | The ask price. | 
**bid** | **float** | The bid price. | 
**mid** | **float** | The mid price. | 
**timestamp** | **int** |  | 

## Example

```python
from tradewatch.models.last_quote import LastQuote

# TODO update the JSON string below
json = "{}"
# create an instance of LastQuote from a JSON string
last_quote_instance = LastQuote.from_json(json)
# print the JSON string representation of the object
print(LastQuote.to_json())

# convert the object into a dict
last_quote_dict = last_quote_instance.to_dict()
# create an instance of LastQuote from a dict
last_quote_from_dict = LastQuote.from_dict(last_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


