# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_photonic_media_frequency_constraint import TapiPhotonicMediaFrequencyConstraint  # noqa: F401,E501
from tapi_server import util


class TapiPhotonicMediaSpectrumBand(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lower_frequency=None, upper_frequency=None, frequency_constraint=None):  # noqa: E501
        """TapiPhotonicMediaSpectrumBand - a model defined in OpenAPI

        :param lower_frequency: The lower_frequency of this TapiPhotonicMediaSpectrumBand.  # noqa: E501
        :type lower_frequency: int
        :param upper_frequency: The upper_frequency of this TapiPhotonicMediaSpectrumBand.  # noqa: E501
        :type upper_frequency: int
        :param frequency_constraint: The frequency_constraint of this TapiPhotonicMediaSpectrumBand.  # noqa: E501
        :type frequency_constraint: TapiPhotonicMediaFrequencyConstraint
        """
        self.openapi_types = {
            'lower_frequency': int,
            'upper_frequency': int,
            'frequency_constraint': TapiPhotonicMediaFrequencyConstraint
        }

        self.attribute_map = {
            'lower_frequency': 'lower-frequency',
            'upper_frequency': 'upper-frequency',
            'frequency_constraint': 'frequency-constraint'
        }

        self._lower_frequency = lower_frequency
        self._upper_frequency = upper_frequency
        self._frequency_constraint = frequency_constraint

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaSpectrumBand':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.SpectrumBand of this TapiPhotonicMediaSpectrumBand.  # noqa: E501
        :rtype: TapiPhotonicMediaSpectrumBand
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lower_frequency(self):
        """Gets the lower_frequency of this TapiPhotonicMediaSpectrumBand.

        The lower frequency bound of the media channel spectrum specified in MHz  # noqa: E501

        :return: The lower_frequency of this TapiPhotonicMediaSpectrumBand.
        :rtype: int
        """
        return self._lower_frequency

    @lower_frequency.setter
    def lower_frequency(self, lower_frequency):
        """Sets the lower_frequency of this TapiPhotonicMediaSpectrumBand.

        The lower frequency bound of the media channel spectrum specified in MHz  # noqa: E501

        :param lower_frequency: The lower_frequency of this TapiPhotonicMediaSpectrumBand.
        :type lower_frequency: int
        """

        self._lower_frequency = lower_frequency

    @property
    def upper_frequency(self):
        """Gets the upper_frequency of this TapiPhotonicMediaSpectrumBand.

        The upper frequency bound of the media channel spectrum specified in MHz  # noqa: E501

        :return: The upper_frequency of this TapiPhotonicMediaSpectrumBand.
        :rtype: int
        """
        return self._upper_frequency

    @upper_frequency.setter
    def upper_frequency(self, upper_frequency):
        """Sets the upper_frequency of this TapiPhotonicMediaSpectrumBand.

        The upper frequency bound of the media channel spectrum specified in MHz  # noqa: E501

        :param upper_frequency: The upper_frequency of this TapiPhotonicMediaSpectrumBand.
        :type upper_frequency: int
        """

        self._upper_frequency = upper_frequency

    @property
    def frequency_constraint(self):
        """Gets the frequency_constraint of this TapiPhotonicMediaSpectrumBand.


        :return: The frequency_constraint of this TapiPhotonicMediaSpectrumBand.
        :rtype: TapiPhotonicMediaFrequencyConstraint
        """
        return self._frequency_constraint

    @frequency_constraint.setter
    def frequency_constraint(self, frequency_constraint):
        """Sets the frequency_constraint of this TapiPhotonicMediaSpectrumBand.


        :param frequency_constraint: The frequency_constraint of this TapiPhotonicMediaSpectrumBand.
        :type frequency_constraint: TapiPhotonicMediaFrequencyConstraint
        """

        self._frequency_constraint = frequency_constraint
