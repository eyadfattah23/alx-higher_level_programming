#!/usr/bin/python3
'''script that updates a state'''

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

    state_to_update = session.query(State).filter(
        State.id == 2).one_or_none()

    state_to_update.name = "New Mexico"

    session.add(state_to_update)
    session.commit()
