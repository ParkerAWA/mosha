from io import BytesIO

from django import forms
from django.shortcuts import render, redirect, HttpResponse

from zxl import models
from zxl.utils.code import check_code
from zxl.utils.encrypt import md5


class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': '用户名不能为空'}
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True),
        error_messages={'required': '密码不能为空'}
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': '验证码不能为空'},
    )

    # 验证码

    def clean_password(self):
        password = self.cleaned_data['password']
        return md5(password)


class LoginModelForm(forms.ModelForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': '用户名不能为空'},
        required=True

    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': '密码不能为空'},
        required=True
    )

    class Meta:
        model = models.admin
        fields = ['username', 'password']


# 登录
def login(request):
    if request.method == 'GET':
        form = LoginForm
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证通过,获取用户信息
        # 1.获取用户名、密码和code
        # print(form.cleaned_data)
        # {'username': 'admin', 'password': '123', 'code': '123'}

        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', '')

        if code.upper() != user_input_code.upper():
            form.add_error('code', '验证码错误')
            return render(request, 'login.html', {'form': form})

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # 2.查询数据库
        admin_object = models.admin.objects.filter(username=username, password=password).first()
        # user = models.admin.objects.filter(**form.cleaned_data).first()
        # 没有找到用户
        if not admin_object:
            form.add_error('password', '用户名或密码错误')
            # 添加错误信息
            return render(request, 'login.html', {'form': form, })
        # 存在用户
        else:
            # 1.生成随机字符串,写到用户浏览器的cookie中,再写到session中
            request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
            # 用户信息保存15天
            request.session.set_expiry(60 * 60 * 24 * 15)
            return redirect('http://127.0.0.1:8000/main/')

    return render(request, 'login.html', {'form': form})


# 注销
def logout(request):
    request.session.clear()
    # 清除session
    return redirect('http://127.0.0.1:8000/main/')


# 验证码
def image_code(request):
    # 调用函数，生成图片和验证码
    img, code_str = check_code()
    print(code_str)
    # 写到session中，以便以后获取验证码校验
    request.session['image_code'] = code_str
    # 设置session的过期时间60秒
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')

    return HttpResponse(stream.getvalue())


# 主页面
def main(request):
    return render(request, 'main.html')
