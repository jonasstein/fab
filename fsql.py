#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""Description: fsql module
Handles low level DB instructions.
"""

import sqlite3
import sys

class FabDatabaseError:
    pass

class FabDataset:
    def __init__(self):
        self.fields = {}
    pass

class FabDatabase:
    """Represents a database for the fab addressbook.
    """
    
    # fields are specified as (key, SQL type) pairs
    FAB_FIELDS = [("ID", "INTEGER PRIMARY KEY"),
                  ("ContactID", "INTEGER"),
                  ("Type", "TEXT"),
                  ("Valid", "INTEGER"),
                  ("Timestamp", "TEXT"),
                  ("Comment", "TEXT")]
                   
    def __init__(self, filename):
        """Connects to the given database. If such database does not exist, it will be created together with an empty table representid the data and another for address book properties mirroring a dictionary."""

        try:
            self._conn = sqlite3.connect(filename)
            sql_command = "CREATE TABLE IF NOT EXISTS Data("
            sql_command = sql_command + ", ".join([" ".join(x) for x in FabDatabase.FAB_FIELDS]) + ")"
            self._conn.execute(sql_command)
            
            # TODO: create 2nd table for metadata
            #self._conn.execute("""CREATE TABLE IF NOT EXISTS Properties(
            #                    Key TEXT,
            #                    Value TEXT)""")
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
        """Inserts a registry from the data table. Registry must be a dictionary.
        """
        template = ",".join(["?"] * len(FabDatabase.FAB_FIELDS)) # generate "?,?,?,?"
        values = [registry[key] for key, _ in FabDatabase.FAB_FIELDS] # generate values in order
        self._conn.execute("INSERT INTO Data VALUES (" + template + ")", values)
        self._conn.commit()

    def get_row(self, ID):
        """Get the dataset with the ID 'ID'. Returns a dictionary."""
        
        #assume unique ID - take first query result
        tupel = self._conn.execute("SELECT * FROM Data WHERE ID = ?",[ID,]).next()
        
        #build dictionary with keys given in FAB_FIELDS
        result = {}
        for fabfield, value in zip(FabDatabase.FAB_FIELDS, tupel):
            key = fabfield[0]
            result[key] = value
        return result

    def erase_row(self,ID):
        """Erases a row.
        """
        self._conn.execute( "DELETE FROM Data WHERE ID = ?", [ID,])
        self._conn.commit()

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


