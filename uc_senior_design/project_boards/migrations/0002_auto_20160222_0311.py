# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
