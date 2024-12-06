# V0038Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | [**V0038MetaPlugin**](V0038MetaPlugin.md) |  | [optional] 
**slurm** | [**V0038MetaSlurm**](V0038MetaSlurm.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0038_meta import V0038Meta

# TODO update the JSON string below
json = "{}"
# create an instance of V0038Meta from a JSON string
v0038_meta_instance = V0038Meta.from_json(json)
# print the JSON string representation of the object
print(V0038Meta.to_json())

# convert the object into a dict
v0038_meta_dict = v0038_meta_instance.to_dict()
# create an instance of V0038Meta from a dict
v0038_meta_from_dict = V0038Meta.from_dict(v0038_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


