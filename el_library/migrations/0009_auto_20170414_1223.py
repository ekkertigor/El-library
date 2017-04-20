# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el_library', '0008_auto_20170414_0048'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.RemoveField(
            model_name='material',
            name='tags',
        ),
        migrations.AddField(
            model_name='material',
            name='tags',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
