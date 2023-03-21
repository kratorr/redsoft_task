import requests
import json


import rest_framework.parsers as parsers

from drf_spectacular.openapi import OpenApiParameter, OpenApiTypes
from drf_spectacular.utils import extend_schema

from django.conf import settings

from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from api.models import Client
from api.serializers import ClientSerializer, InputWeatherSerializer, WeatherSerializer



class ClientViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin
                    ):
    authentication_classes = [JWTTokenUserAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    parser_classes = [parsers.MultiPartParser]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class WeatherView(APIView):
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
    def get(self, request):
        input = InputWeatherSerializer(data=request.GET)
        input.is_valid(raise_exception=True)

        api_url = "http://api.openweathermap.org/geo/1.0/direct?"
        api_key = settings.OPENWEATHER_KEY

        # Выполняем запрос к API, передавая необходимые параметры
        response = requests.get(api_url, params={
            "q": input.validated_data['city'],
            "appid": api_key,
            "start": input.validated_data['date'],
            "cnt": 1,
            "units": "metric"
        })

        print(response.text)

        if response.status_code == 200:
            response = response.json()
        else:
            response = 'Error to fetch weather'

        return Response(response)


class MemoryCheckView(viewsets.ViewSet):

    authentication_classes = [JWTTokenUserAuthentication, ]
    permission_classes = [IsAuthenticated, ]


    def list(self, request):
        with open('./memory_status.json', 'r') as f:
            memory_usage = json.load(f)
        return Response(memory_usage)
