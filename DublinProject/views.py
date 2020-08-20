"""
Routes and views for the flask application.
"""

from flask import Flask
from flask import render_template, redirect, url_for, request, session
from datetime import datetime
from DublinProject import app
import sqlite3



# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # When posting info to the server
    if request.method == 'POST':
        if request.form['username'] == 'Wedding' and request.form['password'] == '2019':
            session['logged_in'] = True
            return redirect ('/')
        else:
            return render_template('login.html', Error = 'Wrong username or password. Please try again.')
    # When getting info from server
    return redirect('/login')



# Home page
@app.route('/')
def home():
    # If not logged in then return login page, else return home page
    if not authorized():
        """Renders (í. teikna) the home page."""
        return render_template('login.html')
    return render_template('home.html')



#Things to do in Dublin page
@app.route('/things_to_do')
def things():
    if not authorized():
        return render_template('login.html')
    else:
       con = sqlite3.connect("database.db")
       con.row_factory = sqlite3.Row
   
       cur = con.cursor()
       cur.execute('''SELECT T.generated_id,
                             T.place_name,
                             I.description,
                             I.website,
                             L.long,
                             L.lat
                      FROM ThingsToDo T
                      JOIN Info I ON I.info_id=T.generated_id
                      JOIN Location L ON L.location_id = T.generated_id''')

       rows = cur.fetchall(); 
       return render_template("things.html",rows = rows)



#Restaurants, bars and cafés in Dublin page
@app.route('/restaurants')
def restaurants():
    if not authorized():
        return render_template('login.html')
    else:
       con = sqlite3.connect('database.db')
       con.row_factory = sqlite3.Row
   
       cur = con.cursor()
       cur.execute('''SELECT V.village_name,
                             R.name,
                             R.emoji,
                             R.short_description,
                             R.details,
                             R.website
                      FROM Villages V 
                      JOIN Restaurants_Bars R ON V.generated_id=R.village_id''')
 
       rows = cur.fetchall()
       dict = {}
       for row in rows:
           key = row['village_name']
           if key in dict:
               dict[key].append(row)
           else:
                dict[key] = [row]

       return render_template("restaurants.html",rows = dict)



#Kinnitty Castle page
@app.route('/KinnittyCastleHotel')
def kinnitty():
    if not authorized():
        return render_template('login.html')
    return render_template('kinnitty.html')



# Log in
def authorized():
    if not session.get('logged_in'):
        return False
    return True



