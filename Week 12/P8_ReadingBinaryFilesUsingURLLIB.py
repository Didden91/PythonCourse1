# Sometimes you want to retrieve a non-text (or binary) file such as an image or video file.
# The data in these files is generally not useful to print out, but you can easily make a copy of a URL to
# a local file on your hard disk using urllib.

# The pattern is to open the URL and use READ to download the entire contents of the document into
# a string variable (img) then write that information to a local file as follows:

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')        # open cover3.jpg, the wb makes open() open a Binary file for Write only
fhand.write(img)
fhand.close()

#potential problem with this file is we read everything at once (we don't give the read() method a parameter or limit)
#So if the file we're receiving is larger than the computer's memory, the program will run out of memory and crash.
#A way around this is to retrieve the data in 'blocks' or 'buffers'
# example:

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()
