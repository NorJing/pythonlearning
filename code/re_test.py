#!/usr/bin/python
import re

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

for bean in beans:
    print bean
    if "kafka.server" in bean:
        matchObj = re.match(r'kafka.server:type=(.*),name=(.*) (.*)', bean, re.M|re.I)
        if matchObj:
            metric = "{0}.{1}.{2}.{3}".format("kafka.server", matchObj.group(1).lower(),
                                              matchObj.group(2).lower(), matchObj.group(3).lower())
            print metric
        else:
            print "No kafka server match!!"
    elif "kafka.controller" in bean:
        matchObj = re.match(r'kafka.controller:type=(.*),name=(.*) (.*)', bean, re.M|re.I)
        if matchObj:
            metric = "{0}.{1}.{2}.{3}".format("kafka.controller", matchObj.group(1).lower(),
                                              matchObj.group(2).lower(), matchObj.group(3).lower())
            print metric
        else:
            print "No kafka controller match!!"
    elif "kafka.network" in bean:
        matchObj = re.match(r'kafka.network:type=(.*),name=(.*),request=(.*) (.*)', bean, re.M|re.I)
        if matchObj:
            metric = "{0}.{1}.{2}.{3}.{4}".format("kafka.network", matchObj.group(1).lower(),
                                                  matchObj.group(2).lower(),
                                                  matchObj.group(3).lower(),
                                                  matchObj.group(4).lower())
            print metric
        else:
            print "No kafka network match!!"
