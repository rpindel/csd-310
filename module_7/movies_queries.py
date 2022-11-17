import mysql.connector
from mysql.connector import errorcode

config = {
    "user" : "root",
    "password" : "mysqltest",
    "host" : "127.0.0.1",
    "database" : "movies",
    "raise_on_warnings" : True
    }
    
db = mysql.connector.connect(**config)

##query 1    
cursor = db.cursor()
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
for studio in studios:
print("-- DISPLAYING Studio RECORDS --")
print("Studio ID: {}\n Studio Name: {}\n".format(studio[0], studio[1]))

##query 2    
cursor = db.cursor()
cursor.execute("SELECT * FROM genre”)
genres = cursor.fetchall()
for genre in genres:
print("-- DISPLAYING Genre RECORDS --")
print("Genre ID: {}\n Genre Name: {}\n".format(genre[0], genre[1]))

##query 3    
cursor = db.cursor()
cursor.execute("SELECT film_name, runtime FROM film WHERE run_time < '120'")
shortFilms = cursor.fetchall()
for shortFilm in shortFilms:
print("-- DISPLAYING Short Film RECORDS --")
print("Film Name: {}\n Runtime: {}\n".format(shortFilm[0], shortFilm[1]))

##query 4    
cursor = db.cursor()
cursor.execute("SELECT film_name, director_name,FROM film GROUP BY director_name”)
directors = cursor.fetchall()
for director in directors:
print("-- DISPLAYING Director RECORDS in Order --")
print("Film Name: {}\n Director Name: {}\n".format(director[0], director [0]))

db.close()
    
    
