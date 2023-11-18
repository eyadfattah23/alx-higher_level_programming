#!/usr/bin/python3
'''script that lists objects.id with the name passed as argument
from the database hbtn_0e_6_usa'''

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_search = sys.argv[4]

    states = session.query(State.id).filter(
        State.name.like(state_to_search)).all()

    if states:
        for state in states:
            print(state.id)
            break
    else:
        print('Not found')
