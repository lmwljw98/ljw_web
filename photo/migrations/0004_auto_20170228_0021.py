# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_mydata_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='code',
            field=models.CharField(default='kimsohye', max_length=50),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='page',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
