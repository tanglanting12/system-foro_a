from oa_admin.oa.models import *
from oa_web.upload import uploadDir
import StringIO
import time
from xlrd import open_workbook
import datetime
from django.db.models import F;
class Leavedetalajax():
   def leavedetailajax(self):
        self.name = self.get_argument("name",default = "abert")
       # user=User.objects.filter(name__exact=name)
        self.index = self.get_argument("index",default = 0)
        self.lastpage = self.get_argument("lastpage",default = 0)
        self.comfirm = self.get_argument("comfirm",default=0)
        self.superiorStyle = self.get_argument("superiorStyle",default = 0)
        if (int(self.index) > 0):
            self.index = int(self.index)-1
        if self.superiorStyle == '1':
            subordinates = User.objects.filter(superior__name__exact = self.name)
            if self.comfirm =='1':
                self.leaves = Leave.objects.order_by("-create_time","leave_time_begin")\
                    .filter(verify_status__exact = 1,user__in = subordinates)
            else:
                self.leaves = Leave.objects.order_by("-create_time","leave_time_begin").filter\
                    (verify_status__exact = 0,user__in = subordinates)
        else :
            self.leaves = Leave.objects.order_by("-create_time","leave_time_begin")\
            .filter(user__name__exact = self.name,verify_status__exact = self.comfirm)
        if self.lastpage=='1':
            self.leavedetails = self.leaves.reverse()[:4]
        else:
            self.leavedetails = self.leaves[int(self.index)*4:(int(self.index)+1)*4]


class exceptiondataajax():

   def exceptiondataajax(self):
        self.name = self.get_argument("name",default = "abert")
       # user=User.objects.filter(name__exact=name)
        self.index = self.get_argument("index",default = 0)
        self.superiorStyle = self.get_argument("superiorStyle",default = 0)
        if (int(self.index) > 0):
            self.index = int(self.index)-1
        if self.superiorStyle == '1':
            print "lookup all exceptiondata"
            self.exceptiondatas = Attendance.objects.order_by("-daytime").exclude(musttime=F('realtime'))

        else :
            self.exceptiondatas = Attendance.objects.order_by("-daytime").filter(user__name__exact  = self.name)\
           .exclude(musttime=F('realtime'))

        self.exceptiondatas = self.exceptiondatas[int(self.index)*8:(int(self.index)+1)*8]

class upload():
    def uploadexcel(self):
         if self.request.files:
            for f in self.request.files['up_file']:
                rawname = f['filename']
                dstname = str(int(time.time()))+'.'+rawname.split('.').pop()
                dir = uploadDir()
                upfile = open(dir+"/"+dstname,'wb')
                upfile.write(f['body'])
                upfile=StringIO.StringIO(upfile.name);
                wb = open_workbook(upfile.read())
                for s in wb.sheets():
                    for row in range(1,s.nrows):
                        values=[]
                        for col in range(1,s.ncols):
                            values.append(s.cell(row,col).value)
                        users = User.objects.filter(name = values[0])
                        user =users[0] if users else None
                        # This code shoule be optimized
                        punchwork = str(values[2]).split(":")  if values[2] else None
                        punchworkoff = str(values[3]).split(":") if values[3] else None
                        latetime = str(values[6]).split(":") if values[6] else None
                        earlytime = str(values[7]).split(":") if values[7] else None
                        overtime = str(values[9]).split(":") if values[9] else None
                        worktime = str(values[11]).split(":") if values[11] else None

                        daytime = datetime.datetime.strptime(values[1],'%Y-%m-%d') if values[1] else None
                        punchwork = datetime.time(int(punchwork[0]),int(punchwork[1])) if values[2] else None
                        punchworkoff = datetime.time(int(punchworkoff[0]),int(punchworkoff[1]))  if values[3] else None
                        musttime = float(values[4]) if values[4] else None
                        realtime = float(values[5]) if values[5] else None
                        latetime = datetime.time(int(latetime[0]),int(latetime[1])) if values[6] else None
                        earlytime = datetime.time(int(earlytime[0]),int(earlytime[1])) if values[7] else None
                        isabsent = 1 if values[8] == 'True' else 0
                        overtime = datetime.time(int(overtime[0]),int(overtime[1])) if values[9] else None
                        apartment = values[10] if values[10] else None
                        worktime = datetime.time(int(worktime[0]),int(worktime[1])) if values[11] else None
                        remark = values[12] if values[12] else None

                        att = Attendance(user = user, daytime = daytime,punchwork=punchwork,punchworkoff=punchworkoff,
                            musttime=musttime,realtime=realtime,latetime=latetime,earlytime=earlytime,isabsent=isabsent,
                            overtime=overtime,apartment=apartment,worktime=worktime,remark=remark
                            )
                        if user is None:
                           att.name = values[0]
                        att.save()
                        print "create attendance success"
         self.finish("file" + upfile.read() + " is uploaded ok")