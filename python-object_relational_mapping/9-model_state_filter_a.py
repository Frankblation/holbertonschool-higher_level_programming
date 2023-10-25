#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print the first State object where the name contains 'a'
    first_state = session.query(State).filter(State.name.like('%a%')).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("No state found with 'a' in the name.")
    session.close()
