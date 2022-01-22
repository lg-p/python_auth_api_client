# swagger_client.UserRolesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_user_roles_assign_post**](UserRolesApi.md#api_v1_user_roles_assign_post) | **POST** /api/v1/user_roles/assign | This endpoint will assign a role to the user
[**api_v1_user_roles_take_away_post**](UserRolesApi.md#api_v1_user_roles_take_away_post) | **POST** /api/v1/user_roles/take_away | This endpoint will take away the role from the user
[**api_v1_user_roles_user_id_get**](UserRolesApi.md#api_v1_user_roles_user_id_get) | **GET** /api/v1/user_roles/{user_id} | This endpoint gets a list of available user roles


# **api_v1_user_roles_assign_post**
> api_v1_user_roles_assign_post(user_id, role_id)

This endpoint will assign a role to the user

Requires authorization and access role \"manage role\"<br/>

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
api_instance = swagger_client.UserRolesApi(swagger_client.ApiClient(configuration))
user_id = swagger_client.UserRoleModel() # UserRoleModel | 
role_id = swagger_client.UserRoleModel() # UserRoleModel | 

try:
    # This endpoint will assign a role to the user
    api_instance.api_v1_user_roles_assign_post(user_id, role_id)
except ApiException as e:
    print("Exception when calling UserRolesApi->api_v1_user_roles_assign_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserRoleModel**](UserRoleModel.md)|  | 
 **role_id** | [**UserRoleModel**](UserRoleModel.md)|  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_roles_take_away_post**
> api_v1_user_roles_take_away_post(user_id, role_id)

This endpoint will take away the role from the user

Requires authorization and access role \"manage role\"<br/>

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
api_instance = swagger_client.UserRolesApi(swagger_client.ApiClient(configuration))
user_id = swagger_client.UserRoleModel() # UserRoleModel | 
role_id = swagger_client.UserRoleModel() # UserRoleModel | 

try:
    # This endpoint will take away the role from the user
    api_instance.api_v1_user_roles_take_away_post(user_id, role_id)
except ApiException as e:
    print("Exception when calling UserRolesApi->api_v1_user_roles_take_away_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**UserRoleModel**](UserRoleModel.md)|  | 
 **role_id** | [**UserRoleModel**](UserRoleModel.md)|  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_user_roles_user_id_get**
> api_v1_user_roles_user_id_get(user_id)

This endpoint gets a list of available user roles

Requires authorization and access role \"manage role\"<br/>

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
api_instance = swagger_client.UserRolesApi(swagger_client.ApiClient(configuration))
user_id = swagger_client.GetUserRoleModels() # GetUserRoleModels | 

try:
    # This endpoint gets a list of available user roles
    api_instance.api_v1_user_roles_user_id_get(user_id)
except ApiException as e:
    print("Exception when calling UserRolesApi->api_v1_user_roles_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**GetUserRoleModels**](GetUserRoleModels.md)|  | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

