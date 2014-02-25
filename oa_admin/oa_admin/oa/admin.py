#coding=utf-8

from django.contrib import admin
import models

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'real_name', 'gender', ]

admin.site.register(models.User, UserAdmin)
