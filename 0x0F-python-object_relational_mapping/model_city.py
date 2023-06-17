#!/usr/bin/python3
"""
Script that uses the declarative base from sqlalchemy
"""

from sqlalchemy import Column, Interger, String
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

engine = create_engine('mysql+mysqldb://argv[1]:argv[2]@localhost:3306/argv[3])

Base = declarative_base()

class State(Base):
   __tablename__ = 'states'

   id = Column(Interger, primary_key=True, autoincrement=True, nullable=False)
   name = Column(String,(128), nullable=False)
