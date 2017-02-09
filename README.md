# clog
A Python 3 module for logging to text file or sqlite3 database.

To initialize LogMessageFile: 
message = clog.LogMessageFile('log.txt')

Or initialize LogMessageDB: 
message = clog.LogMessageDB('log.db')

To read the log: 
message.read()

To write to the log: 
message.write('whatever you want to log.')
