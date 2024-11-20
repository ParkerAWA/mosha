from zxl import models
from django import forms
from django.core.validators import RegexValidator
from zxl.utils.bootstrap import BootstrapModelForm
from zxl.utils.encrypt import md5


# 员工编辑和添加
class UserModelForm(BootstrapModelForm):
    # 该函数定义了一个UserModelForm类，继承自BootstrapModelForm。该类用于创建一个用户模型表单

    # 验证规则
    name = forms.CharField(min_length=2, label='用户名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=3, label='密码')

    # create_time = forms.DateField(label='入职时间', widget=forms.DateInput(attrs={'type': 'date'}), )

    class Meta:
        model = models.userinfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'})
        #
        # }

    # ******


# 号码编辑和添加
class numberModelForm(BootstrapModelForm):
    mobile = forms.CharField(label='手机号', validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')])

    # 正则表达式---'^1[3-9]\d{9}$'---用于匹配11位数字且以1开头、第二位是3到9之间的数字的手机号。如果手机号格式错误，会提示用户“手机号格式错误”。
    class Meta:
        model = models.number
        fields = ['mobile', 'status', 'price', 'leve', ]

    # ******


# 管理员添加
class adminModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(label='确认密码',
                                       widget=forms.PasswordInput(render_value=True))
    username = forms.CharField(label='用户名',
                               validators=[RegexValidator(r'^[\u4e00-\u9fa5_a-zA-Z0-9]{2,20}$', '必须包含2到20'
                                                                                                '个中文、英文、数字、下划线或连字符；')])

    password = forms.CharField(label='密码',
                               validators=[RegexValidator(r'^[\w_-]{1,20}$', '必须包含1到20个字母、数字、下划线或连字符；')],
                               widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.admin
        fields = ['username', 'password', 'confirm_password']

    # 密码加密
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        print(pwd)
        return md5(pwd)

    # 密码验证
    def clean_confirm_password(self):
        print(self.cleaned_data)
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if pwd != confirm:
            raise forms.ValidationError('密码不一致')
        return confirm


# 密码重置
class admin2ModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(label='确认密码',
                                       widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = models.admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    # 密码加密
    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = md5(pwd)
        # 检验密码是否与原密码相同
        exists = models.admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise forms.ValidationError('新密码不能与原密码相同')
        return md5(pwd)

    # 密码验证
    def clean_confirm_password(self):
        print(self.cleaned_data)
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if pwd != confirm:
            raise forms.ValidationError('密码不一致')
        return confirm


# 管理员编辑
class admin3ModelForm(BootstrapModelForm):
    username = forms.CharField(label='用户名',
                               validators=[RegexValidator(r'^[\u4e00-\u9fa5_a-zA-Z0-9]{2,20}$', '必须包含2到20'
                                                                                                '个中文、英文、数字、下划线或连字符；')])

    class Meta:
        model = models.admin
        fields = ['username']


# 测试添加
class testModelForm(BootstrapModelForm):
    username = forms.CharField(label='用户名',
                           validators=[RegexValidator(r'^[\u4e00-\u9fa5_a-zA-Z0-9]{2,20}$', '必须包含2到20'
                                                                                            '个中文、英文、数字、下划线或连字符；')])

    age = forms.IntegerField(label='年龄')
    high = forms.IntegerField(label='身高')
    weight = forms.IntegerField(label='体重')

    class Meta:
        model = models.test
        fields = ['username', 'age', 'high', 'weight']
