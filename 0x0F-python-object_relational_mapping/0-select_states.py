#!/usr/bin/python3
from MySQLdb import _mysql
-- a script that lists all states from the database hbtn_0e_0_usa
db=_mysql.connect(port=3306, user="joebob",
                  password="moonpie",database="hbtn_0e_0_usa")
db.query("""SELECT * FROM states ORDER BY id ASC""")
