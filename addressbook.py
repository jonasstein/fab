#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import unittest

from fsql import FabDatabase

class Data(object):
    """Basic data entity to store information. Mirrors the Data table in the database and provides higher level functionality."""

    def __init__(self, db, ID = None):
        """If ID is given, reads such entry from the DB, else it is treated as a new entry and an ID is assigned."""

        self.properties = {} # Suggestion to use a dictionary
        self.db = db

        self.Value = None
        self.Type = None
        self.Comment = None
        self.Timestamp = None
        self.Priority = None

        if ID:
            self.ID = ID
            self.db.read(self.ID)

        else:
            #Ask DB which is the bigest ID already in use
            self.ID = self.db.max_ID()+1

    def save(self):
        """Call for self.db.store_row() as pertinent."""
        pass

    def delete(self):
        self.db.erase_row(self.ID)

    def __str__(self):
        return """Data
                Type: %s
                Value: %s
                Comment: %s
                Timestamp: %s""" % (self.Type, self.Value, self.Comment, self.Timestamp)

class DataTest(unittest.TestCase):

    def setUp(self):
        self.db = FabDatabase(':memory:')

    def test_new(self):
        """No ID given."""
        pass

    def test_old1(self):
        """ID given which exist in the DB."""
        pass

    def test_old2(self):
        """ID given which does not exist in the DB."""
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

class ContactTest(unittest.TestCase):

    def test_new(self):
        """No ContactID given."""
        pass

    def test_old1(self):
        """ContactID given which exist in the DB."""
        pass

    def test_old2(self):
        """ContactID given which does not exist in the DB."""
        pass

class AddressBook(object):

    def __init__(self, name):
        """name: Name of the address book, also used as filename for the DB"""
        self.name = name
        self.db = FabDatabase(name + '.db')
        self.Contacts = []
        self.properties = {'name': self.name }

    def add_contact(self):
        self.Contacts.append(Contact(self.db))

    def importing(self, name, formating):
        pass

    def exporting(self, name, formating):
        pass

class AddressBookTest(unittest.TestCase):

    def test_add_contact(self):
        pass

if __name__ == "__main__":
    unittest.main()
