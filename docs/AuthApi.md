# swagger_client.AuthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_full_logout_post**](AuthApi.md#api_v1_full_logout_post) | **POST** /api/v1/full_logout | This endpoint deactivates the access token and refresh token for all active devices
[**api_v1_history_get**](AuthApi.md#api_v1_history_get) | **GET** /api/v1/history | This endpoint gets the user&#39;s authentication history
[**api_v1_profile_patch**](AuthApi.md#api_v1_profile_patch) | **PATCH** /api/v1/profile | This endpoint modifies user data
[**api_v1_signup_post**](AuthApi.md#api_v1_signup_post) | **POST** /api/v1/signup | This endpoint is registering a user
[**api_v1_token_deactivate_post**](AuthApi.md#api_v1_token_deactivate_post) | **POST** /api/v1/token/deactivate | This endpoint deactivates the access token and refresh token
[**api_v1_token_introspect_post**](AuthApi.md#api_v1_token_introspect_post) | **POST** /api/v1/token/introspect | This endpoint validates the access token
[**api_v1_token_post**](AuthApi.md#api_v1_token_post) | **POST** /api/v1/token | This endpoint authenticates the user
[**api_v1_token_refresh_post**](AuthApi.md#api_v1_token_refresh_post) | **POST** /api/v1/token/refresh | This endpoint receives an access token over a refresh token


# **api_v1_full_logout_post**
> api_v1_full_logout_post()

This endpoint deactivates the access token and refresh token for all active devices

Requires authorization<br/>

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # This endpoint deactivates the access token and refresh token for all active devices
    api_instance.api_v1_full_logout_post()
except ApiException as e:
    print("Exception when calling AuthApi->api_v1_full_logout_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_history_get**
> HistoryModelResponse api_v1_history_get(page, number_per_page)

This endpoint gets the user's authentication history

Requires authorization<br/>

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number (default to 1)
number_per_page = 20 # object | Number per page (default to 20)

try:
    # This endpoint gets the user's authentication history
    api_response = api_instance.api_v1_history_get(page, number_per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v1_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number | [default to 1]
 **number_per_page** | [**object**](.md)| Number per page | [default to 20]

### Return type

[**HistoryModelResponse**](HistoryModelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_profile_patch**
> api_v1_profile_patch(body)

This endpoint modifies user data

Requires authorization<br/>(one or more valid user parameters)<br/>

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserModel() # UserModel | Changes user data

try:
    # This endpoint modifies user data
    api_instance.api_v1_profile_patch(body)
except ApiException as e:
    print("Exception when calling AuthApi->api_v1_profile_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserModel**](UserModel.md)| Changes user data | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_signup_post**
> api_v1_signup_post(body)

This endpoint is registering a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.UserModel() # UserModel | User registration

try:
    # This endpoint is registering a user
    api_instance.api_v1_signup_post(body)
except ApiException as e:
    print("Exception when calling AuthApi->api_v1_signup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserModel**](UserModel.md)| User registration | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_token_deactivate_post**
> api_v1_token_deactivate_post(body)

This endpoint deactivates the access token and refresh token

Requires authorization<br/>

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
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeactivateToken() # DeactivateToken | Deactivate tokens

try:
    # This endpoint deactivates the access token and refresh token
    api_instance.api_v1_token_deactivate_post(body)
except ApiException as e:
    print("Exception when calling AuthApi->api_v1_token_deactivate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeactivateToken**](DeactivateToken.md)| Deactivate tokens | 

### Return type

void (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_token_introspect_post**
> IntrospectTokenModelResponse api_v1_token_introspect_post(body)

This endpoint validates the access token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.IntrospectToken() # IntrospectToken | Check access token

try:
    # This endpoint validates the access token
    api_response = api_instance.api_v1_token_introspect_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v1_token_introspect_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntrospectToken**](IntrospectToken.md)| Check access token | 

### Return type

[**IntrospectTokenModelResponse**](IntrospectTokenModelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_token_post**
> TokenResponseModel api_v1_token_post(body)

This endpoint authenticates the user

Returns an access token and a refresh token<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.GetToken() # GetToken | Get tokens

try:
    # This endpoint authenticates the user
    api_response = api_instance.api_v1_token_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v1_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetToken**](GetToken.md)| Get tokens | 

### Return type

[**TokenResponseModel**](TokenResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_token_refresh_post**
> TokenResponseModel api_v1_token_refresh_post(body)

This endpoint receives an access token over a refresh token

Returns fresh access token and refresh token<br/>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = swagger_client.RefreshToken() # RefreshToken | Refresh tokens

try:
    # This endpoint receives an access token over a refresh token
    api_response = api_instance.api_v1_token_refresh_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_v1_token_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshToken**](RefreshToken.md)| Refresh tokens | 

### Return type

[**TokenResponseModel**](TokenResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

