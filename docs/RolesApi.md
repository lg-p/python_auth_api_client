# swagger_client.RolesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_roles_get**](RolesApi.md#api_v1_roles_get) | **GET** /api/v1/roles | This endpoint receives a list of roles
[**api_v1_roles_post**](RolesApi.md#api_v1_roles_post) | **POST** /api/v1/roles | This endpoint creates a role
[**api_v1_roles_role_id_delete**](RolesApi.md#api_v1_roles_role_id_delete) | **DELETE** /api/v1/roles/{role_id} | This endpoint delete role
[**api_v1_roles_role_id_get**](RolesApi.md#api_v1_roles_role_id_get) | **GET** /api/v1/roles/{role_id} | This endpoint gets role by id
[**api_v1_roles_role_id_patch**](RolesApi.md#api_v1_roles_role_id_patch) | **PATCH** /api/v1/roles/{role_id} | This endpoint changes role


# **api_v1_roles_get**
> RoleModelResponse api_v1_roles_get()

This endpoint receives a list of roles

Requires authorization and access to the roles \"edit role\" and \"manage role\"<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))

try:
    # This endpoint receives a list of roles
    api_response = api_instance.api_v1_roles_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->api_v1_roles_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleModelResponse**](RoleModelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_roles_post**
> RoleModelResponse api_v1_roles_post(body)

This endpoint creates a role

Requires authorization and access role \"edit role\"<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RoleModel() # RoleModel | Create a Role

try:
    # This endpoint creates a role
    api_response = api_instance.api_v1_roles_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->api_v1_roles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RoleModel**](RoleModel.md)| Create a Role | 

### Return type

[**RoleModelResponse**](RoleModelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_roles_role_id_delete**
> api_v1_roles_role_id_delete(id)

This endpoint delete role

Requires authorization and access role \"edit role\"<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # This endpoint delete role
    api_instance.api_v1_roles_role_id_delete(id)
except ApiException as e:
    print("Exception when calling RolesApi->api_v1_roles_role_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_roles_role_id_get**
> RoleModelResponse api_v1_roles_role_id_get(id)

This endpoint gets role by id

Requires authorization and access role \"edit role\"<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # This endpoint gets role by id
    api_response = api_instance.api_v1_roles_role_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->api_v1_roles_role_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RoleModelResponse**](RoleModelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_roles_role_id_patch**
> api_v1_roles_role_id_patch(id)

This endpoint changes role

Requires authorization and access role \"edit role\"<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Authorization
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # This endpoint changes role
    api_instance.api_v1_roles_role_id_patch(id)
except ApiException as e:
    print("Exception when calling RolesApi->api_v1_roles_role_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

