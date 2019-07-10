#!/usr/bin/python
# coding: utf-8

__author__ = "Leonid Pshennikov"


import sys
import random
import MySQLdb

from shutil import copyfile


mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_user = "root"
mysql_password = "test1234"
mysql_database = "lpt_prom"


print("1")
record_name = sys.argv[1]
process_id = str(random.randint(1, 9999999))

conn = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_password, db=mysql_database)
print("2")
x = conn.cursor()

print("3")
try:
    print("4")
    sql1 = "update record_name set status = 1, process_id = " + process_id + " where status=0 and timestamp < now();"
    print(sql1)
    x.execute(sql1)
    conn.commit()

    sql2 = "select * from record_name where status = 1 and process_id = " + process_id + ";"
    print(sql2)
    x.execute(sql2)
    raw = x.fetchmany(1000)
    print(raw)
    print("5")
    for s in raw:
        print(s[1])
 #       copyfile("/var/log/freeswitch/records/" + s[1] + ".wav", "/sound/" + s[1] + ".wav")
        print("5.1")
    print("5.2")

    conn.commit()
    print("6")
    sql3 = "update record_name set status = 2 where status = 1 and process_id = " + process_id + ";"
    print(sql3)
    x.execute(sql3)
    conn.commit()

except:
    conn.rollback()

conn.close()
