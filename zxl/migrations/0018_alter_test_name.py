# Generated by Django 5.0.4 on 2024-10-17 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zxl', '0017_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=100, verbose_name='名字'),
        ),
    ]