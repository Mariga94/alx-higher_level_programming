#!/usr/bin/python3
import MySQLdb
from sys import argv

try:
    db = MySQLdb.connect(
            host="127.0.0.1",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3]
            )
    db.query("""SELECT id, name FROM states WHERE name LIKE "N%"
            ORDER BY id""")
    result = db.store_result()
    print(result.fetch_row(maxrows=2))
exception MySQLdb.Error as Error:
    print(Error)
