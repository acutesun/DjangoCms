# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-17 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20170817_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='content.Article'),
            preserve_default=False,
        ),
    ]