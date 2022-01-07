from datetime import datetime, timedelta
import pytz
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Аватар')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')

    activate_key = models.CharField(max_length=128, verbose_name='ключ активации', blank=True, null=True)
    activate_key_expired = models.DateTimeField(blank=True, null=True)

    def is_activation_key_expired(self):
        if datetime.now(pytz.timezone(settings.TIME_ZONE)) > self.activate_key_expired + timedelta(hours=48):
            return True
        return False
    #
    # def delete(self, *args, **kwargs):
    #     if self.is_active:
    #         self.is_active = False
    #     else:
    #         self.is_active = True
    #     self.save()
