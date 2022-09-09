#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches argument
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name = %s", [argv[4]])
    states = cur.fetchall()
    for state in states:
        print(state)
