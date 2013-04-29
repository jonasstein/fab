#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""Description: fsql module
Handles low level DB instructions.
"""

import sqlite3
import sys

import unittest

class FabDatabase:
    """Class uppercase first letter, methods lowercase, underscore
    """

    def __init__(self, filename):
        """Connects to the given database. If such database does not exist, it will be created together with an empty table representid the data and another for address book properties mirroring a dictionary."""

        try:
            self.conn = sqlite3.connect(filename)
            self.conn.execute("""CREATE TABLE IF NOT EXISTS Data(
								ID INTEGER PRIMARY KEY,
								ContactID INTEGER,
								Type TEXT,
								Valid INTEGER,
								Priority INTEGER,
								Value TEXT,
								TimeStamp TEXT,
								Comment TEXT)""")
            self.conn.execute("""CREATE TABLE IF NOT EXISTS Properties(
                                Key TEXT,
                                Value TEXT)""")
            self.conn.commit()

        except sqlite3.OperationalError:
            print("OperationalError")

        except sqlite3.DatabaseError:
            print("DatabaseError: file is encrypted or is not a database")

        except RuntimeError:
            print("Runtime Error: Could not create new database.")

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def delete_DB(self):
        """Delete the database. Close first.
        """

    def store_row(self, registry):
        """Inserts a registry from the data table. Registry must be a tuple.
        """
        self.conn.execute("INSERT INTO Data VALUES (?,?,?,?,?,?,?)", registry)
        self.conn.commit()

    def erase_row(self,ID):
        """Erases a row.
        """
        self.conn.execute( "DELETE FROM Data WHERE ID = ?", [ID,])
        self.conn.commmit()

    def erase_contact(self, ContactID):
        """Removes all the entries associated with the given ContactID."""

        self.conn.execute("DELETE FROM Data WHERE ContactID = ?", [ContactID,])
        self.conn.commit()

    def read(self):
        """given a set of attr. and ID's return such attr. of ID's
        """

    def search(self):
        """
        """

    def maxContactID(self):
        """Returns the value of the highest ContactID on the DB."""
        pass


class FabDatabaseTest(unittest.TestCase):
    """Unittesting database management."""

    def setUp(self):
        self.db = FabDatabase("test.db")

    def test_insert(self):
        """Testing row insertion."""
        pass

    def test_remove(self):
        """Testing row removal."""
        pass

if __name__ == "__main__":
    unittest.main()
