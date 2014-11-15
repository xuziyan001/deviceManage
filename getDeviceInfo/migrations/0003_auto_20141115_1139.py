# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('getDeviceInfo', '0002_auto_20141115_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinfo',
            name='op_system',
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='register_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 15, 11, 39, 17, 241888, tzinfo=utc), verbose_name=b'Register Time'),
            preserve_default=False,
        ),
    ]
