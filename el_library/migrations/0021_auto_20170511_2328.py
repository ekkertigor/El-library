# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el_library', '0020_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='materials',
            field=models.ManyToManyField(null=True, to='el_library.Material'),
        ),
    ]
