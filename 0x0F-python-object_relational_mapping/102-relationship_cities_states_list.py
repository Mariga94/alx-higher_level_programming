#!/usr/bin/python3
"""Lists all `City` objects form the database `hbtn_0e_101_usa`"""
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()
    for city in cities:
        print("{} -> {}".format(city.name, city.state.name))
