#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 11:13:34 2022

@author: guillaume.rivollier@Digital-Grenoble.local
"""

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Numeric

engine = create_engine("postgresql+psycopg2://wym_admin:admin@db:5432/postgres",
                       echo=False)


Base = declarative_base()
class User(Base):
    
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    message = Column(String)
        
    def to_postgres(self, engine):
        Session = sessionmaker(engine)  
        session = Session()
        session.add(self)  
        session.commit()

class Texte(Base):
    
    __tablename__ = 'texts'
    
    id = Column(Integer, primary_key=True)
    contenu = Column(String)
    resume = Column(String)
    date = Column(DateTime)
    delay = Column(Numeric)
        
    def to_postgres(self, engine):
        Session = sessionmaker(engine)  
        session = Session()
        session.add(self)  
        session.commit()



def read_DB_users(engine):
    l = []
    with engine.connect() as conn:
        select_statement = ("select * from users")
        result_set = conn.execute(select_statement)
        for r in result_set:
            l.append(dict(r))
    return json.dumps(l)

def read_DB_texts(engine):
    l = []
    with engine.connect() as conn:
        select_statement = ("select * from texts")
        result_set = conn.execute(select_statement)
        for r in result_set:
            l.append(dict(r))
    return l


if __name__ == '__main__':
    import pandas as pd
    pd.read_sql("select * from users",engine)
    with engine.connect() as conn:
        conn.execute("select * from users")
        resp = conn.fetchall()
        for row in resp:
            print(row)
      
    with engine.connect() as conn:

        select_statement = ("select * from users")
        result_set = conn.execute(select_statement)
        for r in result_set:
            print(r)
