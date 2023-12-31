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
from alfresco_core_api_client.models.permissions_body import PermissionsBody

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class NodeBodyUpdate(BaseModel):
    """
    NodeBodyUpdate
    """  # noqa: E501

    name: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description='The name must not contain spaces or the following special characters: * " < > \\ / ? : and |. The character . must not be used at the end of the name. ',
    )
    node_type: Optional[StrictStr] = Field(default=None, alias="nodeType")
    aspect_names: Optional[List[StrictStr]] = Field(default=None, alias="aspectNames")
    properties: Optional[Dict[str, StrictStr]] = None
    permissions: Optional[PermissionsBody] = None
    __properties: ClassVar[List[str]] = [
        "name",
        "nodeType",
        "aspectNames",
        "properties",
        "permissions",
    ]

    @field_validator("name")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(
            r'^(?!(.*[\\"\*\\\>\<\?\/\:\|]+.*)|(.*[\.]?.*[\.]+$)|(.*[ ]+$))', value
        ):
            raise ValueError(
                r'must validate the regular expression /^(?!(.*[\\"\*\\\>\<\?\/\:\|]+.*)|(.*[\.]?.*[\.]+$)|(.*[ ]+$))/'
            )
        return value

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NodeBodyUpdate from a JSON string"""
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
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict["permissions"] = self.permissions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NodeBodyUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "nodeType": obj.get("nodeType"),
                "aspectNames": obj.get("aspectNames"),
                "properties": obj.get("properties"),
                "permissions": PermissionsBody.from_dict(obj.get("permissions"))
                if obj.get("permissions") is not None
                else None,
            }
        )
        return _obj
