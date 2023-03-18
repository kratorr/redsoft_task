from django.shortcuts import render

# Create your views here.
# 2. Создать API, с 4-мя методами:
# -- Позволяет получить список всех клиентов (фото, дата рождения, пол,
# имя, фамилия)
# -- Позволяет добавить нового клиента (фото, дату рождения, пол, имя,
# фамилию)
# -- Позволяет изменить клиента (фото, дату рождения, пол, имя, фамилию)
# -- Позволяет удалить клиента
# Загрузка фото должна осуществляться с возможностью его обрезать под
# размер перед сохранением на сервер. Модели с фото и с основными данными
# пользователя должны быть разными моделями.
# 3. Создать api регистрации клиента.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

from api.models import Client, Photo
from api.serializers import ClientSerializer, PhotoSerializer


# class ClientViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = Client.objects.all()
#         serializer = ClientSerializer(queryset, many=True)
#         return Response(serializer.data)

class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class PhotoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Photo.objects.all()
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data)


class WeatherView(mixins.ListModelMixin, generics.GenericAPIView):
    def get(self, request):
        # по хорошему вытащить в отдельный код
        url = 'https://wttr.in/Moscow'
        #date = '2021-10-20' # Дата в формате ГГГГ-ММ-ДД

        response = requests.get(f'{url}/')
     #   response = requests.get(f'{url}/{date}')
        if response.status_code == 200:
            data = response.text
            print(data)
        else:
            print('Failed to retrieve data from wttr.in')
        return Response(data)