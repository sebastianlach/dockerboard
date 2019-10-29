from django.urls import path
from . import views


app_name = 'images'

urlpatterns = [
    path('list.html', views.list, name='list'),
    path('<str:image_id>/details.html', views.details, name='details'),
]
