# We don't need to call the commit() method when the with statement is used 
# because the changes are automatically saved.

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New Jersey', 'NJ', 9100000)")
    c.execute("INSERT INTO population VALUES('San Diego', 'SD', 1200000)")
