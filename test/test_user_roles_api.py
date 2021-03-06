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
from swagger_client.api.user_roles_api import UserRolesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUserRolesApi(unittest.TestCase):
    """UserRolesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.user_roles_api.UserRolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_user_roles_assign_post(self):
        """Test case for api_v1_user_roles_assign_post

        This endpoint will assign a role to the user  # noqa: E501
        """
        pass

    def test_api_v1_user_roles_take_away_post(self):
        """Test case for api_v1_user_roles_take_away_post

        This endpoint will take away the role from the user  # noqa: E501
        """
        pass

    def test_api_v1_user_roles_user_id_get(self):
        """Test case for api_v1_user_roles_user_id_get

        This endpoint gets a list of available user roles  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
