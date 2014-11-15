# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getDeviceInfo', '0003_auto_20141115_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceinfo',
            name='is_exist',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
