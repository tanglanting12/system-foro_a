import tornado.web

from oa_admin.oa.models import User, Role ,Leave
class Ask_for_leave(tornado.web.UIModule):
    def render(self,username):
           users = User.objects.filter(name=username)
           superiors=User.objects.filter(id=users[0].superior)
          #roler = Role.objects.filter(user__name__exact=self.current_user)
           return self.render_string('ask_for_leave.html',pre_year_holiday=users[0].pre_year_holiday,
                                     remain_year_holiday=users[0].remain_year_holiday,
                                      superior_id=superiors[0].id,superior_name=superiors[0].name)


class Ask_for_out(tornado.web.UIModule):
    def render(self,username):
        return self.render_string('ask_for_out.html',username=username)

class  Default_child(tornado.web.UIModule):
    def render(self,username):
        return self.render_string('test.html')
    def html_body(self):
        return "<script>document.write(\"Hello!\")</script>"
    def embedded_javascript(self):
        return "document.write(\"hi!\")"