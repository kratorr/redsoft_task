from rest_framework import serializers

from api.models import Client, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image']


class ClientSerializer(serializers.ModelSerializer):

    photo = PhotoSerializer()

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
        photo_obj, _ = Photo.objects.get_or_create(**photo)
        instance = Client.objects.create(photo=photo_obj, **validated_data)
        return instance


    # def update(self, validated_data):
    #     photo = validated_data.pop('photo')
    #     photo_obj, _ = Photo.objects.get_or_404(**photo)
    #     instance = Client.objects.update(photo=photo_obj, **validated_data)
    #     return instance
