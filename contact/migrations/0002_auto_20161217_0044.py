# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='contact',
            name='middle_name',
            field=models.CharField(max_length=18),
        ),
    ]
