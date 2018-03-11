# -*- coding:utf-8 -*-
from django.db import models


class Memo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    description = models.CharField(max_length=128, help_text='Краткое описание')
    phone = models.CharField(max_length=24, help_text='Номер телефона')
    ip = models.GenericIPAddressField(default='127.0.0.1')
    create = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.description


    class Meta:
        verbose_name_plural = 'Заметки'
        ordering = ["create"]
