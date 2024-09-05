# CursorPageTCustomizedSymbolsOutFull


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[SymbolsOutFull]**](SymbolsOutFull.md) |  | 
**total** | **int** |  | [optional] 
**current_page** | **str** |  | [optional] 
**current_page_backwards** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 

## Example

```python
from tradewatch.models.cursor_page_t_customized_symbols_out_full import CursorPageTCustomizedSymbolsOutFull

# TODO update the JSON string below
json = "{}"
# create an instance of CursorPageTCustomizedSymbolsOutFull from a JSON string
cursor_page_t_customized_symbols_out_full_instance = CursorPageTCustomizedSymbolsOutFull.from_json(json)
# print the JSON string representation of the object
print(CursorPageTCustomizedSymbolsOutFull.to_json())

# convert the object into a dict
cursor_page_t_customized_symbols_out_full_dict = cursor_page_t_customized_symbols_out_full_instance.to_dict()
# create an instance of CursorPageTCustomizedSymbolsOutFull from a dict
cursor_page_t_customized_symbols_out_full_from_dict = CursorPageTCustomizedSymbolsOutFull.from_dict(cursor_page_t_customized_symbols_out_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


