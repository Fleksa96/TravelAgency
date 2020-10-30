import sys
import traceback
from werkzeug.exceptions import (NotFound,
                                 Forbidden,
                                 Unauthorized,
                                 BadRequest,
                                 Conflict,
                                 UnprocessableEntity)
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from marshmallow import ValidationError
from flask import Response, current_app
from json import dumps

from flask_app.error_handler import error_handler


def report_error(error):
    current_app.logger.exception(error)


@error_handler.app_errorhandler(Forbidden)
def forbidden_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': "You don't have permission "
                                      "to access the requested resource."}),
                    error.code)


@error_handler.app_errorhandler(NotFound)
def not_found_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': error.description}), error.code)


@error_handler.app_errorhandler(BadRequest)
def not_found_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': error.description}), error.code)


@error_handler.app_errorhandler(Conflict)
def not_found_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': error.description}), error.code)


@error_handler.app_errorhandler(MultipleResultsFound)
def multiple_results_found_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': 'Multiple results error.'}), 422)


@error_handler.app_errorhandler(NoResultFound)
def no_result_found_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': 'No result found error.'}), 422)


@error_handler.app_errorhandler(KeyError)
def error_key(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': 'Key error.'}), 400)


@error_handler.app_errorhandler(Unauthorized)
def error_key(error):
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': 'Unauthorized.'}), error.code)


@error_handler.app_errorhandler(ValueError)
def value_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': 'Value error.'}), 400)


@error_handler.app_errorhandler(ValidationError)
def validation_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': 'Validation error.'}), 400)


@error_handler.app_errorhandler(UnprocessableEntity)
def validation_error(error):
    report_error(error)
    if hasattr(error, 'response') and error.response is not None:
        return Response(dumps(error.response), error.code)
    return Response(dumps({'message': error.description}), error.code)


@error_handler.app_errorhandler(Exception)
def error_not_found(error):
    report_error(error)
    return Response(dumps({'message': 'Oops! Something went wrong.'}), 500)
