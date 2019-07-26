# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_global_class import TapiCommonGlobalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_layer_protocol_name import TapiCommonLayerProtocolName  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_coordinate_type import TapiConnectivityCoordinateType  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_resilience_constraint import TapiConnectivityResilienceConstraint  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_reversion_mode import TapiConnectivityReversionMode  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_switch import TapiConnectivitySwitch  # noqa: F401,E501
from tapi_server.models.tapi_connectivity_switch_control_ref import TapiConnectivitySwitchControlRef  # noqa: F401,E501
from tapi_server.models.tapi_topology_resilience_type import TapiTopologyResilienceType  # noqa: F401,E501
from tapi_server import util


class TapiConnectivitySwitchControl(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, uuid=None, is_lock_out=False, max_switch_times=None, restoration_coordinate_type=None, is_coordinated_switching_both_ends=False, hold_off_time=None, is_frozen=False, wait_to_revert_time=15, resilience_type=None, preferred_restoration_layer=None, restore_priority=None, reversion_mode=None, sub_switch_control=None, switch=None):  # noqa: E501
        """TapiConnectivitySwitchControl - a model defined in OpenAPI

        :param name: The name of this TapiConnectivitySwitchControl.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param uuid: The uuid of this TapiConnectivitySwitchControl.  # noqa: E501
        :type uuid: str
        :param is_lock_out: The is_lock_out of this TapiConnectivitySwitchControl.  # noqa: E501
        :type is_lock_out: bool
        :param max_switch_times: The max_switch_times of this TapiConnectivitySwitchControl.  # noqa: E501
        :type max_switch_times: int
        :param restoration_coordinate_type: The restoration_coordinate_type of this TapiConnectivitySwitchControl.  # noqa: E501
        :type restoration_coordinate_type: TapiConnectivityCoordinateType
        :param is_coordinated_switching_both_ends: The is_coordinated_switching_both_ends of this TapiConnectivitySwitchControl.  # noqa: E501
        :type is_coordinated_switching_both_ends: bool
        :param hold_off_time: The hold_off_time of this TapiConnectivitySwitchControl.  # noqa: E501
        :type hold_off_time: int
        :param is_frozen: The is_frozen of this TapiConnectivitySwitchControl.  # noqa: E501
        :type is_frozen: bool
        :param wait_to_revert_time: The wait_to_revert_time of this TapiConnectivitySwitchControl.  # noqa: E501
        :type wait_to_revert_time: int
        :param resilience_type: The resilience_type of this TapiConnectivitySwitchControl.  # noqa: E501
        :type resilience_type: TapiTopologyResilienceType
        :param preferred_restoration_layer: The preferred_restoration_layer of this TapiConnectivitySwitchControl.  # noqa: E501
        :type preferred_restoration_layer: List[TapiCommonLayerProtocolName]
        :param restore_priority: The restore_priority of this TapiConnectivitySwitchControl.  # noqa: E501
        :type restore_priority: int
        :param reversion_mode: The reversion_mode of this TapiConnectivitySwitchControl.  # noqa: E501
        :type reversion_mode: TapiConnectivityReversionMode
        :param sub_switch_control: The sub_switch_control of this TapiConnectivitySwitchControl.  # noqa: E501
        :type sub_switch_control: List[TapiConnectivitySwitchControlRef]
        :param switch: The switch of this TapiConnectivitySwitchControl.  # noqa: E501
        :type switch: List[TapiConnectivitySwitch]
        """
        self.openapi_types = {
            'name': List[TapiCommonNameAndValue],
            'uuid': str,
            'is_lock_out': bool,
            'max_switch_times': int,
            'restoration_coordinate_type': TapiConnectivityCoordinateType,
            'is_coordinated_switching_both_ends': bool,
            'hold_off_time': int,
            'is_frozen': bool,
            'wait_to_revert_time': int,
            'resilience_type': TapiTopologyResilienceType,
            'preferred_restoration_layer': List[TapiCommonLayerProtocolName],
            'restore_priority': int,
            'reversion_mode': TapiConnectivityReversionMode,
            'sub_switch_control': List[TapiConnectivitySwitchControlRef],
            'switch': List[TapiConnectivitySwitch]
        }

        self.attribute_map = {
            'name': 'name',
            'uuid': 'uuid',
            'is_lock_out': 'is-lock-out',
            'max_switch_times': 'max-switch-times',
            'restoration_coordinate_type': 'restoration-coordinate-type',
            'is_coordinated_switching_both_ends': 'is-coordinated-switching-both-ends',
            'hold_off_time': 'hold-off-time',
            'is_frozen': 'is-frozen',
            'wait_to_revert_time': 'wait-to-revert-time',
            'resilience_type': 'resilience-type',
            'preferred_restoration_layer': 'preferred-restoration-layer',
            'restore_priority': 'restore-priority',
            'reversion_mode': 'reversion-mode',
            'sub_switch_control': 'sub-switch-control',
            'switch': 'switch'
        }

        self._name = name
        self._uuid = uuid
        self._is_lock_out = is_lock_out
        self._max_switch_times = max_switch_times
        self._restoration_coordinate_type = restoration_coordinate_type
        self._is_coordinated_switching_both_ends = is_coordinated_switching_both_ends
        self._hold_off_time = hold_off_time
        self._is_frozen = is_frozen
        self._wait_to_revert_time = wait_to_revert_time
        self._resilience_type = resilience_type
        self._preferred_restoration_layer = preferred_restoration_layer
        self._restore_priority = restore_priority
        self._reversion_mode = reversion_mode
        self._sub_switch_control = sub_switch_control
        self._switch = switch

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivitySwitchControl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.SwitchControl of this TapiConnectivitySwitchControl.  # noqa: E501
        :rtype: TapiConnectivitySwitchControl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TapiConnectivitySwitchControl.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiConnectivitySwitchControl.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiConnectivitySwitchControl.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiConnectivitySwitchControl.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this TapiConnectivitySwitchControl.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this TapiConnectivitySwitchControl.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TapiConnectivitySwitchControl.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this TapiConnectivitySwitchControl.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def is_lock_out(self):
        """Gets the is_lock_out of this TapiConnectivitySwitchControl.

        The resource is configured to temporarily not be available for use in the protection scheme(s) it is part of.                      This overrides all other protection control states including forced.                      If the item is locked out then it cannot be used under any circumstances.                      Note: Only relevant when part of a protection scheme.  # noqa: E501

        :return: The is_lock_out of this TapiConnectivitySwitchControl.
        :rtype: bool
        """
        return self._is_lock_out

    @is_lock_out.setter
    def is_lock_out(self, is_lock_out):
        """Sets the is_lock_out of this TapiConnectivitySwitchControl.

        The resource is configured to temporarily not be available for use in the protection scheme(s) it is part of.                      This overrides all other protection control states including forced.                      If the item is locked out then it cannot be used under any circumstances.                      Note: Only relevant when part of a protection scheme.  # noqa: E501

        :param is_lock_out: The is_lock_out of this TapiConnectivitySwitchControl.
        :type is_lock_out: bool
        """

        self._is_lock_out = is_lock_out

    @property
    def max_switch_times(self):
        """Gets the max_switch_times of this TapiConnectivitySwitchControl.

        Used to limit the maximum swtich times. When work fault disappears , and traffic return to the original work path, switch counter reset.  # noqa: E501

        :return: The max_switch_times of this TapiConnectivitySwitchControl.
        :rtype: int
        """
        return self._max_switch_times

    @max_switch_times.setter
    def max_switch_times(self, max_switch_times):
        """Sets the max_switch_times of this TapiConnectivitySwitchControl.

        Used to limit the maximum swtich times. When work fault disappears , and traffic return to the original work path, switch counter reset.  # noqa: E501

        :param max_switch_times: The max_switch_times of this TapiConnectivitySwitchControl.
        :type max_switch_times: int
        """

        self._max_switch_times = max_switch_times

    @property
    def restoration_coordinate_type(self):
        """Gets the restoration_coordinate_type of this TapiConnectivitySwitchControl.


        :return: The restoration_coordinate_type of this TapiConnectivitySwitchControl.
        :rtype: TapiConnectivityCoordinateType
        """
        return self._restoration_coordinate_type

    @restoration_coordinate_type.setter
    def restoration_coordinate_type(self, restoration_coordinate_type):
        """Sets the restoration_coordinate_type of this TapiConnectivitySwitchControl.


        :param restoration_coordinate_type: The restoration_coordinate_type of this TapiConnectivitySwitchControl.
        :type restoration_coordinate_type: TapiConnectivityCoordinateType
        """

        self._restoration_coordinate_type = restoration_coordinate_type

    @property
    def is_coordinated_switching_both_ends(self):
        """Gets the is_coordinated_switching_both_ends of this TapiConnectivitySwitchControl.

        Is operating such that switching at both ends of each flow acorss the FC is coordinated at both ingress and egress ends.  # noqa: E501

        :return: The is_coordinated_switching_both_ends of this TapiConnectivitySwitchControl.
        :rtype: bool
        """
        return self._is_coordinated_switching_both_ends

    @is_coordinated_switching_both_ends.setter
    def is_coordinated_switching_both_ends(self, is_coordinated_switching_both_ends):
        """Sets the is_coordinated_switching_both_ends of this TapiConnectivitySwitchControl.

        Is operating such that switching at both ends of each flow acorss the FC is coordinated at both ingress and egress ends.  # noqa: E501

        :param is_coordinated_switching_both_ends: The is_coordinated_switching_both_ends of this TapiConnectivitySwitchControl.
        :type is_coordinated_switching_both_ends: bool
        """

        self._is_coordinated_switching_both_ends = is_coordinated_switching_both_ends

    @property
    def hold_off_time(self):
        """Gets the hold_off_time of this TapiConnectivitySwitchControl.

        This attribute indicates the time, in milliseconds, between declaration of signal degrade or signal fail, and the initialization of the protection switching algorithm.  # noqa: E501

        :return: The hold_off_time of this TapiConnectivitySwitchControl.
        :rtype: int
        """
        return self._hold_off_time

    @hold_off_time.setter
    def hold_off_time(self, hold_off_time):
        """Sets the hold_off_time of this TapiConnectivitySwitchControl.

        This attribute indicates the time, in milliseconds, between declaration of signal degrade or signal fail, and the initialization of the protection switching algorithm.  # noqa: E501

        :param hold_off_time: The hold_off_time of this TapiConnectivitySwitchControl.
        :type hold_off_time: int
        """

        self._hold_off_time = hold_off_time

    @property
    def is_frozen(self):
        """Gets the is_frozen of this TapiConnectivitySwitchControl.

        Temporarily prevents any switch action to be taken and, as such, freezes the current state.                       Until the freeze is cleared, additional near-end external commands are rejected and fault condition changes and received APS messages are ignored.                      All administrative controls of any aspect of protection are rejected.  # noqa: E501

        :return: The is_frozen of this TapiConnectivitySwitchControl.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this TapiConnectivitySwitchControl.

        Temporarily prevents any switch action to be taken and, as such, freezes the current state.                       Until the freeze is cleared, additional near-end external commands are rejected and fault condition changes and received APS messages are ignored.                      All administrative controls of any aspect of protection are rejected.  # noqa: E501

        :param is_frozen: The is_frozen of this TapiConnectivitySwitchControl.
        :type is_frozen: bool
        """

        self._is_frozen = is_frozen

    @property
    def wait_to_revert_time(self):
        """Gets the wait_to_revert_time of this TapiConnectivitySwitchControl.

        If the protection system is revertive, this attribute specifies the time, in minutes, to wait after a fault clears on a higher priority (preferred) resource before reverting to the preferred resource.  # noqa: E501

        :return: The wait_to_revert_time of this TapiConnectivitySwitchControl.
        :rtype: int
        """
        return self._wait_to_revert_time

    @wait_to_revert_time.setter
    def wait_to_revert_time(self, wait_to_revert_time):
        """Sets the wait_to_revert_time of this TapiConnectivitySwitchControl.

        If the protection system is revertive, this attribute specifies the time, in minutes, to wait after a fault clears on a higher priority (preferred) resource before reverting to the preferred resource.  # noqa: E501

        :param wait_to_revert_time: The wait_to_revert_time of this TapiConnectivitySwitchControl.
        :type wait_to_revert_time: int
        """

        self._wait_to_revert_time = wait_to_revert_time

    @property
    def resilience_type(self):
        """Gets the resilience_type of this TapiConnectivitySwitchControl.


        :return: The resilience_type of this TapiConnectivitySwitchControl.
        :rtype: TapiTopologyResilienceType
        """
        return self._resilience_type

    @resilience_type.setter
    def resilience_type(self, resilience_type):
        """Sets the resilience_type of this TapiConnectivitySwitchControl.


        :param resilience_type: The resilience_type of this TapiConnectivitySwitchControl.
        :type resilience_type: TapiTopologyResilienceType
        """

        self._resilience_type = resilience_type

    @property
    def preferred_restoration_layer(self):
        """Gets the preferred_restoration_layer of this TapiConnectivitySwitchControl.

        Indicate which layer this resilience parameters package configured for.  # noqa: E501

        :return: The preferred_restoration_layer of this TapiConnectivitySwitchControl.
        :rtype: List[TapiCommonLayerProtocolName]
        """
        return self._preferred_restoration_layer

    @preferred_restoration_layer.setter
    def preferred_restoration_layer(self, preferred_restoration_layer):
        """Sets the preferred_restoration_layer of this TapiConnectivitySwitchControl.

        Indicate which layer this resilience parameters package configured for.  # noqa: E501

        :param preferred_restoration_layer: The preferred_restoration_layer of this TapiConnectivitySwitchControl.
        :type preferred_restoration_layer: List[TapiCommonLayerProtocolName]
        """

        self._preferred_restoration_layer = preferred_restoration_layer

    @property
    def restore_priority(self):
        """Gets the restore_priority of this TapiConnectivitySwitchControl.

        none  # noqa: E501

        :return: The restore_priority of this TapiConnectivitySwitchControl.
        :rtype: int
        """
        return self._restore_priority

    @restore_priority.setter
    def restore_priority(self, restore_priority):
        """Sets the restore_priority of this TapiConnectivitySwitchControl.

        none  # noqa: E501

        :param restore_priority: The restore_priority of this TapiConnectivitySwitchControl.
        :type restore_priority: int
        """

        self._restore_priority = restore_priority

    @property
    def reversion_mode(self):
        """Gets the reversion_mode of this TapiConnectivitySwitchControl.


        :return: The reversion_mode of this TapiConnectivitySwitchControl.
        :rtype: TapiConnectivityReversionMode
        """
        return self._reversion_mode

    @reversion_mode.setter
    def reversion_mode(self, reversion_mode):
        """Sets the reversion_mode of this TapiConnectivitySwitchControl.


        :param reversion_mode: The reversion_mode of this TapiConnectivitySwitchControl.
        :type reversion_mode: TapiConnectivityReversionMode
        """

        self._reversion_mode = reversion_mode

    @property
    def sub_switch_control(self):
        """Gets the sub_switch_control of this TapiConnectivitySwitchControl.

        none  # noqa: E501

        :return: The sub_switch_control of this TapiConnectivitySwitchControl.
        :rtype: List[TapiConnectivitySwitchControlRef]
        """
        return self._sub_switch_control

    @sub_switch_control.setter
    def sub_switch_control(self, sub_switch_control):
        """Sets the sub_switch_control of this TapiConnectivitySwitchControl.

        none  # noqa: E501

        :param sub_switch_control: The sub_switch_control of this TapiConnectivitySwitchControl.
        :type sub_switch_control: List[TapiConnectivitySwitchControlRef]
        """

        self._sub_switch_control = sub_switch_control

    @property
    def switch(self):
        """Gets the switch of this TapiConnectivitySwitchControl.

        none  # noqa: E501

        :return: The switch of this TapiConnectivitySwitchControl.
        :rtype: List[TapiConnectivitySwitch]
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this TapiConnectivitySwitchControl.

        none  # noqa: E501

        :param switch: The switch of this TapiConnectivitySwitchControl.
        :type switch: List[TapiConnectivitySwitch]
        """

        self._switch = switch
