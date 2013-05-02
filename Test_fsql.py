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

   # def test_insert(self):
   #     """Testing row insertion."""
    #    pass

#    def test_remove(self):
#        """Testing row removal."""
#        pass

    def tearDown(self):
        """Cleanup after tests."""
        os.unlink(TESTDATABASE)
    
    def test_store_row(self):
        self.assertEqual(self.db.store_row(self.dic),None)

    def test_get_row(self):
        dic2 = self.db.get_row(1)
        self.assertEqual(dic2, self.dic)

if __name__ == "__main__":
    unittest.main()
