#!/usr/bin/python3
'''script that adds a new state'''

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

    new_state = State(name='Louisiana')
    session.add(new_state)

    session.commit()

    records = session.query(State.id).filter(
        State.name == 'Louisiana').one_or_none()

    if records:
        print(f'{records.id}')
    else:
        print('Not found')
