# -*- coding: utf-8 -*-
import json
import logging
import traceback

from django.http import Http404

from . import json_response
from .error import BaseError, UnknownError

logger = logging.getLogger('django')

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class ExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):

        # exception white list

        if issubclass(exception.__class__, Http404):
            return

        logger.error('Exception: {method} {url} param: {param}\n{traceback}'.format(
            url=request.path, method=request.method, param=json.dumps(getattr(request, request.method, {})),
            traceback=traceback.format_exc()
        ))

        if not issubclass(exception.__class__, BaseError):
            return json_response.error(UnknownError)

        return json_response.error(exception, exception.data)
