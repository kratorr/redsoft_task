from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from api.views import ClientViewSet, WeatherView, MemoryCheckView



router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')
router.register(r'weather', WeatherView, basename='weather')
router.register(r'memory', MemoryCheckView, basename='memory')

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  #  path('weather/', WeatherView.as_view()),
   # path('memory/', MemoryCheckView.as_view()),
    path('', include(router.urls))
]