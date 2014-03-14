from oa_admin.oa.models import *
from oa_web.config import ConfigCommon

def leavedetailajax(self):
        name=self.get_argument("name",default="abert")
       # user=User.objects.filter(name__exact=name)
        index = self.get_argument("index",default=0)
        lastpage = self.get_argument("lastpage",default=0)
        comfirm = self.get_argument("comfirm",default=0)
        superiorStyle = self.get_argument("superiorStyle",default=0)
        if (index!=0):
            index=int(index)-1
        if superiorStyle == '1':
            subordinates=User.objects.filter(superior__name__exact=name)
            if comfirm =='1':
                leaves=Leave.objects.filter(verify_status__exact=1,user__in=subordinates)
            else:
                leaves=Leave.objects.filter(verify_status__exact=0,user__in=subordinates)

        else :
            leaves=Leave.objects.order_by("create_time","leave_time_begin")\
            .filter(user__name__exact=name,verify_status__exact=comfirm)
        if lastpage=='1':
            leavedetails=leaves.reverse()[:ConfigCommon.pagingnum]
        else:
            leavedetails=leaves[index*ConfigCommon.pagingnum:(index+1)*ConfigCommon.pagingnum]
        self.render('leave_detailajax.html',leavedetails=leavedetails,name=name,comfirm=comfirm
                    ,superiorStyle=superiorStyle,index=index,lastpage=lastpage)