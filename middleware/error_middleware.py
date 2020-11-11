import logging

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from fund_server import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class CollectionAllErrorMiddleware(MiddlewareMixin):
    """
    拦截所有异常错误
    """

    @staticmethod
    def process_exception(request, exception):
        logger.error(f"path: {request.path}, method: {request.method}, error info: {exception}")
        return HttpResponse("server error")
