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

def export(filename, users, overwrite=True):
    """
    Exports a csv file.

    Create a csv file and fill it with valid users. If "overwrite" is False,
    and file already exists, raise IOError
    """
    if not overwrite and os.path.exists(filename):
        raise IOError(f"'{filename}' already exists")

    valid_users = get_valid_users(users)
    write_csv(filename, valid_users)