#!/usr/bin/python

import time
import pexpect

connection = "localhost:9997"
connection_timeout = 2

jmxterm = pexpect.spawn("java -jar /local/scripts/lib/jmxterm-1.0-alpha-4-uber.jar")
jmxterm.expect_exact("$>") # got prompt, we can continue
jmxterm.sendline("open " + connection)
jmxterm.expect_exact("#Connection to "+connection+" is opened", connection_timeout)

jmxterm.sendline("get -b kafka.server:name=MessagesInPerSec,type=BrokerTopicMetrics FiveMinuteRate")

response_lines = [] * 4
response_lines.append(jmxterm.readline())
response_lines.append(jmxterm.readline())
response_lines.append(jmxterm.readline())
response_lines.append(jmxterm.readline())

result = response_lines[3].replace(";", " ").strip().split(" ")
del result[1]
name, value = result

if "E-" in value:
    value = "0"

print "["+time.ctime()+"]", name, "=", value
jmxterm.sendline("quit")
