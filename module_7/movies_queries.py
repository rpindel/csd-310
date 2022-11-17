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
print("\n-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

##query 2    
cursor = db.cursor()
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("\n-- DISPLAYING Genre RECORDS --")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

##query 3    
cursor = db.cursor()
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < '120'")
shortFilms = cursor.fetchall()
print("\n-- DISPLAYING Short Film RECORDS --")
for shortFilm in shortFilms:
    print("Film Name: {}\nRuntime: {}\n".format(shortFilm[0], shortFilm[1]))

##query 4    
cursor = db.cursor()
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
directors = cursor.fetchall()
print("\n-- DISPLAYING Director RECORDS in Order --")
for director in directors:
    print("Film Name: {}\nDirector: {}\n".format(director[0], director [1]))

db.close()
    
    
