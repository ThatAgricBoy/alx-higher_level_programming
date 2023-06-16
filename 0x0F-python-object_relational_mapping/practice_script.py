#!/usr/bin/python3

import MySQLdb
import os

username = 'samurai'
password = os.environ.get('MYSQL_PASSWORD')
database = 'samurai'

db = MySQLdb.connect(user=username, passwd=password, db=database)
cursor = db.cursor()

cursor.execute("SELECT * FROM `second_table`")

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
db.close()
