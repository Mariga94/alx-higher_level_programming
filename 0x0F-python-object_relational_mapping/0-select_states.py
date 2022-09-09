#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    db.query("""
    SELECT id, name
    FROM states
    ORDER BY id ASC""")
    result = db.store_result()
    states = result.fetch_row(maxrows=0)
    for state in states:
        print(state)
