from django.shortcuts import render, redirect

from zxl import models
from zxl.utils.form import adminModelForm, admin2ModelForm, admin3ModelForm
from zxl.utils.pagenation import pagination


# 管理员列表
def admin_list(request):
    data_dict = {}
    search_data = request.GET.get('admin', "")
    if search_data:
        data_dict['username__contains'] = search_data
    admin = models.admin.objects.filter(**data_dict)
    # filter(**data_dict).order_by('-id')------条件和排序

    page_object = pagination(request, admin)
    context = {
        'admin': page_object.page_queryset,
        'page_string': page_object.html(),

    }
    return render(request, 'admin/admin_list.html', context)


# 管理员添加
def admin_modelformadd(request):
    if request.method == 'GET':
        form = adminModelForm()
        return render(request, 'admin/admin_modelformadd.html', {'form': form, 'title': '添加管理员'})
    form = adminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/admin/list/')
    else:
        return render(request, 'admin/admin_modelformadd.html', {'form': form})


# 管理员删除
def admin_delete(request):
    nid = request.GET.get('id')
    models.admin.objects.filter(id=nid).delete()
    return redirect('http://127.0.0.1:8000/admin/list/')


# 管理员编辑
def admin_update(request, nid):
    title = '编辑管理员'
    if request.method == 'GET':
        admin = models.admin.objects.filter(id=nid).first()
        if not admin:
            return redirect('http://127.0.0.1:8000/admin/list/')
        form = admin3ModelForm(instance=admin)
        return render(request, 'ADD.html', {'form': form, 'title': title, })
    form = admin3ModelForm(data=request.POST, instance=models.admin.objects.filter(id=nid).first())
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/admin/list/')
    else:
        return render(request, 'ADD.html', {'form': form, 'title': title})


# 密码重置
def admin_password(request, nid):
    row_object = models.admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('http://127.0.0.1:8000/admin/list/')
    title = '重置密码----{}'.format(row_object.username)

    if request.method == 'GET':
        form = admin2ModelForm()
        return render(request, 'ADD.html', {'form': form, 'title': title})
    form = admin2ModelForm(data=request.POST, instance=row_object)

    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/admin/list/')
    else:

        return render(request, 'ADD.html', {'form': form, 'title': title})

    # admin = models.admin.objects.filter(id=nid).first()
    # form = admin2ModelForm(instance=admin)
    # title = '重置密码----{}'.format(admin.username)
    #
    # return render(request, 'ADD.html', {'form': form, 'title': title, 'admin': admin})
