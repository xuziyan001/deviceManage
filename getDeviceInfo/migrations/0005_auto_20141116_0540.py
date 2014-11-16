# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('getDeviceInfo', '0004_deviceinfo_is_exist'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceinfo',
            name='borrow_status',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='borrow_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 16, 5, 40, 58, 45714, tzinfo=utc), verbose_name=b'Borrow Time'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='borrower',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='device_name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='device_type',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='kernel_version',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='op_system',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='owner',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='ui_version',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='register_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 16, 5, 40, 58, 45743, tzinfo=utc), verbose_name=b'Register Time'),
            preserve_default=True,
        ),
    ]
