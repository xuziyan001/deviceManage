# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=200)),
                ('op_system', models.CharField(max_length=100)),
                ('kernel_version', models.CharField(max_length=100)),
                ('ui_version', models.CharField(max_length=100)),
                ('device_name', models.CharField(max_length=200)),
                ('device_type', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('borrower', models.CharField(max_length=100)),
                ('borrow_time', models.DateTimeField(verbose_name=b'Borrow Time')),
                ('register_time', models.DateTimeField(verbose_name=b'Register Time')),
                ('borrow_status', models.IntegerField(default=0)),
                ('is_exist', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
