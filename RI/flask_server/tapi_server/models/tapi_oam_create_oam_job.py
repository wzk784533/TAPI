# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_oam_createoamjob_output import TapiOamCreateoamjobOutput  # noqa: F401,E501
from tapi_server import util


class TapiOamCreateOamJob(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiOamCreateOamJob - a model defined in OpenAPI

        :param output: The output of this TapiOamCreateOamJob.  # noqa: E501
        :type output: TapiOamCreateoamjobOutput
        """
        self.openapi_types = {
            'output': TapiOamCreateoamjobOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamCreateOamJob':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.CreateOamJob of this TapiOamCreateOamJob.  # noqa: E501
        :rtype: TapiOamCreateOamJob
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiOamCreateOamJob.


        :return: The output of this TapiOamCreateOamJob.
        :rtype: TapiOamCreateoamjobOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiOamCreateOamJob.


        :param output: The output of this TapiOamCreateOamJob.
        :type output: TapiOamCreateoamjobOutput
        """

        self._output = output
