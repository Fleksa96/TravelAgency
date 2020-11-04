from marshmallow import Schema, fields


class CreateApplicationSchema(Schema):
    arrangement_id = fields.Integer(required=True)


class GetApplicationSchema(Schema):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    arrangement_id = fields.Integer(required=True)
