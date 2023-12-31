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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NodeBodyLock(BaseModel):
    """
    NodeBodyLock
    """ # noqa: E501
    time_to_expire: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="timeToExpire")
    type: Optional[StrictStr] = 'ALLOW_OWNER_CHANGES'
    lifetime: Optional[StrictStr] = 'PERSISTENT'
    __properties: ClassVar[List[str]] = ["timeToExpire", "type", "lifetime"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ALLOW_OWNER_CHANGES', 'FULL'):
            raise ValueError("must be one of enum values ('ALLOW_OWNER_CHANGES', 'FULL')")
        return value

    @field_validator('lifetime')
    def lifetime_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PERSISTENT', 'EPHEMERAL'):
            raise ValueError("must be one of enum values ('PERSISTENT', 'EPHEMERAL')")
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
        """Create an instance of NodeBodyLock from a JSON string"""
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
        """Create an instance of NodeBodyLock from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timeToExpire": obj.get("timeToExpire"),
            "type": obj.get("type") if obj.get("type") is not None else 'ALLOW_OWNER_CHANGES',
            "lifetime": obj.get("lifetime") if obj.get("lifetime") is not None else 'PERSISTENT'
        })
        return _obj


