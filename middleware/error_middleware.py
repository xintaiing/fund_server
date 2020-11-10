import logging

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from fund_server import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class CollectionAllErrorMiddleware(MiddlewareMixin):
    """
    拦截所有异常错误
    """

    def process_exception(self, exception):
        logger.error(exception)
        return HttpResponse("error")
