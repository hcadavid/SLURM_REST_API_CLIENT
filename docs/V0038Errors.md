# V0038Errors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0038Meta**](V0038Meta.md) |  | [optional] 
**errors** | [**List[V0038Error]**](V0038Error.md) | slurm errors | [optional] 

## Example

```python
from openapi_client.models.v0038_errors import V0038Errors

# TODO update the JSON string below
json = "{}"
# create an instance of V0038Errors from a JSON string
v0038_errors_instance = V0038Errors.from_json(json)
# print the JSON string representation of the object
print(V0038Errors.to_json())

# convert the object into a dict
v0038_errors_dict = v0038_errors_instance.to_dict()
# create an instance of V0038Errors from a dict
v0038_errors_from_dict = V0038Errors.from_dict(v0038_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


