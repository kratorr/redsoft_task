import json


from django.conf import settings

from rest_framework import mixins, viewsets, parsers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from drf_spectacular.openapi import OpenApiParameter, OpenApiTypes
from drf_spectacular.utils import extend_schema


from api.models import Client
from api.serializers import (ClientSerializer, InputWeatherSerializer, WeatherSerializer)
from api.utils import get_weather


class ClientViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin
                    ):
    """Methods for work with client"""

    authentication_classes = [JWTTokenUserAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    parser_classes = [parsers.MultiPartParser, ]
    serializer_class = ClientSerializer
    queryset = Client.objects.all().select_related('photo')


class WeatherView(viewsets.ViewSet):
    """Get weather by city and date"""

    serializer_class = WeatherSerializer
    authentication_classes = [JWTTokenUserAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    @extend_schema(
        parameters=[
           OpenApiParameter("city", OpenApiTypes.STR, OpenApiParameter.QUERY),
           OpenApiParameter("date", OpenApiTypes.DATE, OpenApiParameter.QUERY),
        ],
    )
    def list(self, request):
        input = InputWeatherSerializer(data=request.GET)
        input.is_valid(raise_exception=True)

        weather = get_weather(
            input.validated_data['city'],
            input.validated_data['date']
        )
        return Response(weather)


class MemoryCheckView(viewsets.ViewSet):
    """Get memory status"""

    authentication_classes = [JWTTokenUserAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = []

    def list(self, request):
        with open(settings.MEMORY_STATUS_PATH, 'r') as f:
            memory_usage = json.load(f)
        return Response(memory_usage)
