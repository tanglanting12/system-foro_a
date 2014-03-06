#coding=utf-8

from oa_admin.libs.storage import Const


class UserGender(Const):
    male = (0, '男性')
    female = (1, '女性')


class Verfify(Const):
    verfify_not = (0, '未审核')
    verfify = (1, '已审核')


class  AskforleaveType(Const):
    business_leave = (0, '事假')
    sick_leave = (1, '病假')





