from django.shortcuts import render, redirect

from zxl import models
from zxl.utils.form import adminModelForm, admin2ModelForm, admin3ModelForm, testModelForm
from zxl.utils.pagenation import pagination


# 测试列表
def test_list(request):
    data_dict = {}
    search_data = request.GET.get('test', "")
    if search_data:
        data_dict['username__contains'] = search_data

    test = models.test.objects.filter(**data_dict)

    # 分页
    page_object = pagination(request, test)
    context = {
        'test': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data  # 将搜索数据传递回模板
    }

    # 获得数据列表
    return render(request, 'test/test_list.html', context)


# 新建
def test_add(request):
    if request.method == 'GET':
        form = testModelForm()
        return render(request, 'test/test_add.html', {'form': form, 'title': '添加测试'})
    form = testModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/test/list/')
    else:
        return render(request, 'test/test_add.html', {'error_msg': '不能为空'})


# 删除
def test_delete(request):
    id = request.GET.get('id')
    models.test.objects.filter(id=id).delete()
    return redirect('http://127.0.0.1:8000/test/list/')


# 修改
def test_update(request, nid):
    if request.method == 'GET':
        row = models.test.objects.filter(id=nid).first()
        form = testModelForm(instance=row)
        return render(request, 'test/test_update.html', {'form': form})
    form = testModelForm(data=request.POST, instance=models.test.objects.filter(id=nid).first())
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/test/list/')
    else:
        return render(request, 'test/test_update.html', {'form': form})
