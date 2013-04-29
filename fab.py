#!/usr/bin/env python
#  -*- coding: utf-8 -*-

__version__ = 0.01
__author__ = "Jonas Stein"
__contributors__ = "Ignacio Vergara"

"""Description:
"""

from fsql import FabDatabase

class Data(object):
    """Basic data entity to store information. Mirrors the Data table in the database and provides higher level functionality."""

    def __init__(self, db, ID = None):
        """If ID is given, reads such entry from the DB, else it is treated as a new entry and an ID is assigned."""

        self.properties = {} # Suggestion to use a dictionary
        self.db = db

        if ID:
            self.ID = ID
            self.db.read(self.ID)

        else:
            #Ask DB which is the bigest ID already in use
            self.ID = self.db.max_ID()+1

    def save(self):
        """Calls for self.db.store_row() as pertinent."""
        pass

class Contact(object):
    """Class abstracting the whole contact information.
	It is composed by a set/list of Data object instances
	representing all the pertinent entries for a contact."""

    def __init__(self, db, ContactID = None):
        """When called without ContactID, assigns a new one."""

        self.db = db #passing the reference to the db

        if ContactID:
            self.ContactID = ContactID
            # Load all the data for such ContactID
            self.load()

        else:
            #Ask DB which is the biggest ContactID already in use.
            self.ContactID = self.db.max_contact_ID()+1

    def load(self):
        """Loads all the entries for the given contact as multiple Data instances in registries."""

        self.entries = []
        pass

    def delete(self):
        """Removes the whole contact from the DB."""
        self.db.erase_contact(self.ContactID)

    def save(self):
        """Invokes the save method on each data entry."""
        for entry in self.entries:
            entry.save()

class AddressBook(object):

    def __init__(self, name):
        """name: Name of the address book, also used as filename for the DB"""
        self.name = name
        self.db = FabDatabase(name + '.db')
        self.Contacts = []
        self.properties = {'name': self.name }

    def add_contact(self):
        self.Contacts.append(Contact(self.db))

if __name__ == "__main__":
    fab = AddressBook('test')
