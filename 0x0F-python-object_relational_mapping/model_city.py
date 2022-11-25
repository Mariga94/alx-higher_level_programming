#!/usr/bin/python3
"""
Defines the City class.
Inherits from the Base Class.
"""
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Repesents a city for a MySQL database.
    Attributes:
    __tablename__ (str): The name if the MySQL table to store cities.
    id (sqlalchemy.Integer): The city's id
    name (sqlalchemy.String): the cities name
    state_id (sqlalchemy.Integer): city states id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
