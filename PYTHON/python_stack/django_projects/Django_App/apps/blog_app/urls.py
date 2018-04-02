from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index) ,   
    url(r'^new$', views.new_blog),
    url(r'^create$', views.create_blog),
    url(r'^\d+$', views.show),
    url(r'^\d+/edit$', views.edit_number),
    url(r'^\d+/delete$', views.delete)
  ]