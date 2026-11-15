import os
import csv
from copy import deepcopy
# Third party libraries
from marshmallow import Schema, fields, pre_load
from marshmallow.validate import Length, Range

class UserSchema(Schema):
    """
    Requests a *valid* user.
    """
    email = fields.Email(required=True)
    name = fields.Str(required=True, validate=Length(min=1))
    age = fields.Int(required=True, validate=Range(min=18, max=65))
    role = fields.Str()

    @pre_load
    def strip_name(self, data, **kwargs):
        data_copy = deepcopy(data)
        try:
            data_copy["name"] = data_copy["name"].strip()
        except (AttributeError, KeyError, TypeError):
            pass
        return data_copy

schema = UserSchema()