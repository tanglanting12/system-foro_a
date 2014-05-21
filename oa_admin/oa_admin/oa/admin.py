#coding=utf-8

from django.contrib import admin
import models

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'real_name', 'gender', ]

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'detail', ]

class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'detail', ]

class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'detail', ]

class LeaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'leave_type', 'leave_time_begin', 'leave_time_end', ]

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isabsent', 'realtime', ]
    search_fields = ['name']
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Department,DepartmentAdmin)
admin.site.register(models.Position,PositionAdmin)
admin.site.register(models.Role,RoleAdmin)
admin.site.register(models.Leave,LeaveAdmin)
admin.site.register(models.Attendance,AttendanceAdmin)
