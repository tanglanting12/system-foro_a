import tornado.web
from oa_admin.oa.models import User, Role ,Leave

class AskForLeave(tornado.web.UIModule):
    def render(self,username):
        user = User.objects.get(name = username)

        superior = User.objects.get(id = 1)
        print "*&&&&debug user%s" %(user.superior)
          #roler = Role.objects.filter(user__name__exact=self.current_user)
        return self.render_string('AskForLeave.html',pre_year_holiday = user.pre_year_holiday,
                                     remain_year_holiday = user.remain_year_holiday,
                                     superior_name = user.superior)

class Askforout(tornado.web.UIModule):

    def render(self,username):
        return self.render_string('askforout.html',username = username)


class Default_detail(tornado.web.UIModule):

    def render(self,username):
        users = User.objects.filter(name = username)
        perleaves = Leave.objects.filter(user__name__exact = username)
        perleave_num = perleaves.count()
        unvertify_num = perleaves.filter(verify_status = 0).count()
        #print "&&&%s&&%s&" % (perleave_num,unvertify_num)
        return self.render_string('default_detail.html',perleave_num = perleave_num,unvertify_num = unvertify_num)




class Wait_for_confirm(tornado.web.UIModule):

    def render(self,username,navigation):
        return self.render_string('leave_detail.html',name = username,comfirm = 0,superiorStyle = 0)

class Confirm(tornado.web.UIModule):

    def render(self,username,navigation):
        return self.render_string('leave_detail.html',name = username,comfirm = 1,superiorStyle = 0)


class Changepwd(tornado.web.UIModule):
    def render(self,username):
        return self.render_string('change_pwd.html',name = username)


class Perdetail(tornado.web.UIModule):

    def render(self,username):
        return self.render_string('askforout.html',username = username)


class Statistic(tornado.web.UIModule):

    def render(self,username):
        return self.render_string('askforout.html',username = username)


class UncomfirmForOther(tornado.web.UIModule):

    def render(self,username):
         return self.render_string('leave_detail.html',name = username,comfirm = 0,superiorStyle = 1)


class ComfirmForOther(tornado.web.UIModule):

    def render(self,username):
         return self.render_string('leave_detail.html',name = username,comfirm = 1,superiorStyle = 1)

