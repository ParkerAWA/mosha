import json

from django import forms
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt

from zxl import models
from zxl.utils.bootstrap import BootstrapModelForm
from zxl.utils.pagenation import pagination


class taskModelForm(BootstrapModelForm):
    # title = forms.CharField(label='任务名称', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # create_time = forms.DateField(label='创建时间', widget=forms.DateInput(attrs={'type': 'date'}))
    create_time = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    content = forms.CharField(label='任务内容', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.task
        # fields = ['title', 'content', 'create_time', 'level', 'status', 'user']
        fields = '__all__'


# 任务列表
def task_list(request):
    data_dict = {}
    search_data = request.GET.get('title', "")
    if search_data:
        data_dict['title__contains'] = search_data

    queryset = models.task.objects.filter(**data_dict)
    form = taskModelForm()

    page_object = pagination(request, queryset)
    context = {'queryset': page_object.page_queryset,
               # 分页数据
               'page_string': page_object.html(),
               # 页码
               'form': form,
               }

    return render(request, 'task_list.html', context)


@csrf_exempt
# 免除csrf验证,在发送post请求时，不需要csrf验证,否则会报错
def task_ajax(request):
    print(request.GET)
    print(request.POST)

    data_dict = {"status": True, "data": [11, 22, 33, 44]}
    json_string = json.dumps(data_dict)
    # 将一个Python字典data_dict转换成一个JSON格式的字符串json_string。

    return HttpResponse(json_string)


@csrf_exempt
def task_add(request):
    print(request.POST)
    form = taskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        # return HttpResponse(json.dumps(data_dict))
        return JsonResponse(data_dict)
    data_dict = {"status": False, "error": form.errors}
    # return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})


def task_delete(request):
    uid = request.GET.get('uid')
    exists = models.task.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "数据不存在"})
    models.task.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})
