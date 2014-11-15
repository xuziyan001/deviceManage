from django.db import models

# Create your models here.


class DeviceInfo(models.Model):
    device_id = models.CharField(primary_key=True, max_length=200)
    '''
    op_system = models.CharField(max_length=100)
    kernel_version = models.CharField(max_length=100)
    ui_version = models.CharField(max_length=100)
    device_name = models.CharField(max_length=200)
    device_type = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    borrower = models.CharField(max_length=100)
    borrow_time = models.DateTimeField('Borrow Time')
    '''
    register_time = models.DateTimeField('Register Time')
    '''
    borrow_status = models.IntegerField(default=0)
    '''
    is_exist = models.IntegerField(default=1)
