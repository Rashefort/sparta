# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    tz = models.CharField(max_length=5, default='+3', verbose_name='часовой пояс',
        help_text='Часовой пояс пользователя, например +1 или -2. По умолчанию +3')

    def __unicode__(self):
        return self.user


    class Meta:
        verbose_name = 'Профиль'
