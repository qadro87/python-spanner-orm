# python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Model for interacting with Spanner index column schema table."""

from __future__ import annotations

from spanner_orm import field
from spanner_orm.admin import schema


class IndexColumnSchema(schema.InformationSchema):
  """Model for interacting with Spanner index column schema table."""

  __table__ = 'information_schema.index_columns'
  table_catalog = field.Field(field.String, primary_key=True)
  table_schema = field.Field(field.String, primary_key=True)
  table_name = field.Field(field.String, primary_key=True)
  index_name = field.Field(field.String, primary_key=True)
  column_name = field.Field(field.String, primary_key=True)
  ordinal_position = field.Field(field.Integer, nullable=True)
  column_ordering = field.Field(field.String, nullable=True)
  is_nullable = field.Field(field.String)
  spanner_type = field.Field(field.String)
