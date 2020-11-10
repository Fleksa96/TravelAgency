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
