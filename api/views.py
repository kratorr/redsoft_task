from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.models import Client, Photo
from api.serializers import ClientSerializer, PhotoSerializer


# class ClientViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = Client.objects.all()
#         serializer = ClientSerializer(queryset, many=True)
#         return Response(serializer.data)

# class ClientViewSet(viewsets.ModelViewSet):

#     serializer_class = ClientSerializer
#     queryset = Client.objects.all()


class ClientViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin
                    ):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class WeatherView(APIView):
    """Get weather by city and date"""

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('city', openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING),
        openapi.Parameter('date', openapi.IN_QUERY, required=True, type=openapi.FORMAT_DATE)
        ]
     )
    def get(self, request):
        # по хорошему вытащить в отдельный код
        url = 'https://wttr.in/Moscow'
        #date = '2021-10-20' # Дата в формате ГГГГ-ММ-ДД
        city = self.request.query_params.get('city')
        date = self.requet.query

      #  response = requests.get(f'{url}/')
        response = requests.get(f'{url}/city={city}&date={date}')
        if response.status_code == 200:
            data = response.text
            print(data)
        else:
            print('Failed to retrieve data from wttr.in')
        return Response(data)