from django.urls import include, path


urlpatterns = [
    path('', include('dashboard.urls', namespace='dashboard')),
    path('containers/', include('containers.urls', namespace='containers')),
    path('images/', include('images.urls', namespace='images')),
]
