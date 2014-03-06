#coding=utf-8

from django.db import models
from oa_admin.comm_def import UserGender,Verfify,AskforleaveType
#**********************************************************************
class Department(models.Model):
    name = models.CharField('部门名称', max_length = 20, unique=True)
    detail = models.CharField('部门职责', max_length = 100)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '部门数据'
        verbose_name_plural = verbose_name

class Position(models.Model):
    name = models.CharField('职位名称', max_length = 20, unique=True)
    detail = models.CharField('职位职责', max_length = 100)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '职位数据'
        verbose_name_plural = verbose_name

class Role(models.Model):
    name = models.CharField('角色名称', max_length = 20, unique=True)
    detail = models.CharField('角色职责', max_length = 100)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '角色数据'
        verbose_name_plural = verbose_name
#**********************************************************************************

class User(models.Model):
    name = models.CharField('登陆名', max_length=20, unique=True)
    real_name = models.CharField('真实姓名', max_length=20)
    password = models.CharField('密码', max_length=60)
    gender = models.PositiveSmallIntegerField('性别', blank=True, null=True, choices=UserGender.attrs.items())
    birthday = models.DateTimeField('生日', blank=True, null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    phone_num = models.CharField('电话号码', max_length=20)
    pre_year_holiday = models.PositiveSmallIntegerField()
    left_year_holiday = models.PositiveSmallIntegerField()
    superior=models.IntegerField()
    position = models.ForeignKey(Position)
    role = models.ForeignKey(Role)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name


class Leave(models.Model):
    user = models.ForeignKey(User)
    leave_type = models.PositiveSmallIntegerField('请假类型', blank=True, null=True, choices=AskforleaveType.attrs.items())
    reason_for_leave = models.CharField('请假事由', max_length=150)
    leave_time_begin = models.DateTimeField('请假开始时间', auto_now_add=True)
    leave_time_end = models.DateTimeField('请假截址时间', auto_now_add=True)
    verify_status = models.PositiveSmallIntegerField('确认状态', blank=True, null=True, choices=Verfify.attrs.items())

    #verify_people = models.CharField('审核人', max_length=20, unique=True)

    def __unicode__(self):
        return self.reason_for_leave

    class Meta:
        verbose_name = '请假数据'
        verbose_name_plural = verbose_name


class attendance(models.Model):
    user=models.ForeignKey(User)
    punchwork = models.DateTimeField('上班打卡时间',auto_now=True)
    punchworkoff = models.DateTimeField('下班打卡时间',auto_now=True)