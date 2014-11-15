# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getDeviceInfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinfo',
            name='borrow_status',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='borrow_time',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='borrower',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='device_name',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='device_type',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='is_exist',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='kernel_version',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='register_time',
        ),
        migrations.RemoveField(
            model_name='deviceinfo',
            name='ui_version',
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='device_id',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
