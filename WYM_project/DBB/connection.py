#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 11:13:34 2022

@author: guillaume.rivollier@Digital-Grenoble.local
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("postgresql+psycopg2://wym_admin:admin@0.0.0.0:5432/postgres",
                       echo=True)


Base = declarative_base()
class User(Base):
    
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(Integer)
    message = Column(String)
        
    def to_postgres(self, engine):
        Session = sessionmaker(engine)  
        session = Session()
        session.add(self)  
        session.commit()

        

if __name__ == '__main__':
    import pandas as pd
    pd.read_sql("select * from users",engine)
