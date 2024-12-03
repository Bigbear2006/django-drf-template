import logging

from django.db import connection
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.response import Response

logger = logging.getLogger('queries')


class QueriesLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        response: Response = self.get_response(request)
        logger.info(
            f'"{request.method} {request.path} {response.status_code}" '
            f'ran {len(connection.queries)} queries',
        )
        for query in connection.queries:
            logger.info(f'({query["time"]}) {query["sql"]}')
        return response
