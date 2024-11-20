from django.shortcuts import render, redirect

from zxl import models
from zxl.utils.form import UserModelForm
from zxl.utils.pagenation import pagination


# 用户列表
def user_list(request):
    data_dict = {}
    search_data = request.GET.get('user', "")
    if search_data:
        data_dict['name__contains'] = search_data
    user = models.userinfo.objects.filter(**data_dict)


    # 分页
    page_object = pagination(request, user)
    context = {'user': page_object.page_queryset,
               'page_string': page_object.html()
               }

    # 获得数据列表
    return render(request, 'user/user_list.html', context)


# 用户添加
def user_add(request):
    if request.method == 'GET':
        context = {
            'gender_choices': models.userinfo.gender_choices,
            'depart_list': models.department.objects.all()
        }
        return render(request, 'user/user_add.html', context)
    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    account = request.POST.get('account')
    create_time = request.POST.get('create_time')
    gender = request.POST.get('gender')
    depart_id = request.POST.get('depart_id')

    models.userinfo.objects.create(name=name, password=password, age=age, account=account, create_time=create_time,
                                   gender=gender, depart_id=depart_id)
    return redirect('http://127.0.0.1:8000/user/list/')


# 用户删除
def user_delete(request):
    id = request.GET.get('id')
    models.userinfo.objects.filter(id=id).delete()
    return redirect('http://127.0.0.1:8000/user/list/')


# 用户编辑
def user_update(request, nid):
    if request.method == 'GET':
        context = {
            'gender_choices': models.userinfo.gender_choices,
            'depart_list': models.department.objects.all()
        }

        rwo = models.userinfo.objects.filter(id=nid).first()
        return render(request, 'user/user_update.html', {'row': rwo, **context})
    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    account = request.POST.get('account')
    create_time = request.POST.get('create_time')
    gender = request.POST.get('gender')
    depart_id = request.POST.get('depart_id')
    models.userinfo.objects.filter(id=nid).update(name=name, password=password, age=age, account=account,
                                                  create_time=create_time, gender=gender, depart_id=depart_id)

    return redirect('http://127.0.0.1:8000/user/list/')


###############################  modelform实列  ############################################


# 用户添加modelform
def user_modelformadd(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user/user_modelformadd.html', {'form': form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 数据验证成功
        form.save()
        # 存储到数据库
        print(form.cleaned_data)
        return redirect('http://127.0.0.1:8000/user/list/')
    else:
        # 数据验证失败
        # print(form.errors)
        return render(request, 'user/user_modelformadd.html', {'form': form})


# 用户编辑modelform
def user_modelformupdate(request, nid):
    if request.method == 'GET':
        row = models.userinfo.objects.filter(id=nid).first()
        form = UserModelForm(instance=row)
        return render(request, 'user/user_modelformupdate.html', {'form': form})
    form = UserModelForm(data=request.POST, instance=models.userinfo.objects.filter(id=nid).first())
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/user/list/')
    else:
        return render(request, 'user/user_modelformupdate.html', {'form': form})
