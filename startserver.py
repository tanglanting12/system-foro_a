#!/usr/bin/python
#start web tornado server and dgango server
"""

"""
import os.path as osp
import os
import sys
import subprocess
path = osp.abspath(osp.dirname(__file__))
tornadoserverpath = path+'/oa_web'
dgangoserverpath = path+'/oa_admin'
pythonenv = path+'/ENV/bin/python'
#add sys.path for tornado dgango
sys.path.append(tornadoserverpath)
sys.path.append(dgangoserverpath)
#fork process for run.py   and then exec manage.
print "%s" %(sys.argv[0])
#start nginx
#print "start nginx server......" 
#subprocess.Popen('/usr/local/nginx/sbin/nginx' ,shell=True)
#print "nginx server  success operating......" 

#print "start oa_web_torando server......"
#subprocess.Popen('ENV/bin/python %s/run.py "--port=9000"' %tornadoserverpath,shell=True)
#print "tornado server  success operating......" 

print "start oa_admin_Dgango server......" 
os.system('ENV/bin/python %s/manage.py "runserver"' %dgangoserverpath)
print "oa_admin_Dgango server  success operating......" 

