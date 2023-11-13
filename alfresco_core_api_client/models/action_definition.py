# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services. 

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from alfresco_core_api_client.models.action_parameter_definition import ActionParameterDefinition
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ActionDefinition(BaseModel):
    """
    ActionDefinition
    """ # noqa: E501
    id: StrictStr = Field(description="Identifier of the action definition — used for example when executing an action")
    name: Optional[StrictStr] = Field(default=None, description="name of the action definition, e.g. \"move\"")
    title: Optional[StrictStr] = Field(default=None, description="title of the action definition, e.g. \"Move\"")
    description: Optional[StrictStr] = Field(default=None, description="describes the action definition, e.g. \"This will move the matched item to another space.\"")
    applicable_types: List[StrictStr] = Field(description="QNames of the types this action applies to", alias="applicableTypes")
    track_status: StrictBool = Field(description="whether the basic action definition supports action tracking or not", alias="trackStatus")
    parameter_definitions: Optional[List[ActionParameterDefinition]] = Field(default=None, alias="parameterDefinitions")
    __properties: ClassVar[List[str]] = ["id", "name", "title", "description", "applicableTypes", "trackStatus", "parameterDefinitions"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ActionDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in parameter_definitions (list)
        _items = []
        if self.parameter_definitions:
            for _item in self.parameter_definitions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameterDefinitions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ActionDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "applicableTypes": obj.get("applicableTypes"),
            "trackStatus": obj.get("trackStatus"),
            "parameterDefinitions": [ActionParameterDefinition.from_dict(_item) for _item in obj.get("parameterDefinitions")] if obj.get("parameterDefinitions") is not None else None
        })
        return _obj

