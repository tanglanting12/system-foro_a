#coding=utf-8

from django.contrib import admin
import models

class ExpressionSoftwareVAdmin(admin.ModelAdmin):
    list_display = ['id', 'expressionVersionNum', 'expressionVersionName',]

class ZipCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'zipCategoryName', 'zipCategoryDetail', ]

class ExpresionPackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'zipName', 'zipInfo', ]
    search_fields = ['zipName']


admin.site.register(models. ExpressionSoftwareV, ExpressionSoftwareVAdmin)
admin.site.register(models.ZipCategory,ZipCategoryAdmin)
admin.site.register(models.ExpresionPackage, ExpresionPackageAdmin)
