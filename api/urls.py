from django.urls import path, include

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from api.views import ClientViewSet, WeatherView, MemoryCheckView

API_VERSION = 'v1'

router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')
router.register(r'weather', WeatherView, basename='weather')
router.register(r'memory', MemoryCheckView, basename='memory')


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(f'{API_VERSION}/', include(router.urls))
]
