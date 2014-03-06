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
           self.render('productgroup.html', username=user[0].name, rolename=roler[0].name, select="default")
    def post(self):
        leave_type=self.get_argument("leave_type")
        leave_time_begin=self.get_argument("leave_time_begin")
        leave_time_end=self.get_argument("leave_time_end")
        reason_for_leave=self.get_argument("reason_for_leave")
        leave_time_begin=datetime.strptime(leave_time_begin,"%m/%d/%Y")
        leave_time_end=datetime.strptime(leave_time_end,"%m/%d/%Y")
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
        left_year_holiday=self.get_argument("left_year_holiday")
        position=Position.objects.get(id=self.get_argument("position"))
        role=Role.objects.get(id=self.get_argument("role"))
        department=Department.objects.get(id=self.get_argument("department"))
        superior=self.get_argument("superior")
        superior=User.objects.filter(name=superior)
        superior_id=superior[0].id
        User.objects.create(name=name,real_name=real_name,password=password,gender=gender,phone_num=phone_num,
                            pre_year_holiday=pre_year_holiday,left_year_holiday=left_year_holiday,
                            position=position,role=role,department=department,superior=superior_id)
        self.redirect('/register')





