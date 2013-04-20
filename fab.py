#!/usr/bin/env python
#  -*- coding: utf-8 -*- 

__version__ = 0.01 
__author__ = "Jonas Stein"
__contributors__ = "Ignacio Vergara"

"""Description:
""" 

from fsql import FabDatabase

class Data(object):

	self.ID = None
	self.UserID = None
	self.Type = None
	self.Valid = None
	self.Priority = None
	self.Value= None
	self.TimeStamp = None
	self.Comment = None

	def __init__(self):
		pass
		

class Contact(object):
	"""Class abstracting the whole contact information.
	It is composed by a set/list of Data object instances
	representing all the pertinent entries for a contact."""
	
	self.ID = None	
	self.entries = []

	def __init__(self):
		pass
	
	def load(self):
		"""Loads all the entries for the given contact."""
		pass
	
	def delete(self):
		"""Removes the whole contact from the DB."""
		pass
	
	
def main():
    fdb = FabDatabase("fab.db") 
    fdb.init_table()

if __name__ == "__main__":
    main()
