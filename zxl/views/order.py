from django.shortcuts import render, redirect, HttpResponse

from zxl import models
from zxl.utils.bootstrap import BootstrapModelForm
from zxl.utils.pagenation import pagination
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
from datetime import datetime


class orderModelForm(BootstrapModelForm):
    class Meta:
        model = models.order
        # fields = '__all__'
        exclude = ['oid', 'admin']
        # 排除字段


# 订单列表
def order_list(request):
    data_dict = {}
    search_data = request.GET.get('title', "")
    if search_data:
        data_dict['title__contains'] = search_data

    queryset = models.order.objects.filter(**data_dict)
    page_object = pagination(request, queryset)
    form = orderModelForm()
    context = {
        'form': form,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html()
    }

    return render(request, 'order_list.html', context)


# 订单添加
@csrf_exempt
def order_add(request):
    form = orderModelForm(data=request.POST)
    if form.is_valid():
        # 设置订单号
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        # 设置订单管理员
        form.instance.admin_id = request.session['info']['id']
        form.save()
        data_dict = {"status": True}
        # return HttpResponse(json.dumps(data_dict))
        return JsonResponse(data_dict)
    data_dict = {"status": False, "error": form.errors}
    # return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})


# 订单删除
def order_delete(request):
    uid = request.GET.get('uid')
    exists = models.order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    models.order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


# 订单信息获取
def order_update(request):
    uid = request.GET.get('uid')
    row_dict = models.order.objects.filter(id=uid).values('title', 'price', 'status').first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
    result = {
        'status': True,
        'data': row_dict,
        # 'data': {'title': row_object.title,
        #          'price': row_object.price,
        #          'status': row_object.status, }

    }
    return JsonResponse(result)


# 订单修改
@csrf_exempt
def order_edit(request):
    uid = request.GET.get('uid')
    row_object = models.order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在"})
    form = orderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})
