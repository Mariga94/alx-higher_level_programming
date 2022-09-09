#!/usr/bin/python3
import MySQLdb
from sys import argv
"""
Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3])
db.query("""
    SELECT id, name FROM states
    WHERE name LIKE "N%"
    ORDER BY id ASC
    """)
result = db.store_result()
rows = result.fetch_row(maxrows=2)
for row in rows:
    print(row)
