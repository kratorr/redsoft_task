from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from rest_framework import serializers

from api.models import Client, Photo


UserModel = get_user_model()


def validate_file_size(value):
    filesize = value.size
    print(value.size)
    if filesize > 1024 * 1024 * 5:  # 5Mb limit
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value


class ClientSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(source='photo.image', validators=[validate_file_size])

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'sex',
            'birthday',
            'photo',
            ]

    def create(self, validated_data):
        photo = validated_data.pop('photo')
        photo_obj = Photo.objects.create(image=photo['image'])
        instance = Client.objects.create(photo=photo_obj, **validated_data)
        return instance

    def update(self, instance, validated_data, *args, **kwargs):
        photo = validated_data.pop('photo', None)
        if photo:
            photo_obj = Photo.objects.get(id=instance.photo.id)
            photo_obj.image = photo['image']
            photo_obj.save()
            instance.photo = photo_obj

        return super().update(instance, validated_data)


class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    date = serializers.DateField()


class InputWeatherSerializer(serializers.Serializer):
    city = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
