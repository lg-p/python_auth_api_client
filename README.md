# swagger-client
powered by Flasgger

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/lg-p/Movie_contracts.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/lg-p/Movie_contracts.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**api_v1_full_logout_post**](docs/AuthApi.md#api_v1_full_logout_post) | **POST** /api/v1/full_logout | This endpoint deactivates the access token and refresh token for all active devices
*AuthApi* | [**api_v1_history_get**](docs/AuthApi.md#api_v1_history_get) | **GET** /api/v1/history | This endpoint gets the user&#39;s authentication history
*AuthApi* | [**api_v1_profile_patch**](docs/AuthApi.md#api_v1_profile_patch) | **PATCH** /api/v1/profile | This endpoint modifies user data
*AuthApi* | [**api_v1_signup_post**](docs/AuthApi.md#api_v1_signup_post) | **POST** /api/v1/signup | This endpoint is registering a user
*AuthApi* | [**api_v1_token_deactivate_post**](docs/AuthApi.md#api_v1_token_deactivate_post) | **POST** /api/v1/token/deactivate | This endpoint deactivates the access token and refresh token
*AuthApi* | [**api_v1_token_introspect_post**](docs/AuthApi.md#api_v1_token_introspect_post) | **POST** /api/v1/token/introspect | This endpoint validates the access token
*AuthApi* | [**api_v1_token_post**](docs/AuthApi.md#api_v1_token_post) | **POST** /api/v1/token | This endpoint authenticates the user
*AuthApi* | [**api_v1_token_refresh_post**](docs/AuthApi.md#api_v1_token_refresh_post) | **POST** /api/v1/token/refresh | This endpoint receives an access token over a refresh token
*OauthApi* | [**oauth_callback_get**](docs/OauthApi.md#oauth_callback_get) | **GET** /oauth/callback | Process callback from oauth provider
*OauthApi* | [**oauth_signin_get**](docs/OauthApi.md#oauth_signin_get) | **GET** /oauth/signin | Get oauth authorization redirect url for signup
*RolesApi* | [**api_v1_roles_get**](docs/RolesApi.md#api_v1_roles_get) | **GET** /api/v1/roles | This endpoint receives a list of roles
*RolesApi* | [**api_v1_roles_post**](docs/RolesApi.md#api_v1_roles_post) | **POST** /api/v1/roles | This endpoint creates a role
*RolesApi* | [**api_v1_roles_role_id_delete**](docs/RolesApi.md#api_v1_roles_role_id_delete) | **DELETE** /api/v1/roles/{role_id} | This endpoint delete role
*RolesApi* | [**api_v1_roles_role_id_get**](docs/RolesApi.md#api_v1_roles_role_id_get) | **GET** /api/v1/roles/{role_id} | This endpoint gets role by id
*RolesApi* | [**api_v1_roles_role_id_patch**](docs/RolesApi.md#api_v1_roles_role_id_patch) | **PATCH** /api/v1/roles/{role_id} | This endpoint changes role
*UserRolesApi* | [**api_v1_user_roles_assign_post**](docs/UserRolesApi.md#api_v1_user_roles_assign_post) | **POST** /api/v1/user_roles/assign | This endpoint will assign a role to the user
*UserRolesApi* | [**api_v1_user_roles_take_away_post**](docs/UserRolesApi.md#api_v1_user_roles_take_away_post) | **POST** /api/v1/user_roles/take_away | This endpoint will take away the role from the user
*UserRolesApi* | [**api_v1_user_roles_user_id_get**](docs/UserRolesApi.md#api_v1_user_roles_user_id_get) | **GET** /api/v1/user_roles/{user_id} | This endpoint gets a list of available user roles


## Documentation For Models

 - [DeactivateToken](docs/DeactivateToken.md)
 - [GetToken](docs/GetToken.md)
 - [GetUserRoleModels](docs/GetUserRoleModels.md)
 - [HistoryModelResponse](docs/HistoryModelResponse.md)
 - [IntrospectToken](docs/IntrospectToken.md)
 - [IntrospectTokenModelResponse](docs/IntrospectTokenModelResponse.md)
 - [RefreshToken](docs/RefreshToken.md)
 - [RoleModel](docs/RoleModel.md)
 - [RoleModelResponse](docs/RoleModelResponse.md)
 - [TokenResponseModel](docs/TokenResponseModel.md)
 - [UserModel](docs/UserModel.md)
 - [UserRoleModel](docs/UserRoleModel.md)


## Documentation For Authorization


## Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


