#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# coding: utf-8

"""
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ViewPrivilege(str, Enum):
    """
    ViewPrivilege
    """

    """
    allowed enum values
    """
    CATALOG_MANAGE_ACCESS = 'CATALOG_MANAGE_ACCESS'
    VIEW_DROP = 'VIEW_DROP'
    VIEW_LIST = 'VIEW_LIST'
    VIEW_READ_PROPERTIES = 'VIEW_READ_PROPERTIES'
    VIEW_WRITE_PROPERTIES = 'VIEW_WRITE_PROPERTIES'
    VIEW_FULL_METADATA = 'VIEW_FULL_METADATA'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ViewPrivilege from a JSON string"""
        return cls(json.loads(json_str))


