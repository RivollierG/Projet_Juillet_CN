#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:21:01 2022

@author: guillaume.rivollier@Digital-Grenoble.local
"""

from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy import Table, inspect
from sqlalchemy import MetaData


def table_creation_users(engine):
    if not inspect(engine).has_table('users'):
        meta = MetaData()
        users = Table(
           'users', meta, 
           Column('id', Integer, primary_key = True), 
           Column('name', String), 
           Column('email', String),
           Column('phone', String),
           Column('message', String),
        )
        meta.create_all(engine)

def table_creation_texts(engine):
    if not inspect(engine).has_table('texts'):
        meta = MetaData()
        texts = Table(
           'texts', meta, 
           Column('id', Integer, primary_key = True), 
           Column('contenu', String), 
           Column('resume', String), 
           Column('date', DateTime),
           Column('delay', Numeric),
        )
        meta.create_all(engine)
