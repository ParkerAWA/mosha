# Generated by Django 5.0.4 on 2024-05-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxl', '0003_alter_userinfo_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=100, verbose_name='手机号')),
                ('leve', models.SmallIntegerField(choices=[(1, '普通用户'), (2, '高级用户'), (3, 'VIP用户')], verbose_name='等级')),
                ('status', models.SmallIntegerField(choices=[(1, '未占用'), (2, '已占用')], verbose_name='状态')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='价格')),
            ],
        ),
    ]