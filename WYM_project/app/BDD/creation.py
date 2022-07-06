#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:21:01 2022

@author: guillaume.rivollier@Digital-Grenoble.local
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, inspect
from sqlalchemy import MetaData


def data_base_creation(engine):
    if not inspect(engine).has_table('users'):
        meta = MetaData()
        users = Table(
           'users', meta, 
           Column('id', Integer, primary_key = True), 
           Column('name', String), 
           Column('email', String),
           Column('phone', Integer),
           Column('message', String),
        )
        meta.create_all(engine)
