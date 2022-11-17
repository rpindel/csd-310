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
##cursor = db.cursor()
##cursor.execute(“SELECT * FROM studio")
##studios = cursor.fetchall()
##for studio in studios:
##print("-- DISPLAYING Studio RECORDS --")
print(“First Name: {}\n Last Name:{}\n Email:{}\n”.format(employee[0], employee[1], employee[2]))

##query 2    
##cursor = db.cursor()
##cursor.execute(“SELECT * FROM genre”)
##genres = cursor.fetchall()
##for genre in genres:
##print("-- DISPLAYING Genre RECORDS --")
print(“First Name: {}\n Last Name:{}\n Email:{}\n”.format(employee[0], employee[1], employee[2]))

##query 3    
##cursor = db.cursor()
##cursor.execute(“SELECT film_name, run_time FROM film WHERE run_time < '2'")
##shortFilms = cursor.fetchall()
##for shortFilm in shortFilms:
##print("-- DISPLAYING Short Film RECORDS --")
print(“First Name: {}\n Last Name:{}\n Email:{}\n”.format(employee[0], employee[1], employee[2]))

##query 4    
##cursor = db.cursor()
##cursor.execute(“SELECT film_name, director_name,FROM film GROUP BY director_name”)
##directors = cursor.fetchall()
##for director in directors:
####print("-- DISPLAYING Director RECORDS in Order --")
##print("Film Name: {}\n Director Name: {}\n".format(director[0], director [0[]]))

db.close()
    
    
