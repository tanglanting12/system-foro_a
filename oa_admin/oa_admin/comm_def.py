#coding=utf-8

from oa_admin.libs.storage import Const


class UserGender(Const):
    male = (1, '男性')
    female = (2, '女性')


class Verfify(Const):
    verfify_not = (1, '未审核')
    verfify = (2, '已审核')


class  AskforleaveType(Const):
    business_leave = (1, '事假')
    sick_leave = (2, '病假')





