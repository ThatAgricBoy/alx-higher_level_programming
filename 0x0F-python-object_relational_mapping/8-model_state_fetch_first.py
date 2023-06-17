#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """ Get MySQL username, password, and
    database name from command
    line arguments"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db_name = sys.argv[3]

    """Create engine and session"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_username, mysql_password,
                                  mysql_db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query for the first State object and print its name"""
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(state.id, state.name))
