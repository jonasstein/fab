#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sqlite3

"""Testimplematantion of the FAB Project. Come get some!!"""

def loadDatabase(path = '/', name = 'testdata.dat'):
    """
    Returns a database with Structure. Begins with the ID and TIMESTAMP.

    """
    print("Loading database from file...")
    nameWithPath = path + "/" + name
    inFile = open('testdata.dat', 'r')
    linesInFile = inFile.read().splitlines()
    base = []
    for lines in linesInFile:
        if lines[0]!="#":
            base.append(lines.split())
            
    return base


def makeDatabaseString():
    """
    Returns a Database command. Input is a basestructure. 
    """

class data():
    """Class to create a dataelement of a Basestructure:
        1. IdPerson: A unique Number for a person to store ##TODO
        2. time : a timestamp of the stored data. We want to restore the history of a stored person ##TODO
        3. storeName: a Name for the stored data. Futher code will implement special operations for keywords.##TODO
        4. storeValue: a Value you want to store ##TODO"""

    
    def __init__(self, idperson, timeStore):
        if idperson!= None:
            self.idperson = maxIdPerson() + 1
        self.timeStore = time()
        self.storeName = []
        self.storeValue = []
        

    def getIdperson(self):
        """Not like a idcard, hopefully unique for all stored persons"""
        
        return self.idperson()

    def getTimeStore(self):
        """Need time? here you get."""
        
        return self.time()

    def getStoreName(self, storePos):
        """Gives back the Name of the stroed data, on spezified positio, not fully implementet yet and discussed ;)"""
        try:
            return self.store()[storePos]
        except:
            raise NoPositionFound
        
    def getStoreValue(self, storePos):
        """Gives back the value of the stroed data, on spezified positio, not fully implementet yet and discussed ;)"""
        
        
        try:
            return self.storeValue()[storePos]
        except:
            raise NoPositionFound
    
    def storeInBase(self):
        """Test store implemaentation
            Database structure:
            #IdPerson #time #storeName #storeValue"""
        
        inBase = database.cursor()
        inBase.execute('''create table base (idperson text, time text, Name text, Value text)''')

        inBase.execute('insert into base values(?, ?, ?, ?)' , (self.getIdperson(), self.getTimeStore(), self.getStoreName(0), self.getStoreValue(0)) )
        database.commit()
        inBase.close()
    
    def maxIdPerson():

        """Search in Database for next Idperson number. not fully implementet yet"""
        return max(range(1,100))

print(loadDatabase())


database = sqlite3.connect('/Users/arturbielefeld/Documents/projekte/fab/datab')

inBase = database.cursor()

inBase.execute("""create table base1 (date text, trans text, symbol text, qty real, price real)""")

inBase.execute("""insert into base1 values ('2006-01-05','BUY','RHAT',100,35.14)""")
database.commit()

inBase.close()
