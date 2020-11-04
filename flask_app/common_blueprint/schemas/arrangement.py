from marshmallow import Schema, fields, validates, validates_schema, \
    ValidationError
from werkzeug.exceptions import Conflict
from datetime import date


class GetRequestStatusSchema(Schema):
    id = fields.Integer(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    destination = fields.String(required=True)
    travel_guide_id = fields.Integer(required=True)


class GetGuideArrangementSchema(Schema):
    arrangement = fields.Nested(GetRequestStatusSchema)
    request_status = fields.Integer(required=True)


class ArrangementMinimalSchema(Schema):
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.String(required=True)
    destination = fields.String(required=True)


class GetArrangementSchema(Schema):
    id = fields.Integer(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.String(required=True)
    destination = fields.String(required=True)
    price = fields.Float(required=True)
    free_places = fields.Integer(required=True)
    admin_id = fields.Integer(required=True)
    travel_guide_id = fields.Integer(required=True)


class UpdateArrangementSchema(Schema):
    start_date = fields.Date()
    end_date = fields.Date()
    price = fields.Float()
    free_places = fields.Integer()
    travel_guide_id = fields.Integer()

    # @validates('start_date')
    # def check_if_start_date_is_in_future(self, start_date):
    #     if start_date and start_date < date.today():
    #         raise Conflict(description='Start date is in past')
    #
    # @validates_schema
    # def validate_numbers(self, data, **kwargs):
    #     if data.get('end_date') and data.get('start_date') \
    #             and data.get('end_date') < data.get('start_date'):
    #         raise Conflict(description='End date is before ' \
    #                                    'start date')


class CreateArrangementSchema(Schema):
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.String(required=True)
    destination = fields.String(required=True)
    price = fields.Float(required=True)
    free_places = fields.Integer(required=True)
    admin_id = fields.Integer(required=True)
    travel_guide_id = fields.Integer()

    @validates('start_date')
    def check_if_start_date_is_in_future(self, start_date):
        if start_date < date.today():
            raise Conflict(description='Start date is in past')

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        if data["end_date"] < data["start_date"]:
            raise Conflict(description='End date is before ' \
                                       'start date')
