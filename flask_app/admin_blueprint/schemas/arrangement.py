from marshmallow import Schema, fields


class GetArrangementSchema(Schema):
    id = fields.Integer(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.String(required=True)
    destination = fields.String(required=True)
    price = fields.Float(required=True)
    free_places = fields.Integer(required=True)
    admin_id = fields.Integer(required=True)
    tourist_guide_id = fields.Integer(required=True)


class CreateArrangementSchema(Schema):
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.String(required=True)
    destination = fields.String(required=True)
    price = fields.Float(required=True)
    free_places = fields.Integer(required=True)
    admin_id = fields.Integer(required=True)
    tourist_guide_id = fields.Integer(required=True)
