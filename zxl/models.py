from django.db import models


# Create your models here.
# 部门表
class department(models.Model):
    # 部门表
    title = models.CharField(verbose_name='部门表', max_length=100)

    # *********
    def __str__(self):
        return self.title


# 员工表
class userinfo(models.Model):
    # 员工表
    name = models.CharField(verbose_name='员工姓名', max_length=100)
    password = models.CharField(verbose_name='员工密码', max_length=100)
    age = models.IntegerField(verbose_name='员工年龄')
    account = models.DecimalField(verbose_name='员工账户', max_digits=10, decimal_places=2, default=0)

    # create_time = models.DateTimeField(verbose_name='入职时间', )
    create_time = models.DateField(verbose_name='入职时间')
    gender_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    depart = models.ForeignKey(verbose_name='部门', to='department', to_field='id', on_delete=models.CASCADE)


class job(models.Model):
    # 职位表
    title = models.CharField(verbose_name='职位', max_length=100)

    def __str__(self):
        return self.title


# 号码表
class number(models.Model):
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    leve_choices = (
        (1, '普通用户'),
        (2, '高级用户'),
        (3, 'VIP用户'),
    )
    leve = models.SmallIntegerField(verbose_name='等级', choices=leve_choices)
    status_choices = (
        (1, '未占用'),
        (2, '已占用'),

    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices)

    price = models.DecimalField(verbose_name='价格', max_digits=10, decimal_places=2, default=0)


# 管理员
class admin(models.Model):
    # 管理员表
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username
    # 重写__str__方法，使其返回管理员的用户名


# 任务
class task(models.Model):
    title = models.CharField(verbose_name='任务名称', max_length=100)
    content = models.TextField(verbose_name='任务内容', max_length=100)
    create_time = models.DateTimeField(verbose_name='创建时间')

    level_choices = (
        (1, '紧急'),
        (2, '重要'),
        (3, '一般'),
    )
    level = models.SmallIntegerField(verbose_name='优先级', choices=level_choices)
    status_choices = (
        (1, '未完成'),
        (2, '已完成'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices)
    user = models.ForeignKey(verbose_name='负责人', to='admin', on_delete=models.CASCADE)


# 订单表
class order(models.Model):
    oid = models.CharField(verbose_name='订单号', max_length=32)
    title = models.CharField(verbose_name='商品名称', max_length=100)
    price = models.DecimalField(verbose_name='价格', max_digits=10, decimal_places=2)
    status_choices = (
        (1, '已支付'),
        (2, '未支付')
    )
    status = models.SmallIntegerField(verbose_name='订单状态', choices=status_choices)
    admin = models.ForeignKey(verbose_name='管理员', to='admin', on_delete=models.CASCADE)


# 老板
class boos(models.Model):
    name = models.CharField(verbose_name='城市', max_length=100)
    age = models.IntegerField(verbose_name='年龄')
    img = models.ImageField(verbose_name='头像', max_length=128)


class city(models.Model):
    name = models.CharField(verbose_name='城市', max_length=100)
    count = models.IntegerField(verbose_name='人口')
    img = models.FileField(verbose_name='LOGO', max_length=128, upload_to='city/')
    # upload_to='city/'表示将文件保存到media/city/目录下
    # FileField可以自动保存数据，本质上还是CharField


class test(models.Model):
    username = models.CharField(verbose_name='名字', max_length=100)
    age = models.IntegerField(verbose_name='年龄')
    high = models.FloatField(verbose_name='身高')
    weight = models.FloatField(verbose_name='体重')
