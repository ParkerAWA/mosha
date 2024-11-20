from django.shortcuts import render, redirect

from zxl import models
from zxl.utils.form import numberModelForm
from zxl.utils.pagenation import pagination


# 号码列表/搜素功能/分页功能
def number_list(request, ):
    # for i in range(100):
    #     models.number.objects.create(mobile=15755994023 , leve=1, status=1, price=100)

    # 检测用户是否登录，用户发来请求，获取cookie随机字符串，再用随机字符串到session中比对是否存在

    data_dict = {}
    search_data = request.GET.get('number', "")
    if search_data:
        data_dict['mobile__contains'] = search_data

    queryset = models.number.objects.filter(**data_dict).order_by('-leve')
    # 分页导入组件
    page_object = pagination(request, queryset)
    context = {'queryset': page_object.page_queryset,
               # 分页数据
               'search_data': search_data,
               'page_string': page_object.html()
               # 页码
               }

    return render(request, 'number_list.html', context)


# 号码删除
def number_delete(request):
    id = request.GET.get('id')
    models.number.objects.filter(id=id).delete()
    return redirect('http://127.0.0.1:8000/number/list/')


#############################modelform实列############################################


# 号码添加modelform
def number_modelformadd(request):
    if request.method == 'GET':
        form = numberModelForm()
        return render(request, 'number_modelformadd.html', {'form': form})
    form = numberModelForm(data=request.POST)
    if form.is_valid():
        # 数据验证成功
        form.save()
        # 存储到数据库
        print(form.cleaned_data)
        return redirect('http://127.0.0.1:8000/number/list/')
    else:
        # 数据验证失败
        # print(form.errors)
        return render(request, 'number_modelformadd.html', {'form': form})


# 号码编辑modelform
def number_modelformupdate(request, nid):
    if request.method == 'GET':
        row = models.number.objects.filter(id=nid).first()
        form = numberModelForm(instance=row)
        return render(request, 'number_modelformupdate.html', {'form': form})
    form = numberModelForm(data=request.POST, instance=models.number.objects.filter(id=nid).first())
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/number/list/')
    else:
        return render(request, 'number_modelformupdate.html', {'form': form})
