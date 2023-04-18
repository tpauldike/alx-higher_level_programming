#!/usr/bin/python3
"""
This script defines a City class
to work with MySQLAlchemy ORM.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class `City`, a sub-class of Base.
    Attributes:
        __tablename__ (str): The city's table name
        id (int): The city's id
        name (str): The city's name
        state_id (int): The state where the city is found
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
