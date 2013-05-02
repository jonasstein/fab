#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import unittest
from addressbook import *

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

class AddressBookTest(unittest.TestCase):

    def test_add_contact(self):
        pass

if __name__ == "__main__":
    unittest.main()
