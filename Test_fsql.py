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

    def test_insert(self):
        """Testing row insertion."""
        pass

    def test_remove(self):
        """Testing row removal."""
        pass

    def tearDown(self):
        """Cleanup after tests."""
        os.unlink(TESTDATABASE)
        pass

if __name__ == "__main__":
    unittest.main()
