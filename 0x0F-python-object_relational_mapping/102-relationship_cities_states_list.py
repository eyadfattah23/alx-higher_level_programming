#!/usr/bin/python3
''' script that lists all City objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa'''
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    cits = session.query(City).order_by(City.id).all()
    for city in cits:
        print(f'{city.id}: {city.name} -> {city.state.name}')
