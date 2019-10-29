from django.urls import path
from . import views


app_name = 'containers'

urlpatterns = [
    path('list.html', views.list, name='list'),
    path('<str:container_id>/details.html', views.details, name='details'),
    path('<str:container_id>/logs.html', views.details, name='results'),
]
