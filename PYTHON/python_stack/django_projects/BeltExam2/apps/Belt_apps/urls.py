from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'login$', views.logins),
    url(r'log$', views.log),
    url(r'create$', views.Registration),
    url(r'new_user$', views.new_user),
    url(r'show$',  views.show),
    url(r'new_item$', views.additem),
    url(r'new$', views.new_item),
    url(r'out$', views.out),
    url(r'delete$', views.delete),
    url(r'(?P<id>\d+)/showlist$', views.showlist),
    url(r'(?P<id>\d+)/remove$', views.remove),  
    url(r'(?P<id>\d+)/favorites$',  views.favorites),  
    url(r'(?P<id>\d+)/notfave$',  views.notfavorite),  
    

]