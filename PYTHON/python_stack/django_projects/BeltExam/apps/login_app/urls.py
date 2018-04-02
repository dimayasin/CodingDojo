from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'login$', views.logins),
    url(r'log$', views.log),
    url(r'create$', views.Registration),
    url(r'new_user$', views.new_user),
    url(r'show$',  views.show),
    url(r'add$',  views.add),
    url(r'update$',  views.update),
    url(r'new_appointment$', views.Newappointments),
    url(r'(?P<id>\d+)/edit$', views.edit),
    url(r'delete$', views.delete),
    url(r'out$', views.out),
    # url(r'(?P<id>\d+)/showTody$', views.showToday),
    # url(r'(?P<id>\d+)/showOthers$', views.showOthers),
]
