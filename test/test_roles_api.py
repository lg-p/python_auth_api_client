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
from swagger_client.api.roles_api import RolesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.roles_api.RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_roles_get(self):
        """Test case for api_v1_roles_get

        This endpoint receives a list of roles  # noqa: E501
        """
        pass

    def test_api_v1_roles_post(self):
        """Test case for api_v1_roles_post

        This endpoint creates a role  # noqa: E501
        """
        pass

    def test_api_v1_roles_role_id_delete(self):
        """Test case for api_v1_roles_role_id_delete

        This endpoint delete role  # noqa: E501
        """
        pass

    def test_api_v1_roles_role_id_get(self):
        """Test case for api_v1_roles_role_id_get

        This endpoint gets role by id  # noqa: E501
        """
        pass

    def test_api_v1_roles_role_id_patch(self):
        """Test case for api_v1_roles_role_id_patch

        This endpoint changes role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
