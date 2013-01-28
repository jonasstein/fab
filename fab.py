#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sqlite3
import time
"""Testimplematantion of the FAB Project. Come get some!!"""

class Menu(object):
    """main routine, to use on commandline, later we will to implement a command line syntax for scripts"""

    def documentation(self):
        menutrig = True
        while menutrig:
            print("\n")
            print("You have some choices:")
            print("Explain me, why I should use FAB?: 1")
            print("Load a Files with Contacs: 2")
            print("How i change entries?: 3")
            print("back: b,e,q")
            choose = raw_input("Make your desision:")
        
            if choose.lower() in ["e", "q" , "end", "quit", "b"]:
                menutrig = False
                menuobj.menuentries()
            if choose == "1":
                print("\n")
                print("We need to talk, what is FAB? \n We have the idee to write a Adressbook which don't forget the last entries.\n")
                print("People changing from time to time some details, new phone, address etc. And now?")
                print("FAB helps to conservate this details in time relation.\n")
                  
       
            if choose == "2":
                print("\n")
                print("Supported filetyps: only our Filetyp")
            if choose == "3":
                print("\n")
                print("Changing is not the right answer.\n We store all data in our Database with a timestamp.")
                print("Nothing will be deleted.\n If you want to delete from the database, do it in a texteditor.")
                print("FAB databases based on SQLite which stores all entries in a file on your disk.")


    def menuentries(self):
        menutrig = True
        while menutrig:
            print("Welcome to Flexible Address Book. Now you have some choices:")
            print("Search for a Person: 1")
            print("Load a File with Contacs: 2")
            print("Help me, what is diffrent here?: h,?,help")
            print("Exit: e,q")
            choose = raw_input("Make your desision:")
        
            if choose.lower() in ["e", "q" , "end", "quit"]:
                print("Goodbye")
                menutrig = False
                raise SystemExit
            if choose == "1":
                searchPerson()
            if choose == "2":
                importDataobj.menuentriesimport()
            if choose in ["h","help" , "?", "hell", "sunny", "wtf"]:
                menuobj.documentation()


        
           

class ImportData(Menu):

##    def __init__(self):
##        """Prompt to import contacts, expectet are: 1. Database, 2. vcard, 3. some stuff not yet decided"""
##        self.path = None
##        self.filename = None
##        
    
    def loadDatabase(self, pathandfile):
        """path = '/', name = 'testdata.dat'"""
        """
        Returns a database with Structure. Begins with the ID and TIMESTAMP.

        """
        print("Loading database from file...")
        #nameWithPath = path + "/" + name
        inFile = open('testdata.dat', 'r')
        linesInFile = inFile.read().splitlines()
        base = []
        for lines in linesInFile:
            if lines[0]!="#":
                base.append(lines.split())
                    
        return base
    
    def menuentriesimport(self):
            
        menutrig = True
        while menutrig:
            choose = raw_input("Choose your Task:\n Read Database: 1 \n Read vCard: 2 \n back: b \n ::>")
            if choose == "1":
                pathandfile = raw_input("Enter Path and Filename:")
                base = importDataobj.loadDatabase(pathandfile)
                i = 0
                for baseline in base:
                    print(baseline)
                    baseobj.storeDataToBase(baseline)
                    print(i)
                    i+=1                    
                menutrig = False
            elif choose == "2":
                print("TODO")
                menutrig = False
            else:
                if choose.lower == "b":
                    menutrig = False
        menuobj.menuentries() 
                
        
    

class Data(Menu):
    """Class to create a dataelement of a Basestructure:
        1. IdPerson: A unique Number for a person to store ##TODO
        2. time : a timestamp of the stored data. We want to restore the history of a stored person ##TODO
        3. storeName: a Name for the stored data. Futher code will implement special operations for keywords.##TODO
        4. storeValue: a Value you want to store ##TODO"""

    
    def __init__(self, idperson, timestore = int(time.time()), storename = None, storevalue = None):
        if idperson!= None:
            self.idperson = maxIdPerson() + 1
        else:
            self.idperson = None
        self.timeStore = timestore
        self.storeName = storename
        self.storeValue = storevalue
        

    def getIdPerson(self):
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

        inBase.execute('insert into base values(?, ?, ?, ?)' , (self.getIdPerson(), self.getTimeStore(), self.getStoreName(0), self.getStoreValue(0)) )
        database.commit()
        inBase.close()
    
    def maxIdPerson():

        """Search in Database for next Idperson number. not fully implementet yet"""
        return max(range(1,100))

class Base(Data):
    """Our Databse Object, an ordinary list..."""
    def __init__(self):
        self.datab = [["1"],]

    def getDatabase(self):
        return self.datab
    
    def storeDataToBase(self, datastore):
        datasafe = baseobj.getDatabase()[:]
        print(datasafe)
        
        print(datasafe.append(datastore))    ###TODO WHY is not appending?
        print(self.datab)
        

class person(Menu):

    def __init__(self, idperson, timeStore, firstname = None, lastname = None, nickname = None):
        data.__init__(self, idperson, timeStore)
        firstName = firstname
        lastName = lastname
        nickname = nickname

menuobj = Menu()
importDataobj = ImportData()
dataobj = Data(None)
baseobj = Base()
menuobj.menuentries()
      
###print(loadDatabase())
##
##
##database = sqlite3.connect('/Users/arturbielefeld/Documents/projekte/fab/datab')
##
##inBase = database.cursor()
##try:
##    inBase.execute("""create table base1 (date text, trans text, symbol text, qty real, price real)""")
##except:
##    None
##inBase.execute("""insert into base1 values ('2006-01-05','BUY','RHAT',100,35.14)""")
##database.commit()
##
##inBase.close()
