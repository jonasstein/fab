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
        try:
            self.conn = sqlite3.connect(filename)
        except RuntimeError:
            print("Runtime Error: Could not create new database.")


    def delete_DB(self):
        """delete the file from the database. Close first.
        """

    def init_table(self):
        """create new table, if there was no db before
        """
        try:
            self.conn.execute("CREATE TABLE IF NOT EXISTS data(
								ID INTEGER PRIMARY KEY,
								UserID INTEGER,
								Type TEXT,
								Valid INTEGER,
								Priority INTEGER,
								Value TEXT,
								TimeStamp TEXT,
								Comment TEXT)")

        except sqlite3.OperationalError:
            print("OperationalError")
        except sqlite3.DatabaseError:
            print("DatabaseError: file is encrypted or is not a database")
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

    def store_row(self, registry):
        """Inserts a registry from the data table.
        """
        self.conn.execute("INSERT INTO data VALUES (?,?,?,?,?,?,?)", registry)
        self.conn.commit()

    def erase_row(self,ID):
        """Erases a row.
        """
        self.conn.execute( "DELETE from data where ID = ? ", ID)
        self.conn.commmit()

    def read(self):
        """given a set of attr. and ID's return such attr. of ID's
        """

    def search(self):
        """
        """

	 def maxContactID(self):
		"""Returns the value of the highest ContactID on the DB."""
		pass

    def __del__(self):
        self.conn.commit()
        self.conn.close()

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
