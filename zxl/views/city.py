from django.shortcuts import render, redirect

from zxl import models
from zxl.utils.bootstrap import BootstrapModelForm


def city_list(request):
    city_list = models.city.objects.all()
    return render(request, 'city_list.html', {'city_list': city_list})


class CityModelForm(BootstrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.city
        fields = ['name', 'count', 'img']


def city_add(request):
    title = '新建城市'
    if request.method == 'GET':
        form = CityModelForm()
        return render(request, 'city_add.html', {'form': form, 'title': title})
    form = CityModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        # 自动将文件保存
        # 字段+路劲写入到数据库

        return redirect('http://127.0.0.1:8000/city/list/')

    return render(request, 'upload/upload_ModelForm.html', {'form': form, 'title': title})
