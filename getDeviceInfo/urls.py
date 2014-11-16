from django.conf.urls import patterns, url

from getDeviceInfo import views

urlpatterns = patterns('',
                       url(r'^show/$', views.show, name='show'),
                       url(r'borrow/\?$', views.show, name='show'),
                       #url(r'^(?P<register_info>.*?)/register/$', views.register, name='register'),
                       url(r'^register/$', views.register, name='register'),
                       #url(r'^(?P<delete_device_id>.*?)/delete/$', views.delete, name='delete'),
                       url(r'^delete/$', views.delete, name='delete'),
                       #url(r'^(?P<borrower_name>.*?)/borrow/$', views.borrow, name='borrow'),
                       url(r'^borrow/$', views.borrow, name='borrow'),
                       #url(r'^(?P<return_device_id>.*?)/return/$', views.return_device_back, name='return_device_back'),
                       url(r'^return/$', views.return_device_back, name='return_device_back'),
                       url(r'^borrow_with_name/$', views.borrow_with_name, name='borrow_with_name'),

                       )
