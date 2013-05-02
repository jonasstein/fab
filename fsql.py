#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""Description: fsql module
Handles low level DB instructions.
"""

import sqlite3
import sys

class FabDatabaseError:
    pass

class FabDatabase:
    """Class uppercase first letter, methods lowercase, underscore
    """

    def __init__(self, filename):
        """Connects to the given database. If such database does not exist, it will be created together with an empty table representid the data and another for address book properties mirroring a dictionary."""

        try:
            self._conn = sqlite3.connect(filename)
            self._conn.execute("""CREATE TABLE IF NOT EXISTS Data(
								ID INTEGER PRIMARY KEY,
								ContactID INTEGER,
								Type TEXT,
								Valid INTEGER,
								Priority INTEGER,
								Value TEXT,
								TimeStamp TEXT,
								Comment TEXT)""")
            self._conn.execute("""CREATE TABLE IF NOT EXISTS Properties(
                                Key TEXT,
                                Value TEXT)""")
            self._conn.commit()

        except sqlite3.OperationalError:
            print("OperationalError")
            raise FabDatabaseError

        except sqlite3.DatabaseError:
            print("DatabaseError: file is encrypted or is not a database")
            raise FabDatabaseError

    def __del__(self):
        self._conn.commit()
        self._conn.close()

    def delete_DB(self):
        """Delete the database. Close first.
        """
        pass

    def store_row(self, registry):
        """Inserts a registry from the data table. Registry must be a tuple.
        """
        self._conn.execute("INSERT INTO Data VALUES (?,?,?,?,?,?,?,?)", registry)
        self._conn.commit()

    def erase_row(self,ID):
        """Erases a row.
        """
        self._conn.execute( "DELETE FROM Data WHERE ID = ?", [ID,])
        self._conn.commmit()

    def erase_contact(self, ContactID):
        """Removes all the entries associated with the given ContactID."""

        self._conn.execute("DELETE FROM Data WHERE ContactID = ?", [ContactID,])
        self._conn.commit()

    def read(self):
        """given a set of attr. and ID's return such attr. of ID's
        """

    def search(self):
        """
        """

    def maxContactID(self):
        """Returns the value of the highest ContactID on the DB."""
        pass


