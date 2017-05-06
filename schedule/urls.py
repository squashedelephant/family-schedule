from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()
from schedule import views

app_name = 'schedule'
urlpatterns = [
    url(r'^$', views.home,
               name='home'),
    url(r'^schedule$', views.create_dashboard,
                     name='create_dashboard'),
    url(r'^parent$', views.create_parent,
                     name='create_parent'),
    url(r'^parentimage$', views.create_parent,
                          name='upload_parent_image'),
    url(r'^child$', views.create_parent,
                    name='create_child'),
    url(r'^childimage$', views.create_parent,
                         name='upload_child_image'),
    url(r'^event$', views.create_parent,
                    name='create_event'),
    url(r'^admin/', admin.site.urls),
]
