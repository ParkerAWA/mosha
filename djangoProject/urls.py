"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from zxl.views import depart, user, number, admin, account, task, order, echarts, upload, city, test

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

    # 部门管理
    path('department/list/', depart.department_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/update/', depart.depart_update),
    path('depart/upload/', depart.depart_upload),
    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/delete/', user.user_delete),
    path('user/<int:nid>/update/', user.user_update),
    path('user/modelformadd/', user.user_modelformadd),
    path('user/<int:nid>/modelformupdate/', user.user_modelformupdate),
    # 号码管理
    path('number/list/', number.number_list),
    path('number/delete/', number.number_delete),
    path('number/modelformadd/', number.number_modelformadd),
    path('number/<int:nid>/modelformupdate/', number.number_modelformupdate),
    # 管理员
    path('admin/list/', admin.admin_list),
    path('admin/delete/', admin.admin_delete),
    path('admin/<int:nid>/update/', admin.admin_update),
    path('admin/modelformadd/', admin.admin_modelformadd),
    path('admin/<int:nid>/password/', admin.admin_password),
    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    # 验证码
    path('image/code/', account.image_code),
    # 主页面
    path('main/', account.main),
    # 任务管理
    path('task/list/', task.task_list),
    path('task/ajax/', task.task_ajax),
    path('task/add/', task.task_add),
    path('task/delete/', task.task_delete),

    # 订单
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    # 获取订单信息
    path('order/update/', order.order_update),
    # 订单编辑
    path('order/edit/', order.order_edit),
    # 数据统计
    path('echarts/list/', echarts.echarts_list),
    path('echarts/bar/', echarts.echarts_bar),
    path('echarts/pie/', echarts.echarts_pie),
    path('echarts/line/', echarts.echarts_line),
    # 文件上传
    path('upload/list/', upload.upload_list),
    path('upload/form/', upload.upload_form),
    path('upload/ModelForm/', upload.upload_ModelForm),
    # 城市
    path('city/list/', city.city_list),
    path('city/add/', city.city_add),
    # 测试
    path('test/list/', test.test_list),
    path('test/add/', test.test_add),
    path('test/delete/', test.test_delete),
    path('test/<int:nid>/update/', test.test_update),

]
