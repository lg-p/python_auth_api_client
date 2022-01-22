# coding: utf-8

"""
    A swagger API

    powered by Flasgger  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.auth_api import AuthApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_full_logout_post(self):
        """Test case for api_v1_full_logout_post

        This endpoint deactivates the access token and refresh token for all active devices  # noqa: E501
        """
        pass

    def test_api_v1_history_get(self):
        """Test case for api_v1_history_get

        This endpoint gets the user's authentication history  # noqa: E501
        """
        pass

    def test_api_v1_profile_patch(self):
        """Test case for api_v1_profile_patch

        This endpoint modifies user data  # noqa: E501
        """
        pass

    def test_api_v1_signup_post(self):
        """Test case for api_v1_signup_post

        This endpoint is registering a user  # noqa: E501
        """
        pass

    def test_api_v1_token_deactivate_post(self):
        """Test case for api_v1_token_deactivate_post

        This endpoint deactivates the access token and refresh token  # noqa: E501
        """
        pass

    def test_api_v1_token_introspect_post(self):
        """Test case for api_v1_token_introspect_post

        This endpoint validates the access token  # noqa: E501
        """
        pass

    def test_api_v1_token_post(self):
        """Test case for api_v1_token_post

        This endpoint authenticates the user  # noqa: E501
        """
        pass

    def test_api_v1_token_refresh_post(self):
        """Test case for api_v1_token_refresh_post

        This endpoint receives an access token over a refresh token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()