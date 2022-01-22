# coding: utf-8

"""
    A swagger API

    powered by Flasgger  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class UserModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first_name': 'str',
        'last_name': 'str',
        'login': 'str',
        'password': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'login': 'login',
        'password': 'password'
    }

    def __init__(self, first_name=None, last_name=None, login=None, password=None, _configuration=None):  # noqa: E501
        """UserModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._last_name = None
        self._login = None
        self._password = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        self.login = login
        self.password = password

    @property
    def first_name(self):
        """Gets the first_name of this UserModel.  # noqa: E501


        :return: The first_name of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserModel.


        :param first_name: The first_name of this UserModel.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserModel.  # noqa: E501


        :return: The last_name of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserModel.


        :param last_name: The last_name of this UserModel.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def login(self):
        """Gets the login of this UserModel.  # noqa: E501


        :return: The login of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UserModel.


        :param login: The login of this UserModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501

        self._login = login

    @property
    def password(self):
        """Gets the password of this UserModel.  # noqa: E501


        :return: The password of this UserModel.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserModel.


        :param password: The password of this UserModel.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UserModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserModel):
            return True

        return self.to_dict() != other.to_dict()
