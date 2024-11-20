# Generated by Django 5.0.4 on 2024-05-07 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='部门表')),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='员工姓名')),
                ('password', models.CharField(max_length=100, verbose_name='员工密码')),
                ('age', models.IntegerField(verbose_name='员工年龄')),
                ('account', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='员工账户')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='入职时间')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zxl.department', verbose_name='部门')),
            ],
        ),
    ]
