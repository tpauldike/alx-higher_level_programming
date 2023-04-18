#!/usr/bin/python3
""" lists all cities objects from the database hbtn_0e_6_usa """

from sys import argv
from sqlalchemy import create_engine
from model_city import City
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
