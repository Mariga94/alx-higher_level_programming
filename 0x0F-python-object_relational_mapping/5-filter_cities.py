#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
              FROM `cities` as `c` \
              INNER JOIN `states` AS `s` \
              ON `c`.`state_id`=`s`.`id` \
              ORDER BY `c`.`id`")
    states = c.fetchall()
    my_city = list()
    for state in states:
        if "{}".format(sys.argv[4]) in state:
            my_city.append(state[2])
    print(', '.join(my_city))
