#coding=utf-8

from oa_web.module.oa_handler import OaHandler
from oa_web.module.route import Route
import tornado
from datetime import datetime
import time
from oa_admin.oa.models import User, Role,Leave,Position,Department
from oa_web.libs.autodiscover import autodic


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")


@Route('/')
class ProductgroupPage(OaHandler,BaseHandler):

    @tornado.web.authenticated
    def get(self):
        #user = User.objects.get(id=1)
        #self.write('''<p> username:  %s</p>''' %(self.current_user) )
        if self.current_user:
           user = User.objects.filter(name=self.current_user)
           roler = Role.objects.filter(user__name__exact=self.current_user)
           navigation=self.get_argument("navigation",default="default_detail")
           self.render('productgroup.html', username=user[0].name, rolename=roler[0].name, navigation=navigation)

    def post(self):
        leave_type = self.get_argument("leave_type")
        leave_time_begin=self.get_argument("leave_time_begin")
        leave_time_end=self.get_argument("leave_time_end")
        reason_for_leave=self.get_argument("reason_for_leave")
        leave_time_begin=datetime.strptime(leave_time_begin,"%m/%d/%Y")
        leave_time_end=datetime.strptime(leave_time_end,"%m/%d/%Y")
        print "begin%s**,end%s**" %(leave_time_begin,leave_time_end)
        user = User.objects.filter(name=self.current_user)
        Leave.objects.create(user=user[0],leave_type=leave_type,leave_time_begin=leave_time_begin,leave_time_end=leave_time_end,reason_for_leave=reason_for_leave)
        self.redirect('/')
       # print "**%s***%s***%s***%s*******%s***" %(leave_type,leave_time_begin,leave_time_end,reason_for_leave,user[0].name)


@Route('/login')
class LoginHandler(OaHandler,BaseHandler):

    def get(self):
        self.render('login.html')

    def post(self):
        username=self.get_argument("username")
        passwd=self.get_argument("password")
        user = User.objects.filter(name=username,password=passwd)
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
class update(OaHandler):

    def post(self):
        name = self.get_argument("name")
        User.objects.filter(name=name).update(password=self.get_argument("password"))
        self.redirect('/')

    def get(self):
        name=self.get_argument("name",default="abert")
        print "*****%s***" %(type(name))
        #print "***%s***%s***%s" %(position_name.name,role_name.name,department_name.name)
        self.render('change_pwd.html',name=name)



@Route('/register')
class register(OaHandler):

    def get(self):
        positiondic=autodic(Position,"id","name")
        roledic=autodic(Role,"id","name")
        departmentdic=autodic(Department,"id","name")
        self.render('register.html',positiondic=positiondic,roledic=roledic,departmentdic=departmentdic)

    def post(self):
        name=self.get_argument("name")
        real_name=self.get_argument("real_name")
        password=self.get_argument("password")
        gender=self.get_argument("gender")
        phone_num=self.get_argument("phone_num")
        pre_year_holiday=self.get_argument("pre_year_holiday")
        remain_year_holiday=self.get_argument("remain_year_holiday")
        position=Position.objects.get(id=self.get_argument("position"))
        role=Role.objects.get(id=self.get_argument("role"))
        department=Department.objects.get(id=self.get_argument("department"))
        superior=self.get_argument("superior")
        superior=User.objects.filter(name=superior)
        superior_id=superior[0].id
        User.objects.create(name=name,real_name=real_name,password=password,gender=gender,phone_num=phone_num,
                            pre_year_holiday=pre_year_holiday,remain_year_holiday=remain_year_holiday,
                            position=position,role=role,department=department,superior=superior_id)

        self.redirect('/register')


@Route('/leave_detail')
class leavedetail(OaHandler):

    def get(self):
        self.render('leave_detail.html')


@Route('/leave_detailajax')
class leavedetailajax(OaHandler):
    def get(self):
        index=self.get_argument("index",default=0)
        lastpage=self.get_argument("lastpage",default=0)
        comfirm=self.get_argument("comfirm",default=0)
        if (index!=0):
            index=int(index)-1
        step=4
        name=self.get_argument("name",default="abert")
        if lastpage:
            leavedetails=Leave.objects.order_by("leave_time_begin","leave_time_end").filter(user__name__exact=name,verify_status__exact=comfirm).reverse()[:step].values()
        else:
            leavedetails=Leave.objects.order_by("leave_time_begin","leave_time_end").filter(user__name__exact=name,verify_status__exact=comfirm)[index*step:(index+1)*step].values()
        self.render('leave_detailajax.html',leavedetails=leavedetails,name=name)


############### not finish
@Route('/updateperleave')
class updateperleave(OaHandler):

     def get(self):
        leave_id=int(self.get_argument("leave_id"))
        name=int(self.get_argument("name"))
        leave=Leave.objects.get(id=leave_id)
        user = User.objects.get(name=name)
        superior=User.objects.get(id=user.superior)
        return self.render('AskForLeave.html',reason_for_leave=leave.reason_for_leave,
                              superior_id=superior.id,superior_name=superior.name,pre_year_holiday=user.pre_year_holiday,
                              remain_year_holiday=user.remain_year_holiday)



@Route('/leave_delete')
class leave_delete(OaHandler):
     def get(self):
        leave_id=int(self.get_argument("leave_id"))
        Leave.objects.get(id=leave_id).delete()
        print "%s leave Delete success! " %(leave_id)
        self.render('leave_detail.html')

@Route('/leave_comfirm')
class leave_comfirm(OaHandler):
     def get(self):
        step=4
        leave_id=int(self.get_argument("leave_id"))
        Leave.objects.filter(id=leave_id).update(verify_status=1)
        print "&&&%s leave update success! " %(leave_id)
        name=self.get_argument("name",default="abert")
        comfirm=self.get_argument("comfirm",default=0)
        leavedetails=Leave.objects.order_by("leave_time_begin","leave_time_end").filter(user__name__exact=name,verify_status__exact=comfirm).reverse()[:step].values()
        self.render('leave_detailajax.html',leavedetails=leavedetails,name=name)


@Route('/perleave_detail')
class perleave_detail(OaHandler):
     def get(self):
         leave_id=int(self.get_argument("leave_id"))
         leave=Leave.objects.filter(id=leave_id).values()
         self.render('perleave_detail.html',leave=leave)

@Route('/index')
class MainHandler(OaHandler):
     def get(self):
        self.render(
            "index.html",
            header_text = "Header goes here",
            footer_text = "Footer goes here"
        )

'''

@Route('/update')
class update(OaHandler):
    def get(self):
        name="abert"
        user=User.objects.filter(name=name).values()
        position_name=Position.objects.get(id=user[0]["position_id"])
        role_name=Role.objects.get(id=user[0]["role_id"])
        print "****%s***" %(user[0]["department_id"])
        department_name=Department.objects.get(id=user[0]["department_id"])
        print "***%s****&&&&" %(position_name.name)
        #print "***%s***%s***%s" %(position_name.name,role_name.name,department_name.name)
        positiondic=autodic(Position,"id","name")
        roledic=autodic(Role,"id","name")
        departmentdic=autodic(Department,"id","name")
        #print "***%s***%s***%s" %(position_name.name,role_name.name,department_name.name)
        self.render('update_user.html',user=user,position_name=position_name.name,role_name=role_name.name,department_name=department_name.name,
                    positiondic=positiondic,roledic=roledic,departmentdic=departmentdic
                    )
'''
