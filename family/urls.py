from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^schedule/', include('schedule.urls')),
    url(r'^admin/', admin.site.urls),
]
