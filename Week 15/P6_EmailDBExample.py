# Let's write a program that creates a database file and populates it with information from a textfile which is prompted for

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')    #makes the 'connection' to this database called conn
cur = conn.cursor()                         #creates a 'filehandler' for the conn we just made, called cur

cur.execute('DROP TABLE IF EXISTS Counts') #if the table 'Counts' already exists, drop (aka delete) it

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''') #create a table called Counts, containing 2 column (or attributes)
#one called email, containg text entries, and one called count, containing integer entries

#note: the triple quotation marks make it so that these two lines are run as one line. It's been split into two lines for legiability
fname = input('Enter file name: ')                         #prompt for file name
if (len(fname) < 1): fname = 'mbox-short.txt'               #If no entry, default to mbox-short.txt
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]                              #This is the algorithm we used before to find the email address following 'From:'

    #Let's break this next part down, it's bascially like our earlier dictionary histogram thing.
    #First off, cur is the 'filehandler' and .execute() means execute the following SQL code.

    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))

    #So this executes the following: Select the column called count in the table called Counts
    #Select the item in the column count, that is connected to the following email: [enter email variable]
    #So what happens here is the questionmark is a PLACEHOLDER, and that placeholder is filled in by the , (email,)) that follows it,
    #That last part enters the email variable we created above, the one we made with pieces[1], and places it in there
    #The kind of weird syntax is because (email,) is actually a tuple, these questionmark placeholders are filled in by tuples.
    #In this case it's only one varibale so it is a tuple containing only one entry
    #This is because it is dangerous to directly enter strings, or allow people to enter strings into the database, as it could crash, or enable SQL Injection (this is BAD), this way is generally safer.

    #So that whole thing does not actually DO anything to the data, it just OPENS a 'file', it opens a set of records you request and keeps it ready for you.
    #For now we're only going to grab the FIRST item we find, using the following code
    #This says, in our cursor called cur, call method fetchone which retrieves the next row of a query result set and returns a single sequence. Place that result in 'row'
    row = cur.fetchone()

    #If there is nothing in row, INSERT into the table counts, in to the tuple of columns (email and count), the values of
    # (PLACEHOLDER and 1), followed by the data that goes into the placeholder
    #This is like the Get() function we used a while back with the histogram.
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))

    #If the row is NOT NONE: UPDATE in the table Counts, where the email is [PLACEHOLDER], take the value in count and make it the value in count plus 1, followed by the data that goes into the placeholder
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    #This conn (our 'connection') commit line forces the data to be written to the database file
    #before we do this, our instructions are only kept in memory but no changes are actually made to the database.
    #So at the end of this for loop, we commit every time. This is useful because the commit is the 'heaviest' process, so best not to wait too long to call it.
    conn.commit()

# now in a string called sqlstr we'll place an SQL command. This command selects the columns email and count from the Counts table and sorts these two columns by count, in descending order, and limits it to the first ten entries
# So essentially with this we can generate a top 10
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

#Then for every iteration of this command being executed, print the first row and the second row.
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

#and finally close the cursor (just like we would the filehandler)
cur.close()
