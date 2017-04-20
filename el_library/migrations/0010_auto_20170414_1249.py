# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el_library', '0009_auto_20170414_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='material',
            name='tags',
        ),
        migrations.AddField(
            model_name='material',
            name='tags',
            field=models.ManyToManyField(to='el_library.Tags'),
        ),
    ]
