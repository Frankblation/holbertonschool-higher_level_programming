#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(username, password, database_name):
    """list states in database"""
    engine = create_engine(
        f'mysql://{username}:{password}@localhost:3306/{database_name}'
    )

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    list_states(username, password, database_name)
