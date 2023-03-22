from django.core.exceptions import ValidationError
from rest_framework import serializers
from api.models import Client, Photo


def validate_file_size(value):
    filesize = value.size
    if filesize > 1024 * 5:  # 5Mb limit
        raise ValidationError("The maximum file size that can be uploaded is 5MB")
    else:
        return value

class ClientSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(validators=[validate_file_size])
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'sex',
            'birthday',
            'photo',
            'photo_url' 
            ]

    def create(self, validated_data):
        photo = validated_data.pop('photo')
        photo_obj = Photo.objects.create(image=photo)
        instance = Client.objects.create(photo=photo_obj, **validated_data)
        return instance

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo = Photo.objects.get(id=obj.photo.id)
        return request.build_absolute_uri(photo.image.url)

    # def update(self, validated_data):
    #     photo = validated_data.pop('photo')
    #     photo_obj, _ = Photo.objects.get_or_404(**photo)
    #     instance = Client.objects.update(photo=photo_obj, **validated_data)
    #     return instance


class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    date = serializers.DateField()


class InputWeatherSerializer(serializers.Serializer):
    city = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
