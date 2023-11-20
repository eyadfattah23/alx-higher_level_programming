#!/usr/bin/python3
'''script that lists all State objects from the database hbtn_0e_14_usa'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    records = session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id).order_by(City.id).all()

    for record in records:
        print(f'{record[0]}: ({record[1]}) {record[2]}')
