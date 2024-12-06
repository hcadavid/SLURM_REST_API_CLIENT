# V0038MetaSlurm

Slurm information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**V0038MetaSlurmVersion**](V0038MetaSlurmVersion.md) |  | [optional] 
**release** | **str** | version specifier | [optional] 

## Example

```python
from openapi_client.models.v0038_meta_slurm import V0038MetaSlurm

# TODO update the JSON string below
json = "{}"
# create an instance of V0038MetaSlurm from a JSON string
v0038_meta_slurm_instance = V0038MetaSlurm.from_json(json)
# print the JSON string representation of the object
print(V0038MetaSlurm.to_json())

# convert the object into a dict
v0038_meta_slurm_dict = v0038_meta_slurm_instance.to_dict()
# create an instance of V0038MetaSlurm from a dict
v0038_meta_slurm_from_dict = V0038MetaSlurm.from_dict(v0038_meta_slurm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


