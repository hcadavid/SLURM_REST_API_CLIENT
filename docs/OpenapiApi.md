# openapi_client.OpenapiApi

All URIs are relative to *https://virtserver.swaggerhub.com/hcadavid6/slurm-rest_api_ro/0.0.38*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openapi_get**](OpenapiApi.md#openapi_get) | **GET** /openapi | Retrieve OpenAPI Specification
[**openapi_json_get**](OpenapiApi.md#openapi_json_get) | **GET** /openapi.json | Retrieve OpenAPI Specification
[**openapi_v3_get**](OpenapiApi.md#openapi_v3_get) | **GET** /openapi/v3 | Retrieve OpenAPI Specification
[**openapi_yaml_get**](OpenapiApi.md#openapi_yaml_get) | **GET** /openapi.yaml | Retrieve OpenAPI Specification


# **openapi_get**
> openapi_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
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
    api_instance = openapi_client.OpenapiApi(api_client)

    try:
        # Retrieve OpenAPI Specification
        api_instance.openapi_get()
    except Exception as e:
        print("Exception when calling OpenapiApi->openapi_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_json_get**
> openapi_json_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
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
    api_instance = openapi_client.OpenapiApi(api_client)

    try:
        # Retrieve OpenAPI Specification
        api_instance.openapi_json_get()
    except Exception as e:
        print("Exception when calling OpenapiApi->openapi_json_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_v3_get**
> openapi_v3_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
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
    api_instance = openapi_client.OpenapiApi(api_client)

    try:
        # Retrieve OpenAPI Specification
        api_instance.openapi_v3_get()
    except Exception as e:
        print("Exception when calling OpenapiApi->openapi_v3_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_yaml_get**
> openapi_yaml_get()

Retrieve OpenAPI Specification

### Example

* Api Key Authentication (user):
* Api Key Authentication (token):

```python
import openapi_client
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
    api_instance = openapi_client.OpenapiApi(api_client)

    try:
        # Retrieve OpenAPI Specification
        api_instance.openapi_yaml_get()
    except Exception as e:
        print("Exception when calling OpenapiApi->openapi_yaml_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[user](../README.md#user), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenAPI Specification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

