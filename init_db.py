import sqlite3

# create a connection to the database
connection = sqlite3.connect('database/IA2_Database.db')

with open('schema/schema.sql') as f:
    connection.executescript(f.read())

# create a cursor object that is required to process rows in a database
# the cursor object is necessary to read through the database
cur = connection.cursor()

# Use the cursors execute method to run SQL statements
