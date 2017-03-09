#!/usr/bin/env python

import os

docs = []
commands = []

with open(("./doc_version_id.txt"), mode='r') as f:
    for doc_version_id in f.readlines():
        command = "select main_document_id from document_version where document_version_id = '" + doc_version_id.lstrip("").rstrip("\n").rstrip(" ") + "';"
        print command
        commands.append(command)

# Write command to file
with open("./doc_group_id_commands.cql", mode='w') as f:
    f.write("use rapidokeyspace;\n")
    for each in commands:
        f.write(each + "\n")

# Run the cql file to get doc group id
os.system("/local/java/cassandra/apache-cassandra-1.0.12/bin/cqlsh < ./doc_group_id_commands.cql > ./doc_group_id.txt")

# Get exact doc group id
with open("./doc_group_id.txt", mode='r') as f:
    for doc in f.readlines():
        if (not doc.__contains__("main_")) and (not doc.__contains__("------------------------------------")):
            if not doc.startswith("\n"):
                print doc.lstrip("").rsplit("\n")[0]
                docs.append(doc.rsplit("\n")[0])

with open("./sync_doc_by_group_id.sh", mode='w') as f:
    f.write("#!/bin/bash\n\n")
    for doc in docs:
        # print doc
        command = "/local/java/jdk1.8.0_25/bin/java -jar /local/scripts/cassandra3_rapido/rapido-cassandra-data-migration-12.jar prod-dtc beta " + doc + "\n"
        # print command
        f.write(command)

os.system("chmod 755 ./sync_doc_by_group_id.sh")
os.system("./sync_doc_by_group_id.sh")