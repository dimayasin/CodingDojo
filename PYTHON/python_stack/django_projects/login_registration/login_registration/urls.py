from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('apps.login_app.urls')),
    url(r'^', include('apps.login_app.urls'))
]
