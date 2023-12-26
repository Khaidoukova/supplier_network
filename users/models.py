from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    name = models.CharField(max_length=50, verbose_name='имя', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='телефон', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

