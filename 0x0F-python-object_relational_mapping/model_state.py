#!/usr/bin/python3
'''the class definition of a State and
an instance Base = declarative_base()'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''the class definition of a State table'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement='ignore_fk')
    name = Column(String(128), nullable=False)
