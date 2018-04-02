"""Belt_Exam URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^belt/', include('apps.login_registration.urls')),
    url(r'^', include('apps.login_registration.urls')),
]
