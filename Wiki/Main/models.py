from django.db import models
from django.contrib.auth.models import AbstractUser

def Get_UserName(instance, filename):
    return "user/{0}/{1}".format(instance.username, filename)
# Create your models here.
# Переосмысление модели пользователя, добавление новых полей.
class CustomUser(AbstractUser):
    login = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    second_name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True, help_text="ФИО пользователя")
    department = models.CharField(max_length=30, blank=True)
    otdel = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(verbose_name="Фото пользователя", blank=True, null=True, upload_to=Get_UserName)
    birth_date = models.DateField(null=True, blank=True)
