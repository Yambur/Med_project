import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    code = ''.join([str(secrets.token_urlsafe(5))])
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=20, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=20, verbose_name='Фамилия', **NULLABLE)

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    verify_code = models.CharField(max_length=10, default=code, verbose_name='Код проверки')
    is_verified = models.BooleanField(default=False, verbose_name='Проверка верификации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'пациент'
        verbose_name_plural = 'пациенты'
