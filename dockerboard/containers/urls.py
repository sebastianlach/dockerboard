from django.conf.urls import url
from . import views


app_name = 'containers'

urlpatterns = [
    url(r'^list.html$', views.list, name='list'),
    url(r'^(?P<container_id>.+)/details.html$', views.details, name='details'),
    url(r'^(?P<container_id>.+)/start$', views.start, name='start'),
    url(r'^(?P<container_id>.+)/restart$', views.restart, name='restart'),
    url(r'^(?P<container_id>.+)/stop$', views.stop, name='stop'),
]
