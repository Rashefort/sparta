# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Note



@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'description')
