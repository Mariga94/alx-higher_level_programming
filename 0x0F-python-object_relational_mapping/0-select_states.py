#!/usr/bin/python3
from sys import argv
import MySQLdb
try:
    db = MySQLdb.connect(
            host='127.0.0.1',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    states = cur.fetchmany(5)
    print(states)
except MySQLdb.Error as Error:
    print(Error)
