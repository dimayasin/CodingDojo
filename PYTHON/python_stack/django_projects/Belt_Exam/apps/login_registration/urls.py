from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'login$', views.logins),
    url(r'create$', views.Registration),
    url(r'out$', views.out),
    # url(r'out$', views.out),
]
