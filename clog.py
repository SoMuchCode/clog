#
# clog.py module
#
# Containing: LogMessageFile and LogMessageDB classes
#  For writing (appending) to a log file or sqlite3 database
#  version 0.1
#
# Python 3.6
# CLM 20170209
# https://github.com/SoMuchCode
#
# To initialize LogMessageFile
# message = clog.LogMessageFile('log.txt')
#
# Or initialize LogMessageDB
# message = clog.LogMessageDB('log.db')
#
# To read the log
# message.read()
#
# To write to the log
# message.write('whatever you want to log.')
#
try:
    import sqlite3
except Exception as errorCaught:
    print('Error: Cannot load module, sqlite3')
    print('Error:', errorCaught)

class LogMessageFile:
    def __init__(self, fileName):
        self.fn = fileName
    def read(self):
        self.file = open(self.fn,'r')
        for linE in self.file:
            print(linE, end = '')
        self.file.close()
    def write(self, texT):
        try:
            self.appendMe = texT
            self.file = open(self.fn,'a')
            self.file.write('\n')
            self.file.write(self.appendMe)
            self.file.close()
        except IOError as errorCaught:
            try:
                self.appendMe = texT
                self.file = open(self.fn,'w')
                self.file.write(self.appendMe)
                self.file.close()
            except Exception as errorCaught:
                print('Error: ' , errorCaught)
        except Exception as errorCaught:
            print('Error: ' , errorCaught)

class LogMessageDB:
    def __init__(self, dbName):
        self.dbn = dbName
        try:
            self.db = sqlite3.connect(self.dbn)
            self.db.execute('create table if not exists clog (message)')
            self.db.commit() #this saves it
            self.db.close()
        except:
            print('Error: Problem connecting to database', self.dbn)
    def read(self):
        self.db = sqlite3.connect(self.dbn)
        self.table = self.db.execute('select * from clog')
        for self.each in self.table:
            print(self.each)
        self.db.close()
    def write(self, texT):
        try:
            self.db = sqlite3.connect(self.dbn)
            self.appendMe = texT
            self.db.execute("insert into clog values (?)", (self.appendMe,))
            self.db.commit()
            self.db.close()
        except lite.Error as errorCaught:
            print('Error:', errorCaught)
            if self.db:
                self.db.rollback()
                self.db.close()
        except Exception as errorCaught:
            print('Error:', errorCaught)
            if self.db:
                self.db.rollback()
                self.db.close()
