#!/usr/bin/env python
#  -*- coding: utf-8 -*- 

"""Description: fsql module
""" 

import sqlite3
import sys

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
            self.conn.execute("CREATE TABLE data" +
                              "(ID UserID Type Valid Priority Value TimeStamp Comment)")  
        except sqlite3.OperationalError:    
            print("OperationalError")
        except sqlite3.DatabaseError:
            print("DatabaseError: file is encrypted or is not a database")
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

    def store_row(self):
        """
        """

    def erase_row(self):
        """
        """

    def read(self):
        """given a set of attr. and ID's return such attr. of ID's
        """

    def search(self):
        """
        """
     
  

    def __del__(self):
        self.conn.commit()
        self.conn.close()
