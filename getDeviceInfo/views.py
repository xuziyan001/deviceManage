from django.shortcuts import render
from django.http import HttpResponse
from models import DeviceInfo
import datetime


def register(request):
    if request.method == 'POST':
        info = request.POST
        device_id = info['device_id']
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
        register_time = datetime.strptime(info['register_time'], '%y%m%d %H:%M')
        '''
        borrow_status = models.IntegerField(default=0)
        '''
        is_exist = models.IntegerField(default=1)
        new_device = DeviceInfo.objects.create(device_id=device_id, register_time=register_time)
        new_device.save()
        return HttpResponse('register ok.')


def delete(request):
    if request.method == 'GET':
        info = request.GET
        device_id = info['device_id']
        delete_device = DeviceInfo.objects.filter(device_id=device_id)
        assert delete_device['is_exist'] == 1
        delete_device.update(is_exist=0)
    return HttpResponse('delete %s' % device_id)


def borrow(request):
    if request.method == 'GET':
        info = request.GET
        device_id = info['device_id']
        borrower = info['borrower']
        borrow_device = DeviceInfo.objects.filter(device_id=device_id)
        borrow_device.update(borrower=borrower)
        return HttpResponse('%s borrowed device %s' % (borrower, device_id))


def return_device_back(request):
    if request.method == 'GET':
        info = request.GET
        device_id = info['device_id']
        borrow_device = DeviceInfo.objects.filter(device_id=device_id)
        borrow_device.update(borrower='nobody')
        return HttpResponse('%s returned.' % device_id)


def show(request):
    data = []
    a = DeviceInfo.objects.filter(is_exist=1)
    for each in a:
        s = dict()
        s['device_id'] = each.device_id
        s['register_time'] = each.register_time
        data.append(s)
    return HttpResponse('show %s' % s['device_id'])

