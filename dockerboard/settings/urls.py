from django.conf.urls import url
from . import views


app_name = 'settings'

urlpatterns = [
    url('', views.index, name='index'),
]
