import sqlite3 as sql

class dbAccess(object):
    """description of class"""
    def __init__(self):
        self.databaseName = 'mydb.db'
        if not dbExists:
            self.createDB()

    def createDBlocation(self):
        connection = sql.connect(self.databaseName)
        connection.cursor()
        #Create tables
        connection.execute('CREATE TABLE Location(id int, name text, lng float, lat float)')
        # Insert a row of data
        connection.execute("INSERT INTO Location VALUES (1,'Baggot Street', 53.333206, -6.243367)")
        # Save changes
        connection.commit()
        connection.close()

        
        #self.connection.execute('CREATE TABLE Class(id int, name text)')
        #self.connection.execute('CREATE TABLE Restaurants(id int, name text, class int, description text)')


    def FetchTable(self, tableName):
        #get table with tableName
        pass
