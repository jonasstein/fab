#!/usr/bin/env python
#  -*- coding: utf-8 -*- 

__version__ = 0.01 
__author__ = "Jonas Stein"
__contributors__ = ""

"""Description:
""" 

import sqlite3
from fsql import FabDatabase


def main():
    fdb = FabDatabase() #if there is a init it would be called here
    fdb.create_DB("fab.db")



if __name__ == "__main__":
    main()
