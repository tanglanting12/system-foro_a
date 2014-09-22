#coding=utf-8

from django.db import models
from oa_admin.comm_def import UserGender,Verfify,AskforleaveType,Isabsent,Deleteleavetag,Isnormal
#**********************************************************************

class ExpressionSoftwareV(models.Model):
    expressionPackage = models.CharField('客户端包名',max_length = 30)
    expressionVersionNum = models.CharField('客户端版本号',max_length = 20,unique = True)
    expressionVersionName = models.CharField('客户端版本名称',max_length = 30)
    expressionUrl = models.FileField('客户端软件',upload_to = 'SoftwareFiles/%Y/%m/%d')

    def __unicode__(self):
        return self.expressionVersionNum
    class Meta:
        verbose_name = '客户端软件数据'
        verbose_name_plural = verbose_name

class ZipCategory(models.Model):
    zipCategoryName = models.CharField('表情包类别名',max_length=20)
    zipCategoryDetail = models.CharField('表情包类别简介',max_length=40)
    zipCategoryLogo =  models.ImageField('表情包类别logo',upload_to = 'ExpressionPackageCategoryPhotos/%Y/%m/%d')


    def __unicode__(self):
        return self.zipCategoryName

    class Meta:
        verbose_name = '表情包类型数据'
        verbose_name_plural = verbose_name

class ExpresionPackage(models.Model):
    zipUrl = models.FileField('表情包',upload_to = 'ExpressionPackageFiles/%Y/%m/%d')
    picUrl = models.ImageField('表情logo',upload_to = 'ExpressionPackagePhotos/%Y/%m/%d')
    zipName = models.CharField('表情包名称',max_length = 20)
    zipInfo = models.CharField('表情包介绍',max_length = 30)
    zipSize = models.FloatField('表情包大小')
    zipReleaseTime = models.DateTimeField('发布日期', auto_now_add = True)
    zipPrice = models.FloatField('表情包价格')
    zipCategory = models.ForeignKey(ZipCategory,verbose_name = '表情包类别')

    def __unicode__(self):
        return self.zipName

    class Meta:
        verbose_name = '表情包数据'
        verbose_name_plural = verbose_name



'''
class Department(models.Model):
    name = models.CharField('部门名称', max_length = 20, unique = True)
    detail = models.CharField('部门职责', max_length = 100)
    picture = models.ImageField('部门logo',upload_to = 'photos/%Y/%m/%d',blank = True, null = True)
    filesDepartment = models.FileField('提交文件',upload_to = 'files/%Y/%m/%d',blank = True, null = True)
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
    pre_year_holiday = models.PositiveSmallIntegerField(verbose_name = '每年年假')
    superior = models.ForeignKey('self',default = 'null',blank = True,null = True,verbose_name = '上级')
    position = models.ForeignKey(Position,verbose_name = '职位')
    role = models.ForeignKey(Role,verbose_name = '角色')
    department = models.ForeignKey(Department,verbose_name = '部门')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name


class Leave(models.Model):
    user = models.ForeignKey(User,verbose_name = '用户名')
    leave_type = models.PositiveSmallIntegerField('请假类型', blank = True, null = True, choices=AskforleaveType.attrs.items())
    reason_for_leave = models.CharField('请假事由', max_length=150)
    leave_time_begin = models.DateTimeField('请假开始时间')
    leave_time_end = models.DateTimeField('请假截址时间')
    verify_status = models.PositiveSmallIntegerField('确认状态', blank = True, null = True,default = 0,choices = Verfify.attrs.items())
    create_time = models.DateTimeField('创建时间', auto_now_add = True)
    #verify_people = models.CharField('审核人', max_length=20, unique=True)
    deleteleavetag = models.PositiveSmallIntegerField('标记请假是否有效', blank = True, null = True,default = 0,choices = Deleteleavetag.attrs.items())
    def __unicode__(self):
        return self.reason_for_leave

    class Meta:
        verbose_name = '请假数据'
        verbose_name_plural = verbose_name
,blank = True, null = True

class Attendance(models.Model):
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
     isnormal=models.PositiveSmallIntegerField('是否异常',blank=True,null=True,default = 0,choices = Isnormal.attrs.items())


     def __unicode__(self):
         return self.name

     class Meta:
         verbose_name = '考勤数据'
         verbose_name_plural = verbose_name
'''