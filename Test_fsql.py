#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""Description: fsql Test module
"""

import unittest
from fsql import *
import os

TESTDATABASE = "test.db"

class FabDatabaseTest(unittest.TestCase):
    """Unittesting database management."""

    def setUp(self):
        self.db = FabDatabase(TESTDATABASE)
        self.dic={"ID":1,"ContactID":2,"Type":'Name',"Valid":1,"Timestamp":'10-10-2013T010101',"Comment":'blub'}
        self.tupel=(1,2,u'Name',1,u'10-10-2013T010101',u'blub')

   # def test_insert(self):
   #     """Testing row insertion."""
    #    pass

#    def test_remove(self):
#        """Testing row removal."""
#        pass

    def test_store_row(self):
        self.db.store_row(self.dic)
        self.assertEqual(self.db._conn.execute("SELECT * FROM data WHERE ID=1").next(),self.tupel)

    def test_get_row(self):
        self.db.store_row(self.dic)
        self.assertEqual(self.db.get_row(1),self.dic)    

    def test_erase_row(self):
        self.db.erase_row(1)
        self.assertRaises(StopIteration,self.db._conn.execute("SELECT * FROM data WHERE ID=1").next)


    def tearDown(self):
        """Cleanup after tests."""
        os.unlink(TESTDATABASE)
    

if __name__ == "__main__":
    unittest.main()
