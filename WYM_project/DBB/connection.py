#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 11:13:34 2022

@author: guillaume.rivollier@Digital-Grenoble.local
"""

from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://wym_admin:admin@0.0.0.0:5432/postgres")
