from marshmallow import Schema, fields


class CreateUserSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)


class GetUserSchema(Schema):
    id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.String(required=True)
    user_type = fields.String(required=True)


class UserLoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class UserMinimalSchema(Schema):
    id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)