from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
#from drf_yasg.utils import swagger_auto_schema
#from drf_yasg import openapi
from drf_spectacular.utils import extend_schema
from drf_spectacular.openapi import OpenApiParameter, OpenApiTypes

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
import requests

from api.models import Client, Photo
from api.serializers import ClientSerializer, WeatherSerializer


class ClientViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin
                    ):
    authentication_classes = [JWTTokenUserAuthentication,]
    permission_classes = [IsAuthenticated,]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class WeatherView(APIView):
    """Get weather by city and date"""

    serializer_class = WeatherSerializer
    
    @extend_schema(
        parameters=[
        #  WeatherSerializer,  # serializer fields are converted to parameters
           OpenApiParameter("city", OpenApiTypes.STR, OpenApiParameter.QUERY),
           OpenApiParameter("date", OpenApiTypes.DATE, OpenApiParameter.QUERY),
        ],
     #   request=WeatherSerializer,
      #  responses=WeatherSerializer,
        # more customizations
    )
    def get(self, request):
        api_url = "h777ttps://api.openweathermap.org/data/2.5/forecast"
        api_key = "<YOUR_API_KEY>"

        # Конвертируем дату в формат, необходимый для запроса к API
        start_date = datetime.strptime(date, '%Y-%m-%d')
        start_date_str = start_date.strftime('%Y-%m-%d') + " 12:00:00"
        start_timestamp = int(datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S').timestamp())

        # Выполняем запрос к API, передавая необходимые параметры
        response = requests.get(api_url, params={
            "q": city,
            "appid": api_key,
            "start": start_timestamp,
            "cnt": 1,
            "units": "metric"
        })

        # Обрабатываем результаты запроса
        if response.status_code == 200:
            weather_data = response.json()
           # return weather_data
   
        
        return Response(data)
