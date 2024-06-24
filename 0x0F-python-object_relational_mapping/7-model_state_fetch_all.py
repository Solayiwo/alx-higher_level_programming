#!/usr/bin/python3
"""A script that lists all State objects from the database"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    for obj in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(obj.id, obj.name))
