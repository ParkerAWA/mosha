# Generated by Django 5.0.4 on 2024-05-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxl', '0007_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.TextField(max_length=100, verbose_name='任务内容'),
        ),
    ]
