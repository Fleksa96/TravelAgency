from marshmallow import Schema, fields


class UserMinimalSchema(Schema):
    id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)


class GetArrangementSchema(Schema):
    id = fields.Integer(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.String(required=True)
    destination = fields.String(required=True)
    price = fields.Float(required=True)
    free_places = fields.Integer(required=True)
    admin = fields.Nested(UserMinimalSchema)
    tourist_guide = fields.Nested(UserMinimalSchema)
