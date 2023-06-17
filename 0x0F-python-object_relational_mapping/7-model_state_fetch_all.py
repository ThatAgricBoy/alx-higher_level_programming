#!/usr/bin/python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa
"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:
{}@localhost:3306/{}'.format(mysql_username, mysql_password,
                             mysql_db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id,
                              state.name))
