import sqlite3
from flask import g

class db_access(object):
    """description of class"""
    def __init__ ():
        DATABASE = '\FlaskWebProject\Database\Database.py'
        connection = sqlite3.connect("database.db") #creating a new database
        self.c = connection.cursor() # saving the database in the location where the 'py' file is saved

    def get_villages(self):
        return self.c.execute(''' SELECT generated_id, village_name FROM Villages ''')

    def get_restaurants(self):
        return self.c.execute(''' SELECT restaurant_id, village_id, name, short_description, details FROM Restaurants_Bars ''')

    def get_restaurants_in_villages(self, villageId):
        pass

