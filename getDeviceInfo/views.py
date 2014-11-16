from django.shortcuts import render
from django.http import HttpResponse
from models import DeviceInfo
import datetime
from django.template import RequestContext, loader


def register(request):
    if request.method == 'POST':
        info = request.POST
        device_id = info['device_id']
        op_system = models.CharField(max_length=100)
        kernel_version = models.CharField(max_length=100)
        ui_version = models.CharField(max_length=100)
        device_name = models.CharField(max_length=200)
        device_type = models.CharField(max_length=100)
        owner = models.CharField(max_length=100)
        borrower = models.CharField(max_length=100)
        borrow_time = models.DateTimeField('Borrow Time')
        register_time = datetime.strptime(info['register_time'], '%y%m%d %H:%M')
        borrow_status = models.IntegerField(default=0)
        is_exist = models.IntegerField(default=1)
        new_device = DeviceInfo.objects.create(device_id=device_id,
                                               op_system=op_system,
                                               kernel_version=kernel_version,
                                               ui_version=ui_version,
                                               device_name=device_name,
                                               device_type=device_type,
                                               owner=owner,
                                               borrower=borrower,
                                               borrow_status=borrow_status,
                                               is_exist=is_exist,
                                               register_time=register_time)
        new_device.save()
        return HttpResponse('register ok.')


def delete(request):
    if request.method == 'GET':
        info = request.GET
        device_id = info['device_id']
        delete_device = DeviceInfo.objects.filter(device_id=device_id)
        #assert delete_device['is_exist'] == 1
        if delete_device[0].borrow_status == 1:
            return HttpResponse('Please return the device first.' +
                                '<br><a href="http://localhost:8000/getDeviceInfo/show">return</a>')
        else:
            delete_device.update(is_exist=0)
    return HttpResponse('delete %s' % device_id+'<br><a href="http://localhost:8000/getDeviceInfo/show">return</a>')


def borrow(request):
    if request.method == 'GET':
        info = request.GET
        device_id = info['device_id']
        template = loader.get_template('borrow.html')
        context = RequestContext(request, {'device_id': device_id})
        #borrow_device = DeviceInfo.objects.filter(device_id=device_id)
        #borrow_device.update(borrower=borrower, borrow_status=1)
        #return HttpResponse('%s borrowed device %s <br><a href="http://localhost:8000/getDeviceInfo/show">return</a>' % (borrower, device_id))
        return HttpResponse(template.render(context))
    else:
        return HttpResponse('fsdfds')


def borrow_with_name(request):
    if request.method == 'GET':
        info = request.GET
        device_id = info['device_id']
        borrower = info['borrower']
        borrow_device = DeviceInfo.objects.filter(device_id=device_id)
        borrow_device.update(borrower=borrower, borrow_status=1)
        return HttpResponse('%s borrowed device %s <br><a href="http://localhost:8000/getDeviceInfo/show">return</a>' % (borrower, device_id))


def return_device_back(request):
    if request.method == 'GET':
        info = request.GET
        device_id = info['device_id']
        borrow_device = DeviceInfo.objects.filter(device_id=device_id)
        borrow_device.update(borrow_status=0, borrower='')
        return HttpResponse('%s returned. <br><a href="http://localhost:8000/getDeviceInfo/show">return</a>' % device_id)


def show(request):
    a = DeviceInfo.objects.filter(is_exist=1)
    template = loader.get_template('template.html')
    context = RequestContext(request, {'device': a})
    return HttpResponse(template.render(context))

