#!/usr/bin/python

import subprocess
import sys
import os

cassandra_list = []
with open("beta_cassandra_list", 'r') as f:
    for server in f.readlines():
        # stop each cassandra
        server = server.strip("\n")
        print(server)
        pre = "pcadmin@"
        connnect = pre + server
        print(connnect)
        output = subprocess.Popen(["ssh", "-o", "StricthostKeyChecking=no", connnect, "/local/scripts/cassandra start"], stdout=subprocess.PIPE)
        print(output.communicate()[0])
        # output = subprocess.Popen(["ssh", "-o", "StricthostKeyChecking=no", connnect, "/local/scripts/cassandra status"], stdout=subprocess.PIPE)
        # print(output.communicate()[0])
        # server = server.split(".")[0]
        # print(server)
        # path = "/data/" + server + "/data/system/LocationInfo*"
        # print(path)
        # output = subprocess.Popen(["ls", path], stdout=subprocess.PIPE)
        # print(output.communicate()[0])