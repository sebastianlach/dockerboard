from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', include('dashboard.urls', namespace='dashboard')),
    url(r'^api/', include('api.urls', namespace='api')),
] + static(settings.STATIC_URL)
