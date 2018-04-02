from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^show$', views.show),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/showuser$', views.showuser),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    # url(r'^edit$', views.edit),
    url(r'^(?P<id>\d+)/update$', views.update),
    url(r'^(?P<id>\d+)/delete$', views.delete),
]