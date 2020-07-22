from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ContainerList, ContainerView

app_name = 'api'

urlpatterns = [
    path(r'containers/', ContainerList.as_view()),
    path(r'containers/<int:pk>/', ContainerView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
