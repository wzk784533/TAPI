# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_forwarding_direction import TapiCommonForwardingDirection  # noqa: F401,E501
from tapi_server.models.tapi_common_global_class import TapiCommonGlobalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_layer_protocol_name import TapiCommonLayerProtocolName  # noqa: F401,E501
from tapi_server.models.tapi_common_lifecycle_state import TapiCommonLifecycleState  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_common_operational_state import TapiCommonOperationalState  # noqa: F401,E501
from tapi_server.models.tapi_common_operational_state_pac import TapiCommonOperationalStatePac  # noqa: F401,E501
from tapi_server.models.tapi_oam_meg_mep import TapiOamMegMep  # noqa: F401,E501
from tapi_server.models.tapi_oam_meg_mip import TapiOamMegMip  # noqa: F401,E501
from tapi_server import util


class TapiOamOamcontextMeg(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, uuid=None, operational_state=None, lifecycle_state=None, meg_identifier=None, meg_level=None, mip=None, layer_protocol_name=None, mep=None, direction=None):  # noqa: E501
        """TapiOamOamcontextMeg - a model defined in OpenAPI

        :param name: The name of this TapiOamOamcontextMeg.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param uuid: The uuid of this TapiOamOamcontextMeg.  # noqa: E501
        :type uuid: str
        :param operational_state: The operational_state of this TapiOamOamcontextMeg.  # noqa: E501
        :type operational_state: TapiCommonOperationalState
        :param lifecycle_state: The lifecycle_state of this TapiOamOamcontextMeg.  # noqa: E501
        :type lifecycle_state: TapiCommonLifecycleState
        :param meg_identifier: The meg_identifier of this TapiOamOamcontextMeg.  # noqa: E501
        :type meg_identifier: str
        :param meg_level: The meg_level of this TapiOamOamcontextMeg.  # noqa: E501
        :type meg_level: int
        :param mip: The mip of this TapiOamOamcontextMeg.  # noqa: E501
        :type mip: List[TapiOamMegMip]
        :param layer_protocol_name: The layer_protocol_name of this TapiOamOamcontextMeg.  # noqa: E501
        :type layer_protocol_name: TapiCommonLayerProtocolName
        :param mep: The mep of this TapiOamOamcontextMeg.  # noqa: E501
        :type mep: List[TapiOamMegMep]
        :param direction: The direction of this TapiOamOamcontextMeg.  # noqa: E501
        :type direction: TapiCommonForwardingDirection
        """
        self.openapi_types = {
            'name': List[TapiCommonNameAndValue],
            'uuid': str,
            'operational_state': TapiCommonOperationalState,
            'lifecycle_state': TapiCommonLifecycleState,
            'meg_identifier': str,
            'meg_level': int,
            'mip': List[TapiOamMegMip],
            'layer_protocol_name': TapiCommonLayerProtocolName,
            'mep': List[TapiOamMegMep],
            'direction': TapiCommonForwardingDirection
        }

        self.attribute_map = {
            'name': 'name',
            'uuid': 'uuid',
            'operational_state': 'operational-state',
            'lifecycle_state': 'lifecycle-state',
            'meg_identifier': 'meg-identifier',
            'meg_level': 'meg-level',
            'mip': 'mip',
            'layer_protocol_name': 'layer-protocol-name',
            'mep': 'mep',
            'direction': 'direction'
        }

        self._name = name
        self._uuid = uuid
        self._operational_state = operational_state
        self._lifecycle_state = lifecycle_state
        self._meg_identifier = meg_identifier
        self._meg_level = meg_level
        self._mip = mip
        self._layer_protocol_name = layer_protocol_name
        self._mep = mep
        self._direction = direction

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamOamcontextMeg':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.oamcontext.Meg of this TapiOamOamcontextMeg.  # noqa: E501
        :rtype: TapiOamOamcontextMeg
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TapiOamOamcontextMeg.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiOamOamcontextMeg.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiOamOamcontextMeg.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiOamOamcontextMeg.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this TapiOamOamcontextMeg.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this TapiOamOamcontextMeg.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TapiOamOamcontextMeg.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity.                      UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters.                      Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}                       Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this TapiOamOamcontextMeg.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def operational_state(self):
        """Gets the operational_state of this TapiOamOamcontextMeg.


        :return: The operational_state of this TapiOamOamcontextMeg.
        :rtype: TapiCommonOperationalState
        """
        return self._operational_state

    @operational_state.setter
    def operational_state(self, operational_state):
        """Sets the operational_state of this TapiOamOamcontextMeg.


        :param operational_state: The operational_state of this TapiOamOamcontextMeg.
        :type operational_state: TapiCommonOperationalState
        """

        self._operational_state = operational_state

    @property
    def lifecycle_state(self):
        """Gets the lifecycle_state of this TapiOamOamcontextMeg.


        :return: The lifecycle_state of this TapiOamOamcontextMeg.
        :rtype: TapiCommonLifecycleState
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """Sets the lifecycle_state of this TapiOamOamcontextMeg.


        :param lifecycle_state: The lifecycle_state of this TapiOamOamcontextMeg.
        :type lifecycle_state: TapiCommonLifecycleState
        """

        self._lifecycle_state = lifecycle_state

    @property
    def meg_identifier(self):
        """Gets the meg_identifier of this TapiOamOamcontextMeg.

        none  # noqa: E501

        :return: The meg_identifier of this TapiOamOamcontextMeg.
        :rtype: str
        """
        return self._meg_identifier

    @meg_identifier.setter
    def meg_identifier(self, meg_identifier):
        """Sets the meg_identifier of this TapiOamOamcontextMeg.

        none  # noqa: E501

        :param meg_identifier: The meg_identifier of this TapiOamOamcontextMeg.
        :type meg_identifier: str
        """

        self._meg_identifier = meg_identifier

    @property
    def meg_level(self):
        """Gets the meg_level of this TapiOamOamcontextMeg.

        none  # noqa: E501

        :return: The meg_level of this TapiOamOamcontextMeg.
        :rtype: int
        """
        return self._meg_level

    @meg_level.setter
    def meg_level(self, meg_level):
        """Sets the meg_level of this TapiOamOamcontextMeg.

        none  # noqa: E501

        :param meg_level: The meg_level of this TapiOamOamcontextMeg.
        :type meg_level: int
        """

        self._meg_level = meg_level

    @property
    def mip(self):
        """Gets the mip of this TapiOamOamcontextMeg.

        ME may 0, 1, or more MIPs  # noqa: E501

        :return: The mip of this TapiOamOamcontextMeg.
        :rtype: List[TapiOamMegMip]
        """
        return self._mip

    @mip.setter
    def mip(self, mip):
        """Sets the mip of this TapiOamOamcontextMeg.

        ME may 0, 1, or more MIPs  # noqa: E501

        :param mip: The mip of this TapiOamOamcontextMeg.
        :type mip: List[TapiOamMegMip]
        """

        self._mip = mip

    @property
    def layer_protocol_name(self):
        """Gets the layer_protocol_name of this TapiOamOamcontextMeg.


        :return: The layer_protocol_name of this TapiOamOamcontextMeg.
        :rtype: TapiCommonLayerProtocolName
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name):
        """Sets the layer_protocol_name of this TapiOamOamcontextMeg.


        :param layer_protocol_name: The layer_protocol_name of this TapiOamOamcontextMeg.
        :type layer_protocol_name: TapiCommonLayerProtocolName
        """

        self._layer_protocol_name = layer_protocol_name

    @property
    def mep(self):
        """Gets the mep of this TapiOamOamcontextMeg.

        1. ME may have 0 MEPs (case of transit domains where at least 1 MIP is present)                      2. ME may have 1 MEP (case of edge domaind, where the peer MEP is ouside the managed domain)                      3. ME may have 2 MEPs  # noqa: E501

        :return: The mep of this TapiOamOamcontextMeg.
        :rtype: List[TapiOamMegMep]
        """
        return self._mep

    @mep.setter
    def mep(self, mep):
        """Sets the mep of this TapiOamOamcontextMeg.

        1. ME may have 0 MEPs (case of transit domains where at least 1 MIP is present)                      2. ME may have 1 MEP (case of edge domaind, where the peer MEP is ouside the managed domain)                      3. ME may have 2 MEPs  # noqa: E501

        :param mep: The mep of this TapiOamOamcontextMeg.
        :type mep: List[TapiOamMegMep]
        """

        self._mep = mep

    @property
    def direction(self):
        """Gets the direction of this TapiOamOamcontextMeg.


        :return: The direction of this TapiOamOamcontextMeg.
        :rtype: TapiCommonForwardingDirection
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TapiOamOamcontextMeg.


        :param direction: The direction of this TapiOamOamcontextMeg.
        :type direction: TapiCommonForwardingDirection
        """

        self._direction = direction
