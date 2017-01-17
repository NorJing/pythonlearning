#!/usr/bin/env python

import os
import subprocess
import logging

logging.basicConfig(filename="/local/logs/esb/restart_esb-app-umm2newsml-default.log", format='%(levelname)s:%(asctime)s:%(message)s', filemode='a', level=logging.INFO, datefmt='%Y-%m-%d-%I-%M-%S')

def check_umm2_log_and_restart():
    """
    Run on Python 2.6.6 and on c301mag
    This is a scripts to check if  esb-app-umm2newsml-default.log and esb-app-umm2newsml-default.out are existed on the c301mag
    """
    if os.path.exists("/local/logs/esb/esb-app-umm2newsml-default.out") and os.path.exists("/local/logs/esb/esb-app-umm2newsml-default.log"):
        print "Both logs exists"
    else:
        # restart esb-app-umm2newsml-default
        subprocess.call("sudo stop esb-app-umm2newsml-default", shell=True)
        subprocess.call("sudo start esb-app-umm2newsml-default", shell=True)
        logging.info("esb-app-umm2newsml-default is restart")

if __name__ == '__main__':
    check_umm2_log_and_restart()
