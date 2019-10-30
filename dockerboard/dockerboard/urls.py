from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', include('dashboard.urls', namespace='dashboard')),
    url(r'^containers/', include('containers.urls', namespace='containers')),
    url(r'^images/', include('images.urls', namespace='images')),
]
