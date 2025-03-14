# coding: utf-8
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.common.rest.configuration import Configuration


class TextSearchRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "project_id": "int",
        "query_string": "str",
        "label_constraints": "list[str]",
        "topk": "int",
        "params": "object",
    }

    attribute_map = {
        "project_id": "projectId",
        "query_string": "queryString",
        "label_constraints": "labelConstraints",
        "topk": "topk",
        "params": "params",
    }

    def __init__(
        self,
        project_id=None,
        query_string=None,
        label_constraints=None,
        topk=None,
        params=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """TextSearchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._query_string = None
        self._label_constraints = None
        self._topk = None
        self._params = None
        self.discriminator = None

        self.project_id = project_id
        self.query_string = query_string
        if label_constraints is not None:
            self.label_constraints = label_constraints
        self.topk = topk
        if params is not None:
            self.params = params

    @property
    def project_id(self):
        """Gets the project_id of this TextSearchRequest.  # noqa: E501


        :return: The project_id of this TextSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TextSearchRequest.


        :param project_id: The project_id of this TextSearchRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and project_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `project_id`, must not be `None`"
            )  # noqa: E501

        self._project_id = project_id

    @property
    def query_string(self):
        """Gets the query_string of this TextSearchRequest.  # noqa: E501


        :return: The query_string of this TextSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this TextSearchRequest.


        :param query_string: The query_string of this TextSearchRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and query_string is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `query_string`, must not be `None`"
            )  # noqa: E501

        self._query_string = query_string

    @property
    def label_constraints(self):
        """Gets the label_constraints of this TextSearchRequest.  # noqa: E501


        :return: The label_constraints of this TextSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._label_constraints

    @label_constraints.setter
    def label_constraints(self, label_constraints):
        """Sets the label_constraints of this TextSearchRequest.


        :param label_constraints: The label_constraints of this TextSearchRequest.  # noqa: E501
        :type: list[str]
        """

        self._label_constraints = label_constraints

    @property
    def topk(self):
        """Gets the topk of this TextSearchRequest.  # noqa: E501


        :return: The topk of this TextSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._topk

    @topk.setter
    def topk(self, topk):
        """Sets the topk of this TextSearchRequest.


        :param topk: The topk of this TextSearchRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and topk is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `topk`, must not be `None`"
            )  # noqa: E501

        self._topk = topk

    @property
    def params(self):
        """Gets the params of this TextSearchRequest.  # noqa: E501


        :return: The params of this TextSearchRequest.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this TextSearchRequest.


        :param params: The params of this TextSearchRequest.  # noqa: E501
        :type: object
        """

        self._params = params

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TextSearchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextSearchRequest):
            return True

        return self.to_dict() != other.to_dict()
