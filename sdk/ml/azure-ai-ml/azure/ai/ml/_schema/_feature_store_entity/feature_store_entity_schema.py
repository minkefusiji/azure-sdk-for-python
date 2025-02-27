# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------


from marshmallow import fields, validate

from azure.ai.ml._schema import NestedField
from azure.ai.ml._schema.core.schema import YamlFileSchema

from .data_column_schema import DataColumnSchema


class FeatureStoreEntitySchema(YamlFileSchema):
    name = fields.Str(required=True, allow_none=False)
    version = fields.Str(required=True, allow_none=False)
    index_columns = fields.List(NestedField(DataColumnSchema), required=True, allow_none=False)
    stage = fields.Str(validate=validate.OneOf(["Development", "Production", "Archived"]), dump_default="Development")
    description = fields.Str()
    tags = fields.Dict(keys=fields.Str(), values=fields.Str())
    properties = fields.Dict(keys=fields.Str(), values=fields.Str())
