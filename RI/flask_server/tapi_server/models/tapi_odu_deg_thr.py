# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_odu_deg_thr_type import TapiOduDegThrType  # noqa: F401,E501
from tapi_server.models.tapi_odu_percentage_granularity import TapiOduPercentageGranularity  # noqa: F401,E501
from tapi_server import util


class TapiOduDegThr(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deg_thr_value=None, percentage_granularity=None, deg_thr_type=None):  # noqa: E501
        """TapiOduDegThr - a model defined in OpenAPI

        :param deg_thr_value: The deg_thr_value of this TapiOduDegThr.  # noqa: E501
        :type deg_thr_value: int
        :param percentage_granularity: The percentage_granularity of this TapiOduDegThr.  # noqa: E501
        :type percentage_granularity: TapiOduPercentageGranularity
        :param deg_thr_type: The deg_thr_type of this TapiOduDegThr.  # noqa: E501
        :type deg_thr_type: TapiOduDegThrType
        """
        self.openapi_types = {
            'deg_thr_value': int,
            'percentage_granularity': TapiOduPercentageGranularity,
            'deg_thr_type': TapiOduDegThrType
        }

        self.attribute_map = {
            'deg_thr_value': 'deg-thr-value',
            'percentage_granularity': 'percentage-granularity',
            'deg_thr_type': 'deg-thr-type'
        }

        self._deg_thr_value = deg_thr_value
        self._percentage_granularity = percentage_granularity
        self._deg_thr_type = deg_thr_type

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduDegThr':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.DegThr of this TapiOduDegThr.  # noqa: E501
        :rtype: TapiOduDegThr
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deg_thr_value(self):
        """Gets the deg_thr_value of this TapiOduDegThr.

        Percentage of detected errored blocks  # noqa: E501

        :return: The deg_thr_value of this TapiOduDegThr.
        :rtype: int
        """
        return self._deg_thr_value

    @deg_thr_value.setter
    def deg_thr_value(self, deg_thr_value):
        """Sets the deg_thr_value of this TapiOduDegThr.

        Percentage of detected errored blocks  # noqa: E501

        :param deg_thr_value: The deg_thr_value of this TapiOduDegThr.
        :type deg_thr_value: int
        """

        self._deg_thr_value = deg_thr_value

    @property
    def percentage_granularity(self):
        """Gets the percentage_granularity of this TapiOduDegThr.


        :return: The percentage_granularity of this TapiOduDegThr.
        :rtype: TapiOduPercentageGranularity
        """
        return self._percentage_granularity

    @percentage_granularity.setter
    def percentage_granularity(self, percentage_granularity):
        """Sets the percentage_granularity of this TapiOduDegThr.


        :param percentage_granularity: The percentage_granularity of this TapiOduDegThr.
        :type percentage_granularity: TapiOduPercentageGranularity
        """

        self._percentage_granularity = percentage_granularity

    @property
    def deg_thr_type(self):
        """Gets the deg_thr_type of this TapiOduDegThr.


        :return: The deg_thr_type of this TapiOduDegThr.
        :rtype: TapiOduDegThrType
        """
        return self._deg_thr_type

    @deg_thr_type.setter
    def deg_thr_type(self, deg_thr_type):
        """Sets the deg_thr_type of this TapiOduDegThr.


        :param deg_thr_type: The deg_thr_type of this TapiOduDegThr.
        :type deg_thr_type: TapiOduDegThrType
        """

        self._deg_thr_type = deg_thr_type
