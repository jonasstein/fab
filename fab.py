#!/usr/bin/env python
#  -*- coding: utf-8 -*-

__version__ = 0.01
__author__ = "Jonas Stein"
__contributors__ = "Ignacio Vergara"

"""Description: This is the main program of the "Flexible Address Bookl"
It should be executed in a python 2.7 interpreter.
"""

from adressbook import AddressBook

if __name__ == "__main__":
    print 'Loading database: test'
    fab = AddressBook('test')
