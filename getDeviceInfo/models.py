from django.db import models
from django.utils import timezone
# Create your models here.


class DeviceInfo(models.Model):
    device_id = models.CharField(primary_key=True, max_length=200)
    op_system = models.CharField(max_length=100, default='')
    kernel_version = models.CharField(max_length=100, default='')
    ui_version = models.CharField(max_length=100, default='')
    device_name = models.CharField(max_length=200, default='')
    device_type = models.CharField(max_length=100, default='')
    owner = models.CharField(max_length=100, default='')
    borrower = models.CharField(max_length=100, default='')
    borrow_time = models.DateTimeField('Borrow Time', default=timezone.now())
    register_time = models.DateTimeField('Register Time', default=timezone.now())
    borrow_status = models.IntegerField(default=0) #0 can be borrowed 1 cannot
    is_exist = models.IntegerField(default=1) # 0 deleted 1 exist
