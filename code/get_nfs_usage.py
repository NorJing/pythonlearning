#!/usr/bin/python

import subprocess
import sys

storage_info = subprocess.Popen(["df", "-h"], shell=True, stdout=subprocess.PIPE)
outputs = storage_info.communicate()[0].strip().split("\n")

for output in outputs:
    each = output.split()
    if len(each) > 1:
        if each[4].__contains__("/n01") or each[4].__contains__("/n02") or each[4].__contains__("/s01") or each[4].__contains__("/s02"):
            if len(sys.argv) > 1:
                if sys.argv[1] == "print":
                    print "share={0} usage={1}".format(each[4], each[3])

            percentage = each[3][:-1]
            path = "dwh_" + each[4].split("/")[1] + "_" + each[4].split("/")[2] + "_usage"
            subprocess.Popen(["/local/scripts/send_to_traverse.pl", percentage, path, "DWH storage usage"])

            hostname = subprocess.Popen(["hostname"], shell=True, stdout=subprocess.PIPE).communicate()[0].strip()
            fqdn = hostname + ".int.com"
            cmd = "test.create deviceName=" + fqdn + ", testType=external, subType=external, testName=" + path + ", interval=5m, units=percentage, warningThreshold=90, criticalThreshold=90, actionName=Critical_Alerts,  maxvalue=100, resultMultiplier=1, thresholdType=ascend"
            print cmd
