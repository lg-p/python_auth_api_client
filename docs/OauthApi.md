# swagger_client.OauthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_callback_get**](OauthApi.md#oauth_callback_get) | **GET** /oauth/callback | Process callback from oauth provider
[**oauth_signin_get**](OauthApi.md#oauth_signin_get) | **GET** /oauth/signin | Get oauth authorization redirect url for signup


# **oauth_callback_get**
> oauth_callback_get()

Process callback from oauth provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthApi()

try:
    # Process callback from oauth provider
    api_instance.oauth_callback_get()
except ApiException as e:
    print("Exception when calling OauthApi->oauth_callback_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_signin_get**
> oauth_signin_get()

Get oauth authorization redirect url for signup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OauthApi()

try:
    # Get oauth authorization redirect url for signup
    api_instance.oauth_signin_get()
except ApiException as e:
    print("Exception when calling OauthApi->oauth_signin_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

