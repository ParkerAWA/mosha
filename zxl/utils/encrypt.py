from django.conf import settings

import hashlib


def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    # settings.SECRET_KEY对密码加密进行加盐
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()

# 中间件是一个类，它必须实现一个process_request()方法，该方法接收一个HttpRequest对象，返回一个HttpResponse对象。
