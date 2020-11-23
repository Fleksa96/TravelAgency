from marshmallow import Schema, fields, validates_schema, ValidationError
from werkzeug.exceptions import Conflict


class CreateUserSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)
    email = fields.Email(required=True)
    user_type = fields.Integer(required=True)

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        if data.get("password") != data.get("confirm_password"):
            raise Conflict(
                description='Password and confirm password field differs'
            )


class RegistrationUserSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)
    email = fields.Email(required=True)
    user_type = fields.Integer(required=False)

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        if data.get("password") != data.get("confirm_password"):
            raise Conflict(
                description='Password and confirm password field differs'
            )


class UpdateUserSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    username = fields.String()
    password = fields.String()
    confirm_password = fields.String()
    email = fields.Email()

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        if data.get("password") is not None and \
                data.get("confirm_password") is None:
            raise Conflict(
                description='You need to enter password confirmation'
            )
        if data.get("password") is None and \
                data.get("confirm_password") is not None:
            raise Conflict(
                description='You need to enter password first'
            )


class GetUserSchema(Schema):
    id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)
    user_type = fields.Integer(required=True)


class UserLoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class UserMinimalSchema(Schema):
    id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
