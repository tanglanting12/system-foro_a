#!/usr/bin/python
#start web tornado server and dgango server
"""

"""
import os.path as osp
import os
import sys
import subprocess
path = osp.abspath(osp.dirname(__file__))
tornadoserverpath = path+'/pinhui_oa/oa_web'
dgangoserverpath = path+'/pinhui_oa/oa_admin'
pythonenv = path+'/env/bin/python'
#add sys.path for tornado dgango
sys.path.append(tornadoserverpath)
sys.path.append(dgangoserverpath)
#fork process for run.py   and then exec manage.
print "%s" %(sys.argv[0])
#start nginx
print "start nginx server......" 
subprocess.Popen('/usr/local/nginx/sbin/nginx',shell=True)
print "nginx server  success operating......" 

print "start oa_web_torando server......" 
subprocess.Popen('env/bin/python %s/run.py' %tornadoserverpath,shell=True)
print "tornado server  success operating......" 

print "start oa_admin_Dgango server......" 
os.system('env/bin/python %s/manage.py "runserver"' %dgangoserverpath)
print "oa_admin_Dgango server  success operating......" 

