#coding=utf-8

from django.contrib import admin
import models

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'real_name', 'gender', ]

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Department)
admin.site.register(models.Position)
admin.site.register(models.Role)
admin.site.register(models.Leave)
admin.site.register(models.Attendance)
