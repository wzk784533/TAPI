# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_getserviceinterfacepointlist_output_sip import TapiCommonGetserviceinterfacepointlistOutputSip  # noqa: F401,E501
from tapi_server import util


class TapiCommonGetserviceinterfacepointlistOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sip=None):  # noqa: E501
        """TapiCommonGetserviceinterfacepointlistOutput - a model defined in OpenAPI

        :param sip: The sip of this TapiCommonGetserviceinterfacepointlistOutput.  # noqa: E501
        :type sip: List[TapiCommonGetserviceinterfacepointlistOutputSip]
        """
        self.openapi_types = {
            'sip': List[TapiCommonGetserviceinterfacepointlistOutputSip]
        }

        self.attribute_map = {
            'sip': 'sip'
        }

        self._sip = sip

    @classmethod
    def from_dict(cls, dikt) -> 'TapiCommonGetserviceinterfacepointlistOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.common.getserviceinterfacepointlist.Output of this TapiCommonGetserviceinterfacepointlistOutput.  # noqa: E501
        :rtype: TapiCommonGetserviceinterfacepointlistOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sip(self):
        """Gets the sip of this TapiCommonGetserviceinterfacepointlistOutput.

        none  # noqa: E501

        :return: The sip of this TapiCommonGetserviceinterfacepointlistOutput.
        :rtype: List[TapiCommonGetserviceinterfacepointlistOutputSip]
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        """Sets the sip of this TapiCommonGetserviceinterfacepointlistOutput.

        none  # noqa: E501

        :param sip: The sip of this TapiCommonGetserviceinterfacepointlistOutput.
        :type sip: List[TapiCommonGetserviceinterfacepointlistOutputSip]
        """

        self._sip = sip
