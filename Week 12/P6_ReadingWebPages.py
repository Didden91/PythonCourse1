#What we just did was open a TEXT file on a webpage, but we can just as well read the webpage itself
#Let's try it with a HTML page


import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())

#This simply prints what's on the webpage, with all the html formatting still in there, so in this case:

# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://www.dr-chuck.com/page2.htm">
# Second Page</a>.
# </p>

#now to PARSE this HTML to make it a lot easier to process
