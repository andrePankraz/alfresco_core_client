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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from alfresco_core_api_client.models.content_info import ContentInfo
from alfresco_core_api_client.models.path_info import PathInfo
from alfresco_core_api_client.models.user_info import UserInfo

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SharedLink(BaseModel):
    """
    SharedLink
    """  # noqa: E501

    id: Optional[StrictStr] = None
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")
    node_id: Optional[StrictStr] = Field(default=None, alias="nodeId")
    name: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description='The name must not contain spaces or the following special characters: * " < > \\ / ? : and |. The character . must not be used at the end of the name. ',
    )
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    modified_at: Optional[datetime] = Field(default=None, alias="modifiedAt")
    modified_by_user: Optional[UserInfo] = Field(default=None, alias="modifiedByUser")
    shared_by_user: Optional[UserInfo] = Field(default=None, alias="sharedByUser")
    content: Optional[ContentInfo] = None
    allowable_operations: Optional[List[StrictStr]] = Field(
        default=None,
        description="The allowable operations for the Quickshare link itself. See allowableOperationsOnTarget for the allowable operations pertaining to the linked content node. ",
        alias="allowableOperations",
    )
    allowable_operations_on_target: Optional[List[StrictStr]] = Field(
        default=None,
        description="The allowable operations for the content node being shared. ",
        alias="allowableOperationsOnTarget",
    )
    is_favorite: Optional[StrictBool] = Field(default=None, alias="isFavorite")
    properties: Optional[Union[str, Any]] = Field(
        default=None,
        description="A subset of the target node's properties, system properties and properties already available in the SharedLink are excluded. ",
    )
    aspect_names: Optional[List[StrictStr]] = Field(default=None, alias="aspectNames")
    path: Optional[PathInfo] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "expiresAt",
        "nodeId",
        "name",
        "title",
        "description",
        "modifiedAt",
        "modifiedByUser",
        "sharedByUser",
        "content",
        "allowableOperations",
        "allowableOperationsOnTarget",
        "isFavorite",
        "properties",
        "aspectNames",
        "path",
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
        """Create an instance of SharedLink from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of modified_by_user
        if self.modified_by_user:
            _dict["modifiedByUser"] = self.modified_by_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shared_by_user
        if self.shared_by_user:
            _dict["sharedByUser"] = self.shared_by_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict["content"] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of path
        if self.path:
            _dict["path"] = self.path.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SharedLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "expiresAt": obj.get("expiresAt"),
                "nodeId": obj.get("nodeId"),
                "name": obj.get("name"),
                "title": obj.get("title"),
                "description": obj.get("description"),
                "modifiedAt": obj.get("modifiedAt"),
                "modifiedByUser": UserInfo.from_dict(obj.get("modifiedByUser"))
                if obj.get("modifiedByUser") is not None
                else None,
                "sharedByUser": UserInfo.from_dict(obj.get("sharedByUser"))
                if obj.get("sharedByUser") is not None
                else None,
                "content": ContentInfo.from_dict(obj.get("content"))
                if obj.get("content") is not None
                else None,
                "allowableOperations": obj.get("allowableOperations"),
                "allowableOperationsOnTarget": obj.get("allowableOperationsOnTarget"),
                "isFavorite": obj.get("isFavorite"),
                "properties": obj.get("properties"),
                "aspectNames": obj.get("aspectNames"),
                "path": PathInfo.from_dict(obj.get("path"))
                if obj.get("path") is not None
                else None,
            }
        )
        return _obj
