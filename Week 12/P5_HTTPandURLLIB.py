#Now let's write a webbrowser again, but EVEN SHORTER, only 4! lines instead of 10
#opening a connection, sending a GET request, sending two newlines, receiving the data, removing the headers,
# doing ALL this stuff is so common, why not make a library for it!
# That's exactly what URLLIB does!
#Instead of sockets we now import urllib!

#The below program does the same as the earlier 10 line socket program

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#What this does: open urllib library, call the request module in the library, and in that module call the urlopen function
#Within that function open the following url: http://data.pr4e.org/romeo.txt
#urllib returns to you an OBJECT that looks pretty similar to a Filehandle!
# Place that object in a handler called fhand

# for line in fhand:                      # Pretty much the same as how you read a file, fo through it line by line
#     print(line.decode().strip())        # The data return is in the BYTES format however, so we first have to DECODE it again
#                                         # Then strip, and print

#Part of what urlopen() does is REMOVE the headers, but it does STORE them.
#There are ways to get the headers should you need them

#After you do the DECODE bit, you can treat it like any old file, for example, let's count the words again!
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
