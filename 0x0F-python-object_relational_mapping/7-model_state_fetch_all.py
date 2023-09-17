#!/usr/bin/python3
import sys
from model_state import Base, State
'''script that lists all State objects from the database hbtn_0e_6_usa'''
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    records = session.query(State).order_by(State.id).all()
    for record in records:
        print(f"{record.id}: {record.name}")
