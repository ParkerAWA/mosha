from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect, render


# 检测用户是否登录，用户发来请求，获取cookie随机字符串，再用随机字符串到session中比对是否存在
# info = request.session.get('info')
# print(info)
# if not info:
#     return redirect('http://127.0.0.1:8000/login/')

# 如果没有返回值（返回None），则继续执行下一个中间件，
# 如果返回值，则直接返回
# return HttpResponse('无权限访问')
# return redirect('http://127.0.0.1:8000/login/')
# return render(request, 'login.html')

class auth(MiddlewareMixin):
    """
    中间件1
    """
    def process_request(self, request):
        # 排除不用登录就可以使用的页面
        # request.path_info 获取当前用户请求的url
        if request.path_info in ['/login/', '/main/', '/image/code/', ]:
            return None

        info_dict = request.session.get('info')
        # 读取用户的session信息，读取成功，证明已登录，继续执行
        if info_dict:
            return None
        else:
            return redirect('http://127.0.0.1:8000/login/')
