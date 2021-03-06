# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_path_computation_optimizep2ppath_input import TapiPathComputationOptimizep2ppathInput  # noqa: F401,E501
from tapi_server import util


class InlineObject26(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None):  # noqa: E501
        """InlineObject26 - a model defined in OpenAPI

        :param input: The input of this InlineObject26.  # noqa: E501
        :type input: TapiPathComputationOptimizep2ppathInput
        """
        self.openapi_types = {
            'input': TapiPathComputationOptimizep2ppathInput
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject26':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_26 of this InlineObject26.  # noqa: E501
        :rtype: InlineObject26
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InlineObject26.


        :return: The input of this InlineObject26.
        :rtype: TapiPathComputationOptimizep2ppathInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InlineObject26.


        :param input: The input of this InlineObject26.
        :type input: TapiPathComputationOptimizep2ppathInput
        """

        self._input = input
