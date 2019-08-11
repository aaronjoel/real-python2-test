# The aim of this exercise is to create a database named cars.db
# with the table called inventory which includes the following 
# fields Make, Model, Quantity 

# Import the sqlite3 library
import sqlite3

# create the database cars.db or connect to its if it exists.
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory (make TEXT, model TEXT, quantity INT)""")

# close the database connection
conn.close()

