#coding=utf-8

from django.db import models
from oa_admin.comm_def import UserGender


class User(models.Model):
    name = models.CharField('登陆名', max_length=20, unique=True)
    real_name = models.CharField('真实姓名', max_length=20)
    password = models.CharField('密码', max_length=60)
    gender = models.PositiveSmallIntegerField('性别', blank=True, null=True, choices=UserGender.attrs.items())
    birthday = models.DateTimeField('生日', blank=True, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name