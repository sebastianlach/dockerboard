from django.urls import path
from . import views


app_name = 'images'

urlpatterns = [
    path('list.html', views.list, name='list'),
]
