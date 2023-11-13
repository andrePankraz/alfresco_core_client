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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Favorite(BaseModel):
    """
    A favorite describes an Alfresco entity that a person has marked as a favorite. The target can be a site, file or folder. 
    """ # noqa: E501
    target_guid: StrictStr = Field(description="The guid of the object that is a favorite.", alias="targetGuid")
    created_at: Optional[datetime] = Field(default=None, description="The time the object was made a favorite.", alias="createdAt")
    target: Union[str, Any]
    properties: Optional[Union[str, Any]] = Field(default=None, description="A subset of the target favorite properties, system properties and properties already available in the target are excluded.")
    allowable_operations: Optional[List[StrictStr]] = Field(default=None, description="The allowable operations for the target.", alias="allowableOperations")
    __properties: ClassVar[List[str]] = ["targetGuid", "createdAt", "target", "properties", "allowableOperations"]

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
        """Create an instance of Favorite from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Favorite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "targetGuid": obj.get("targetGuid"),
            "createdAt": obj.get("createdAt"),
            "target": obj.get("target"),
            "properties": obj.get("properties"),
            "allowableOperations": obj.get("allowableOperations")
        })
        return _obj


