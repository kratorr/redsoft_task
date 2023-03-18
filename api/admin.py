from django.contrib import admin

from api.models import Client, Photo
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client)
admin.site.register(Photo)
