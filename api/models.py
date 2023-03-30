from django.db import models


class Client(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Photo(models.Model):
    client = models.OneToOneField('Client', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media', default='')
