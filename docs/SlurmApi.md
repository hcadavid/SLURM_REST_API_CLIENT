# openapi_client.SlurmApi

All URIs are relative to *https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurm_v0038_diag**](SlurmApi.md#slurm_v0038_diag) | **GET** /slurm/v0.0.38/diag | get diagnostics
[**slurm_v0038_get_job**](SlurmApi.md#slurm_v0038_get_job) | **GET** /slurm/v0.0.38/job/{job_id} | get job info
[**slurm_v0038_get_jobs**](SlurmApi.md#slurm_v0038_get_jobs) | **GET** /slurm/v0.0.38/jobs | get list of jobs
[**slurm_v0038_get_node**](SlurmApi.md#slurm_v0038_get_node) | **GET** /slurm/v0.0.38/node/{node_name} | get node info
[**slurm_v0038_get_nodes**](SlurmApi.md#slurm_v0038_get_nodes) | **GET** /slurm/v0.0.38/nodes | get all node info
[**slurm_v0038_get_partition**](SlurmApi.md#slurm_v0038_get_partition) | **GET** /slurm/v0.0.38/partition/{partition_name} | get partition info
[**slurm_v0038_get_partitions**](SlurmApi.md#slurm_v0038_get_partitions) | **GET** /slurm/v0.0.38/partitions | get all partition info
[**slurm_v0038_get_reservation**](SlurmApi.md#slurm_v0038_get_reservation) | **GET** /slurm/v0.0.38/reservation/{reservation_name} | get reservation info
[**slurm_v0038_get_reservations**](SlurmApi.md#slurm_v0038_get_reservations) | **GET** /slurm/v0.0.38/reservations | get all reservation info
[**slurm_v0038_ping**](SlurmApi.md#slurm_v0038_ping) | **GET** /slurm/v0.0.38/ping | ping test
[**slurm_v0038_slurmctld_get_licenses**](SlurmApi.md#slurm_v0038_slurmctld_get_licenses) | **GET** /slurm/v0.0.38/licenses | get all Slurm tracked license info


# **slurm_v0038_diag**
> V0038Diag slurm_v0038_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_diag import V0038Diag
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get diagnostics
        api_response = api_instance.slurm_v0038_diag()
        print("The response of SlurmApi->slurm_v0038_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0038Diag**](V0038Diag.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_job**
> V0038JobsResponse slurm_v0038_get_job(job_id)

get job info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_jobs_response import V0038JobsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Slurm JobID

    try:
        # get job info
        api_response = api_instance.slurm_v0038_get_job(job_id)
        print("The response of SlurmApi->slurm_v0038_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Slurm JobID | 

### Return type

[**V0038JobsResponse**](V0038JobsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job matching JobId not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_jobs**
> V0038JobsResponse slurm_v0038_get_jobs(update_time=update_time)

get list of jobs

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_jobs_response import V0038JobsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0038_get_jobs(update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0038JobsResponse**](V0038JobsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_node**
> V0038NodesResponse slurm_v0038_get_node(node_name)

get node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_nodes_response import V0038NodesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Slurm Node Name

    try:
        # get node info
        api_response = api_instance.slurm_v0038_get_node(node_name)
        print("The response of SlurmApi->slurm_v0038_get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Slurm Node Name | 

### Return type

[**V0038NodesResponse**](V0038NodesResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_nodes**
> V0038NodesResponse slurm_v0038_get_nodes(update_time=update_time)

get all node info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_nodes_response import V0038NodesResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all node info
        api_response = api_instance.slurm_v0038_get_nodes(update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0038NodesResponse**](V0038NodesResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | no nodes in cluster |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_partition**
> V0038PartitionsResponse slurm_v0038_get_partition(partition_name, update_time=update_time)

get partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_partitions_response import V0038PartitionsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Slurm Partition Name
    update_time = 56 # int | Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0038_get_partition(partition_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Slurm Partition Name | 
 **update_time** | **int**| Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time. | [optional] 

### Return type

[**V0038PartitionsResponse**](V0038PartitionsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_partitions**
> V0038PartitionsResponse slurm_v0038_get_partitions(update_time=update_time)

get all partition info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_partitions_response import V0038PartitionsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0038_get_partitions(update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0038PartitionsResponse**](V0038PartitionsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | no partitions found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_reservation**
> V0038ReservationsResponse slurm_v0038_get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_reservations_response import V0038ReservationsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Slurm Reservation Name
    update_time = 56 # int | Filter if no reservation (not limited to reservation in URL) changed since update_time. (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0038_get_reservation(reservation_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Slurm Reservation Name | 
 **update_time** | **int**| Filter if no reservation (not limited to reservation in URL) changed since update_time. | [optional] 

### Return type

[**V0038ReservationsResponse**](V0038ReservationsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_get_reservations**
> V0038ReservationsResponse slurm_v0038_get_reservations(update_time=update_time)

get all reservation info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_reservations_response import V0038ReservationsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)
    update_time = 56 # int | Filter if changed since update_time. Use of this parameter can result in faster replies. (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0038_get_reservations(update_time=update_time)
        print("The response of SlurmApi->slurm_v0038_get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **int**| Filter if changed since update_time. Use of this parameter can result in faster replies. | [optional] 

### Return type

[**V0038ReservationsResponse**](V0038ReservationsResponse.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | no reservations found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_ping**
> V0038Pings slurm_v0038_ping()

ping test

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_pings import V0038Pings
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurm_v0038_ping()
        print("The response of SlurmApi->slurm_v0038_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0038Pings**](V0038Pings.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | unable to request ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0038_slurmctld_get_licenses**
> V0038Licenses slurm_v0038_slurmctld_get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
from openapi_client.models.v0038_licenses import V0038Licenses
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SlurmApi(api_client)

    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0038_slurmctld_get_licenses()
        print("The response of SlurmApi->slurm_v0038_slurmctld_get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0038_slurmctld_get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0038Licenses**](V0038Licenses.md)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | unable to request licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

