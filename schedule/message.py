from django.http import HttpResponse
from ujson import dumps, loads

class Message:
    @classmethod
    def _msg(cls, status_code, reason, data=None):
        return HttpResponse(dumps({'status_code': status_code,
                                   'reason': reason,
                                   'data': [data]}))

    @classmethod
    def object_created(cls, id):
        status_code = 201
        reason = 'object created successfully'
        data = {'id': id}
        return cls._msg(status_code,
                        reason,
                        data)

    @classmethod
    def object_updated(cls, id):
        status_code = 201
        reason = 'object updated successfully'
        data = {'id': id}
        return cls._msg(status_code,
                        reason,
                        data)
