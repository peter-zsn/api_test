import traceback
import logging
import json
from django.http import Http404, HttpRequest, HttpResponse

from libs.utils import ajax


log = logging.getLogger(__name__)


class AuthenticationMiddleware(object):

    def process_request(self, request):
        try:
            return self._process_request(request)
        except:
            exc = traceback.format_exc()
            log.error(exc)

    def _process_request(self, request):
        # REQUEST过期, 使用QUERY代替
        query = request.GET.copy()
        query.update(request.POST)
        # 把body参数合并到QUERY
        try:
            body = json.loads(request.body)
            query.update(body)
        except:
            pass
        request.QUERY = query
        r = self.cross_domain(request)
        if r:
            return r

    def cross_domain(self, request, response=None):
        """添加跨域头"""
        origin = request.META.get('HTTP_ORIGIN', '*')
        if request.method == 'OPTIONS' and not response:
            response = HttpResponse()
        if not response:
            return
        response['Access-Control-Allow-Origin'] = origin
        response['Access-Control-Allow-Methods'] = 'GET,POST'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        response['Access-Control-Max-Age'] = '1728000'
        return response

    def process_response(self, request, response):
        self.cross_domain(request, response)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return

        exc = traceback.format_exc()
        log.error(exc)

        r = ajax.ajax_fail(request, message="抱歉，服务器开小差了，请联系客服12556185")
        r.status_code = 500
        return r