#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db.connect(
            host='127.0.0.1',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM `cities` ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
