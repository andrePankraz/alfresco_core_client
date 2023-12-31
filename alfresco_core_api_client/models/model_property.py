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
from alfresco_core_api_client.models.constraint import Constraint
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ModelProperty(BaseModel):
    """
    ModelProperty
    """ # noqa: E501
    id: StrictStr
    title: Optional[StrictStr] = Field(default=None, description="the human-readable title")
    description: Optional[StrictStr] = Field(default=None, description="the human-readable description")
    default_value: Optional[StrictStr] = Field(default=None, description="the default value", alias="defaultValue")
    data_type: Optional[StrictStr] = Field(default=None, description="the name of the property type (e.g. d:text)", alias="dataType")
    is_multi_valued: Optional[StrictBool] = Field(default=None, description="define if the property is multi-valued", alias="isMultiValued")
    is_mandatory: Optional[StrictBool] = Field(default=None, description="define if the property is mandatory", alias="isMandatory")
    is_mandatory_enforced: Optional[StrictBool] = Field(default=None, description="define if the presence of mandatory properties is enforced", alias="isMandatoryEnforced")
    is_protected: Optional[StrictBool] = Field(default=None, description="define if the property is system maintained", alias="isProtected")
    constraints: Optional[List[Constraint]] = Field(default=None, description="list of constraints defined for the property")
    __properties: ClassVar[List[str]] = ["id", "title", "description", "defaultValue", "dataType", "isMultiValued", "isMandatory", "isMandatoryEnforced", "isProtected", "constraints"]

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
        """Create an instance of ModelProperty from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in constraints (list)
        _items = []
        if self.constraints:
            for _item in self.constraints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['constraints'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ModelProperty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "defaultValue": obj.get("defaultValue"),
            "dataType": obj.get("dataType"),
            "isMultiValued": obj.get("isMultiValued"),
            "isMandatory": obj.get("isMandatory"),
            "isMandatoryEnforced": obj.get("isMandatoryEnforced"),
            "isProtected": obj.get("isProtected"),
            "constraints": [Constraint.from_dict(_item) for _item in obj.get("constraints")] if obj.get("constraints") is not None else None
        })
        return _obj


