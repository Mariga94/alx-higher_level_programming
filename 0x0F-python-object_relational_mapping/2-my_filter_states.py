#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name = %s", [sys.argv[4]])
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
