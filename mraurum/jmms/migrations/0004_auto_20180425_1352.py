# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jmms', '0003_auto_20180423_1205'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='raw_material_type',
            unique_together=set([('material_name', 'material_purity')]),
        ),
    ]
