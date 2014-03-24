#coding=utf-8

from django.db import models
from oa_admin.comm_def import UserGender,Verfify,AskforleaveType,Isabsent
#**********************************************************************
class Department(models.Model):
    name = models.CharField('部门名称', max_length = 20, unique = True)
    detail = models.CharField('部门职责', max_length = 100)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '部门数据'
        verbose_name_plural = verbose_name

class Position(models.Model):
    name = models.CharField('职位名称', max_length = 20, unique = True)
    detail = models.CharField('职位职责', max_length = 100)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '职位数据'
        verbose_name_plural = verbose_name

class Role(models.Model):
    name = models.CharField('角色名称', max_length = 20, unique = True)
    detail = models.CharField('角色职责', max_length = 100)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '角色数据'
        verbose_name_plural = verbose_name
#**********************************************************************************

class User(models.Model):
    name = models.CharField('登陆名', max_length = 20, unique = True)
    real_name = models.CharField('真实姓名', max_length = 20)
    password = models.CharField('密码', max_length = 60)
    gender = models.PositiveSmallIntegerField('性别', blank = True, null = True, choices = UserGender.attrs.items())
    birthday = models.DateTimeField('生日', blank=True, null = True)
    create_time = models.DateTimeField('创建时间', auto_now_add = True)
    update_time = models.DateTimeField('更新时间', auto_now = True)
    phone_num = models.CharField('电话号码', max_length = 20)
    pre_year_holiday = models.PositiveSmallIntegerField()
    remain_year_holiday = models.PositiveSmallIntegerField()
    superior = models.ForeignKey('self',default = 'null',blank = True,null = True)
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
    leave_type = models.PositiveSmallIntegerField('请假类型', blank = True, null = True, choices=AskforleaveType.attrs.items())
    reason_for_leave = models.CharField('请假事由', max_length=150)
    leave_time_begin = models.DateTimeField('请假开始时间')
    leave_time_end = models.DateTimeField('请假截址时间')
    verify_status = models.PositiveSmallIntegerField('确认状态', blank = True, null = True,default = 0,choices = Verfify.attrs.items())
    create_time = models.DateTimeField('创建时间', auto_now_add = True)
    #verify_people = models.CharField('审核人', max_length=20, unique=True)

    def __unicode__(self):
        return self.reason_for_leave

    class Meta:
        verbose_name = '请假数据'
        verbose_name_plural = verbose_name


class Attendance(models.Model):
     user = models.ForeignKey(User, default=None, null=True)
     name = models.CharField('名字',max_length=20,blank=True,null=True)
     punchwork = models.TimeField('上班打卡时间',blank = True, null = True)
     punchworkoff = models.TimeField('下班打卡时间', blank = True, null = True)
     daytime=models.DateField("日期", blank = True, null = True)
     musttime=models.FloatField('应到', blank = True, null = True)
     realtime=models.FloatField('实际到', blank = True, null = True)
     latetime=models.TimeField('迟到时间',blank=True,null=True)
     earlytime=models.TimeField('早到时间',blank=True,null=True, default=None)
     isabsent=models.PositiveSmallIntegerField('是否旷工',blank=True,null=True,choices = Isabsent.attrs.items())
     overtime=models.TimeField('加班',blank=True,null=True)
     apartment=models.CharField('部门',max_length=50,blank=True,null=True)
     worktime=models.TimeField('出勤时间',blank=True,null=True)
     remark=models.CharField('备注',max_length=150,blank=True,null=True)

