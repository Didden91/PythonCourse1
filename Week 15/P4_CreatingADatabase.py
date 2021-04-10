# Creating a database table
# Databases require more defined structure than Python lists or dictionaries.
#
# When we create a database table we must tell the database in advance the names of each of the columns in the table
# and the type of data which we are planning to store in each column.
# When the database software knows the type of data in each column,
#  it can choose the most efficient way to store and look up the data based on the type of data.
#
# The code to create a database file and a table named Tracks with two columns in the database is as follows:

import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()

# The connect operation makes a “connection” to the database stored in the file music.sqlite in the current directory. If the file does not exist, it will be created. The reason this is called a “connection” is that sometimes the database is stored on a separate “database server” from the server on which we are running our application. In our simple examples the database will just be a local file in the same directory as the Python code we are running.

# A cursor is like a file handle that we can use to perform operations on the data stored in the database. Calling cursor() is very similar conceptually to calling open() when dealing with text files.
