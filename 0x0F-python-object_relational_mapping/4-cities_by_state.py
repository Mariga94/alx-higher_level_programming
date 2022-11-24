#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            db='hbtn_0e_4_usa')

    cur = db.cursor()
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                 INNER JOIN `states` as `s` \
                 ON `c`.`state_id` = `s`.`id` \
                 ORDER BY `c`.`id`")
    cities = cur.fetchall()
    for city in cities:
        print(city)
