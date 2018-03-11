# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Memo


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'description')
