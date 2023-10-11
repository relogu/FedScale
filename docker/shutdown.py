import argparse
import os
import sys
import time

# FIXME: put the monitor shutdown

job_name = sys.argv[1]


if job_name == 'all':
    os.system("ps -ef | grep nvidia-smi | grep query > nvidia_monitor_running_temp")
else:
    os.system("ps -ef | grep nvidia-smi | grep query | grep {} > nvidia_monitor_running_temp".format(job_name))
[os.system("kill -9 "+str(l.split()[1]) + " 1>/dev/null 2>&1") for l in open("nvidia_monitor_running_temp").readlines()]
os.system("rm nvidia_monitor_running_temp")

time.sleep(2)

if job_name == 'all':
    os.system("ps -ef | grep python | grep FedScale > fedscale_running_temp")
else:
    os.system("ps -ef | grep python | grep job_name={} > fedscale_running_temp".format(job_name))
[os.system("kill -9 "+str(l.split()[1]) + " 1>/dev/null 2>&1") for l in open("fedscale_running_temp").readlines()]
os.system("rm fedscale_running_temp")
