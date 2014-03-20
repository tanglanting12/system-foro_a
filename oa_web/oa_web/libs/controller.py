from oa_admin.oa.models import *
from oa_web.config import ConfigCommon

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
                self.leaves = Leave.objects.filter(verify_status__exact = 1,user__in = subordinates)
            else:
                self.leaves = Leave.objects.filter(verify_status__exact = 0,user__in = subordinates)
        else :
            self.leaves = Leave.objects.order_by("create_time","leave_time_begin")\
            .filter(user__name__exact = self.name,verify_status__exact = self.comfirm)
        if self.lastpage=='1':
            self.leavedetails = self.leaves.reverse()[:ConfigCommon.pagingnum]
        else:
            self.leavedetails = self.leaves[int(self.index)*ConfigCommon.pagingnum:(int(self.index)+1)*ConfigCommon.pagingnum]