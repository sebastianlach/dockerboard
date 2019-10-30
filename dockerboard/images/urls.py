from django.conf.urls import url
from . import views


app_name = 'images'

urlpatterns = [
    url(r'^list.html$', views.list, name='list'),
    url(r'^(?P<image_id>.+)/details.html$', views.details, name='details'),
]
