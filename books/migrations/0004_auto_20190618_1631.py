# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-18 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_place_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='name'),
        ),
    ]