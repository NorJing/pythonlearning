#!/usr/bin/python

import pexpect
import time

timestamp = int(time.time())
prefix = "pre_production.undefined.fqdn"
metrics = [
    "kafka.server.brokertopicmetrics.messagesinpersec.fiveminuterate",
    "kafka.server.brokertopicmetrics.bytesinpersec.fiveminuterate",
    "kafka.server.brokertopicmetrics.bytesoutpersec.fiveminuterate",
    "kafka.server.replicamanager.underreplicatedpartitions.value",
    "kafka.server.kafkacontroller.offlinepartitionscount.value",
    "kafka.server.requestMetrics.totaltimems.fetchconsumer.mean",
    "kafka.server.requestmetrics.requestspersec.fetchconsumer.fiveminuterate"
]
beans = [
    "kafka.server:type=BrokerTopicMetrics,name=MessagesInPerSec FiveMinuteRate",
    "kafka.server:type=BrokerTopicMetrics,name=BytesInPerSec FiveMinuteRate",
    "kafka.server:type=BrokerTopicMetrics,name=BytesOutPerSec FiveMinuteRate",
    "kafka.server:type=ReplicaManager,name=UnderReplicatedPartitions Value",
    "kafka.controller:type=KafkaController,name=OfflinePartitionsCount Value",
    "kafka.network:type=RequestMetrics,name=TotalTimeMs,request=FetchConsumer Mean",
    "kafka.network:type=RequestMetrics,name=RequestsPerSec,request=FetchConsumer FiveMinuteRate"
]
connection = "fqdn:9997"
connection_timeout = 2

jmxterm = pexpect.spawn("java -jar jmxterm-1.0-alpha-4-uber.jar")
jmxterm.expect_exact("$>")
jmxterm.sendline("open " + connection)
jmxterm.expect_exact("#Connection to "+connection+" is opened", connection_timeout)
i = 0
for bean in beans:
    # print bean
    command = "{0} {1}".format("get -b", bean)
    # print command
    jmxterm.sendline(command)
    response_lines = []
    # readline three time first to pass no useful info
    jmxterm.readline()
    jmxterm.readline()
    jmxterm.readline()
    response_lines.append(jmxterm.readline())
    # print response_lines
    result = response_lines[0].replace(";", " ").strip().split(" ")
    del result[1]
    name, value = result
    if "E-" in value:
        value = "0"

    output = "{0}.{1} {2} {3}".format(prefix, metrics[i], value, timestamp)
    print output
    i = i + 1

jmxterm.sendline("quit")


