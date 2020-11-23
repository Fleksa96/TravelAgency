from marshmallow import Schema, fields, validates_schema
from werkzeug.exceptions import Conflict


class ReservationSchema(Schema):
    number_of_reservations = fields.Integer(required=True, allow_none=False)

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        if data.get('number_of_reservations') < 1:
            raise Conflict(
                description='Number of reservations has to be '
                            'bigger than 0'
            )


class GetReservationSchema(Schema):
    id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    arrangement_id = fields.Integer(required=True)
    num_of_places = fields.Integer(required=True)
    price = fields.Float(required=True)
