import sqlite3

# create a connection to the database
connection = sqlite3.connect('database/IA2_Database.db')

with open('schema/schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
