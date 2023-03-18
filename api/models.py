from django.db import models

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
# 3. Создать api регистрации клиента.\

class Client(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    photo = models.OneToOneField('Photo', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Photo(models.Model):
    image = models.ImageField(upload_to='media', default='')
