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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from alfresco_core_api_client.models.simple_condition_definition import SimpleConditionDefinition
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CompositeConditionDefinition(BaseModel):
    """
    CompositeConditionDefinition
    """ # noqa: E501
    inverted: Optional[StrictBool] = Field(default=False, description="Whether to invert the logic for this condition (if true then \"not\" is applied to the whole condition)")
    boolean_mode: Optional[StrictStr] = Field(default='and', description="How to combine the clauses of this condition (\"and\" or \"or\")", alias="booleanMode")
    composite_conditions: Optional[List[CompositeConditionDefinition]] = Field(default=None, description="Nested list of composite clauses in this condition", alias="compositeConditions")
    simple_conditions: Optional[List[SimpleConditionDefinition]] = Field(default=None, description="Nested list of simple (per field) conditions.", alias="simpleConditions")
    __properties: ClassVar[List[str]] = ["inverted", "booleanMode", "compositeConditions", "simpleConditions"]

    @field_validator('boolean_mode')
    def boolean_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('and', 'or'):
            raise ValueError("must be one of enum values ('and', 'or')")
        return value

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
        """Create an instance of CompositeConditionDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in composite_conditions (list)
        _items = []
        if self.composite_conditions:
            for _item in self.composite_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['compositeConditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in simple_conditions (list)
        _items = []
        if self.simple_conditions:
            for _item in self.simple_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['simpleConditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CompositeConditionDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inverted": obj.get("inverted") if obj.get("inverted") is not None else False,
            "booleanMode": obj.get("booleanMode") if obj.get("booleanMode") is not None else 'and',
            "compositeConditions": [CompositeConditionDefinition.from_dict(_item) for _item in obj.get("compositeConditions")] if obj.get("compositeConditions") is not None else None,
            "simpleConditions": [SimpleConditionDefinition.from_dict(_item) for _item in obj.get("simpleConditions")] if obj.get("simpleConditions") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
CompositeConditionDefinition.model_rebuild(raise_errors=False)

