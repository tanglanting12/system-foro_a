#coding=utf-8
'''
use to Route for web location :how to solve in server(such as get post)

'''
from oa_web.module.oa_handler import OaHandler
from oa_web.module.route import Route
from oa_admin.oa.models import ExpressionSoftwareV, ZipCategory ,ExpresionPackage
from oa_web.libs.autodiscover import autodic
from oa_web.libs.controller import Leavedetalajax,upload,exceptiondataajax
from oa_web.upload import uploadDir
from xlrd import open_workbook
import StringIO
import tornado
import datetime
import time
import os.path as osp
from oa_web.libs.util import MyobjectEncoder,MyobjectDecoder
import json

@Route('/expressionPackage')
class Leavedelete(OaHandler,Leavedetalajax):
     def get(self):
       # leave_id = int(self.get_argument("leave_id"))
        self.expressionpackages = ExpresionPackage.objects.all()[:1].values('zipUrl','picUrl','zipName','zipInfo','zipSize','zipPrice','zipCategory')

        #MyobjectEncoder(self.expressionpackages)
       # Leave.objects.filter(id = leave_id).update(deleteleavetag=1)
        print "%s expressionpackages! " %(json.dumps(list(self.expressionpackages)))
        return self.render('test.html',myjson = json.dumps(list(self.expressionpackages)))
       # self.leavedetailajax()
        #return  self.render('leave_detailajax.html',leavedetails = self.leavedetails,name = self.name,comfirm = self.comfirm\
         #           ,superiorStyle = self.superiorStyle,index = self.index)


'''

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")


@Route('/')
class Index(OaHandler,BaseHandler):

    @tornado.web.authenticated
    def get(self):
        if self.current_user:
            user = User.objects.get(name = self.current_user)
            roler = Role.objects.filter(user__name__exact = self.current_user)
            navigation = self.get_argument("navigation",default = "default_detail")
            leaves=Leave.objects.filter(verify_status__exact = 0)
            subordinates = User.objects.filter(superior__exact = user.id)
            uncomfirmNum = leaves.filter(user__in = subordinates,deleteleavetag = 0).count()
            if uncomfirmNum == 0:
                uncomfirmNum = ""
            else:
                uncomfirmNum = "("+str(uncomfirmNum)+")"
            if roler[0].name == "管理层":
                self.render('supervisor.html', username = user.name, rolename = roler[0].name, navigation = navigation,uncomfirmNum = uncomfirmNum)
            elif roler[0].name == "行政层":
                self.render('Admin.html', username = user.name, rolename = roler[0].name, navigation = navigation,uncomfirmNum = uncomfirmNum)
            else:
                self.render('productgroup.html', username = user.name, rolename = roler[0].name, navigation = navigation)

    def post(self):
        leave_type = self.get_argument("leave_type")
        leave_time_begin = self.get_argument("leave_time_begin")
        leave_time_end = self.get_argument("leave_time_end")
        reason_for_leave = self.get_argument("reason_for_leave")
        superior = self.get_argument("superior_name")
        leave_time_begin = datetime.datetime.strptime(leave_time_begin,'%Y-%m-%d %H:%M')
        print "leave_time_begin:%s&&" %(leave_time_begin)
        leave_time_end =datetime.datetime.strptime(leave_time_end,'%Y-%m-%d %H:%M')
        print "begin%s**,end%s**" %(leave_time_begin,leave_time_end)
        user = User.objects.filter(name = self.current_user)
        Leave.objects.create(user = user[0],leave_type = leave_type,leave_time_begin = leave_time_begin,
                             leave_time_end = leave_time_end,reason_for_leave = reason_for_leave)
        self.redirect('/')


@Route('/login')
class LoginHandler(OaHandler,BaseHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_argument("username")
        passwd = self.get_argument("password")
        user = User.objects.filter(name = username,password = passwd)
        if user:
           self.set_secure_cookie("username",user[0].name)
           self.redirect("/")
        else:
           error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect.")
           self.redirect(u"/login"+error_msg)
       # user = User.objects.get(id=1)

@Route('/logout')
class LogoutHandler(BaseHandler):

    def get(self):
        #if (self.get_argument("logout", None)):
        self.clear_cookie("username")
        self.redirect('/')


@Route('/updatepwd')
class Update(OaHandler):

    def post(self):
        name = self.get_argument("name")
        User.objects.filter(name = name).update(password = self.get_argument("password"))
        self.redirect('/')

    def get(self):
        name = self.get_argument("name",default = "abert")
        self.render('change_pwd.html',name = name)

@Route('/leave_detail')
class Leavedetail(OaHandler):
    def get(self):
        self.render('leave_detail.html')


@Route('/Leavedetailajax')
class Leavedetailajax(OaHandler,Leavedetalajax):

   def get(self):
        self.leavedetailajax()
        return  self.render('leave_detailajax.html',leavedetails = self.leavedetails,name = self.name,comfirm = self.comfirm\
                    ,superiorStyle = self.superiorStyle,index = self.index,leaves=self.leaves)

@Route('/exceptiondata')
class exceptiondata(OaHandler):
    def get(self):
        self.render('exceptiondata.html')


@Route('/exceptiondataajax')
class exceptiondataajaxClass(OaHandler,exceptiondataajax):
   def get(self):
        self.exceptiondataajax()
        return  self.render('exceptiondataajax.html',exceptiondatas = self.exceptiondatas)




@Route('/leave_delete')
class Leavedelete(OaHandler,Leavedetalajax):
     def get(self):
        leave_id = int(self.get_argument("leave_id"))
        Leave.objects.filter(id = leave_id).update(deleteleavetag=1)
        print "%s leave Delete success! " %(leave_id)
        self.leavedetailajax()
        return  self.render('leave_detailajax.html',leavedetails = self.leavedetails,name = self.name,comfirm = self.comfirm\
                    ,superiorStyle = self.superiorStyle,index = self.index)

@Route('/leave_comfirm')
class Leavecomfirm(OaHandler,Leavedetalajax):
     def get(self):
        leave_id = int(self.get_argument("leave_id"))
        Leave.objects.filter(id = leave_id).update(verify_status=1)
        print "&&&%s leave comfirm success! " %(leave_id)
        self.leavedetailajax()
        return  self.render('leave_detailajax.html',leavedetails = self.leavedetails,name = self.name,comfirm = self.comfirm\
                    ,superiorStyle = self.superiorStyle,index = self.index)

@Route('/leaveUncomfirm')
class LeaveUncomfirm(OaHandler,Leavedetalajax):
     def get(self):
        leave_id = int(self.get_argument("leave_id"))
        Leave.objects.filter(id = leave_id).update(verify_status=0)
        print "&&&%s leave uncomfirm success! " %(leave_id)
        self.leavedetailajax()
        return  self.render('leave_detailajax.html',leavedetails = self.leavedetails,name = self.name,comfirm = self.comfirm\
                    ,superiorStyle = self.superiorStyle,index = self.index)





@Route('/perleave_detail')
class Perleave_detail(OaHandler):
     def get(self):
         leave_id = int(self.get_argument("leave_id"))
         leave = Leave.objects.filter(id = leave_id).values()
         self.render('perleave_detail.html',leave = leave)

@Route('/perexceptiondata')
class Perexceptiondata(OaHandler):
     def get(self):
         exceptiondataid = int(self.get_argument("exceptiondataid"))
         exceptiondata = Attendance.objects.get(id = exceptiondataid)
         self.render('perexceptiondata.html',exceptiondata = exceptiondata)

@Route('/index')
class MainHandler(OaHandler):
     def get(self):
        self.render(
            "index.html",
            header_text = "Header goes here",
            footer_text = "Footer goes here"
        )


@Route('/upload')
class UploadHandler(OaHandler,upload):
    def get(self):
        self.render('UploadAbsenceFile.html')
    def post(self):
        self.uploadexcel()

'''
