#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """Get MySQL username, password, and database name from command line arguments
"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db_name = sys.argv[3]

    """Create engine and session"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(mysql_username, mysql_password, mysql_db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query all State objects and sort by id"""
    states = session.query(State).order_by(State.id).all()

    """Print results"""
    for state in states:
        print('{}: {}'.format(state.id, state.name))
