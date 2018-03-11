# -*- coding:utf-8 -*-
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import UserProfile



class UserInline(admin.StackedInline):
    model = UserProfile
    verbose_name_plural = 'Дополнительная информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline, )
    list_display = ('username', 'email', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
