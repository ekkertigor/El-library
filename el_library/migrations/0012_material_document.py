# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el_library', '0011_remove_material_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='document',
            field=models.FileField(default=0, upload_to=''),
        ),
    ]
