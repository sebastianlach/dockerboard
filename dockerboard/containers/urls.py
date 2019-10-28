from django.urls import path
from . import views


app_name = 'containers'

urlpatterns = [
    path('list.html', views.list, name='list'),
]
