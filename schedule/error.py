from datetime import datetime
from ujson import dumps

from django.http import HttpResponse

class Error:
    @classmethod
    def _error(cls, code, reason, data=None):
        return HttpResponse(dumps({'status_code': code,
                                   'reason': reason,
                                   'data': [data]}))

    @classmethod
    def debug(cls, obj):
       return HttpResponse(str(obj))

    @classmethod
    def http405(cls):
        http = HttpResponse()
        http.status_code = 405
        return http
