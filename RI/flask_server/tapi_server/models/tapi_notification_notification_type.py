# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiNotificationNotificationType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    OBJECT_CREATION = "OBJECT_CREATION"
    OBJECT_DELETION = "OBJECT_DELETION"
    ATTRIBUTE_VALUE_CHANGE = "ATTRIBUTE_VALUE_CHANGE"
    ALARM_EVENT = "ALARM_EVENT"
    THRESHOLD_CROSSING_ALERT = "THRESHOLD_CROSSING_ALERT"

    def __init__(self):  # noqa: E501
        """TapiNotificationNotificationType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TapiNotificationNotificationType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.notification.NotificationType of this TapiNotificationNotificationType.  # noqa: E501
        :rtype: TapiNotificationNotificationType
        """
        return util.deserialize_model(dikt, cls)
