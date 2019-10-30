from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', include('dashboard.urls', namespace='dashboard')),
    url(r'^containers/', include('containers.urls', namespace='containers')),
    url(r'^images/', include('images.urls', namespace='images')),
] + static(settings.STATIC_URL)
