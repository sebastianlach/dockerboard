from django.conf.urls import url
from . import views


app_name = 'containers'

urlpatterns = [
    url(r'^list.html$', views.list, name='list'),
    url(r'^(?P<container_id>.+)/details.html$', views.details, name='details'),
    url(r'^(?P<container_id>.+)/logs.html$', views.details, name='logs'),
]
