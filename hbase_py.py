import happybase
import time
import random

batch_size = 1000
host = ""
file_path = "Request_for_Information_Cases.csv"
namespace = "sample_data"
row_count = 0
start_time = time.time()
table_name = "rfic"

# connection = happybase.Connection(host)
# connection.open()
# print(connection.tables())

#####
# start thrift
# /local/java/hbase/current/bin/hbase thrift start
#####

def connect_to_hbase():
    connection = happybase.Connection(host=host, table_prefix=namespace, table_prefix_separator=':', port=9090)
    connection.open()
    table = connection.table(name=table_name)
    batch = table.batch(batch_size=batch_size)
    return connection, table, batch

def insert_row(batch, row):
    batch.put(str(row), {"data:value": str(row+10)})
    print "Insert row %i" % (row)

def delete_row(batch, row):
    batch.delete(str(row))
    print "Delete row %i" % (row)

# Start to run
# connection, table, batch = connect_to_hbase()
pool = happybase.ConnectionPool(size=3, host=host, table_prefix=namespace, table_prefix_separator=':', port=9090)
with pool.connection() as connection:
    # print "Connect to HBase. batch size: %i" % (batch_size)
    print(connection.tables())
    table = connection.table(name=table_name)
    batch = table.batch(batch_size=batch_size)

    for row in range(1, 10000):
        insert_row(batch, row)

    batch.send()

#    with batch:
#        insert_row(batch, row)

#    delete_row(batch, row)
#    insert_row(batch, row)

# batch.send()

# read
# one_row = table.row(row='2')
# print(one_row['data:value'])
# for key, data in table.scan():
#    if key != '':
#        print(key, data)
        # print "Remove row %i" % int(key)
        # batch.delete(row=str(key))


# batch.send()

connection.close()
duration = time.time() - start_time
print "Done. duration: %.3f s" % (duration)
