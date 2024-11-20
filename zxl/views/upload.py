from django import forms
from django.shortcuts import render, HttpResponse
from zxl.utils.bootstrap import BootstrapForm, BootstrapModelForm
from zxl import models
import os
from django.conf import settings


def upload_list(request):
    """
    上传文件列表
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'upload/upload_list.html')

    file_object = request.FILES.get('file')

    f = open(file_object.name, 'wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse('ok')


class UploadForm(BootstrapForm):
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.ImageField(label="头像")
    # 去除bootstrap样式
    bootstrap_exclude_fields = ['img']


class UploadModelForm(BootstrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.city
        fields = ['name', 'count', 'img']


# 上传文件表单
def upload_form(request):
    title = '上传个人信息'
    if request.method == 'GET':
        form = UploadForm()
        return render(request, 'upload/upload_form.html', {'form': form, 'title': title})
    form = UploadForm(data=request.POST, files=request.FILES)
    if form.is_valid():

        # 1.读取图片内容，存储到文件中并获取文件路径
        img_object = form.cleaned_data.get('img')

        # media_path = os.path.join(settings.MEDIA_ROOT, img_object.name)----绝对路径
        media_path = os.path.join('media', img_object.name)
        # 相对路径

        f = open(media_path, mode='wb')
        for chunk in img_object.chunks():
            f.write(chunk)
        f.close()

        # 2.将文件路径存储到数据库中
        models.boos.objects.create(name=form.cleaned_data['img'], age=form.cleaned_data['age'], img=media_path)
        return HttpResponse('ok')
    else:
        return render(request, 'upload/upload_form.html', {'form': form, 'title': title})


# 上传文件表单ModelForm
def upload_ModelForm(request):
    title = '上传个人信息'
    if request.method == 'GET':
        form = UploadModelForm()
        return render(request, 'upload/upload_ModelForm.html', {'form': form, 'title': title})
    form = UploadModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        # 自动将文件保存
        # 字段+路劲写入到数据库

        return HttpResponse('ok')

    return render(request, 'upload/upload_ModelForm.html', {'form': form, 'title': title})

