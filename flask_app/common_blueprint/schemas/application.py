from marshmallow import Schema, fields


class GetApplicationSchema(Schema):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    arrangement_id = fields.Integer(required=True)
    request_status = fields.Integer(required=True)
