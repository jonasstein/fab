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
    


print(loadDatabase())


database = sqlite3.connect('/Users/arturbielefeld/Documents/projekte/fab/datab')

inBase = database.cursor()

inBase.execute(date text, trans text, symbol text,
 qty real, price real)

inBase.execute('2006-01-05','BUY','RHAT',100,35.14)

inBase.close()
