#looking more at the complexity of text processing
#Most of what we've been doing so far is all in ASCII
# ASCII is a 128 item list of how characters are represented and stored
# This is also why capital letters are sorted before lower case latter when using sort() for example
# You can find the Ordinal, or numeric representation of a number in Python by using the ord() function

print(ord('H'))
print(ord('e'))
print(ord('\n'))

# ASCII is only aplicapble to some western nations, for more international standards, we use a MUCH more complex character set:
# UNICODE
# The problem is, if we sent UNICODE accross the network, it would be way too large,
# that's the downside of such a extremely versatile character set
# that would be UTF-32
# What they've come up with is ways to compress this, namely UTF-8
# UTF-8 is the BEST PRACTICE in moving data across the internet
# UTF-8 can represent everything UTF-32 can represent, it is just a compression of it.

#in Python 2, unicode and string were seperate
#in Python 3: UNICODE and string is THE SAME
# A string inside Python 3 is IN UNICODE
# In python 3 this leads to a class called BYTES
# Whereas in Python 2 BYTES and STRINGS were the same and UNICODE was weird
# in Python 3 STRINGS AND UNICODE are the same and BYTES is the weird one
# so in accessing the web, we might sometimes get bytes returned to us, which we have to deal with
# example:
x = b'abc'
print(type(x))      #this is a BYTES class (presumably because it is preceded by a 'b'(?))
y = '한국어 키보드'
print(type(y))      #This would be UNICODE in old python, in python 3 this is just a string.

#At times API's might return BYTES to us, and we need to figure out what those bytes contain
# because those bytes might contain ASCII, might contain UTF-8, might contain various things
# GOOD NEWS IS, in 98% of the cases it will be UTF-8

# When we read from an external resourse, we must DECODE it based on the character set so it is properly represented in Python 3
# That's what we use the decode() method for!
# Same with ENCODING before sending it: using the encode() method
# What that does is take the UNICODE string we made in Python 3 and converts it to UTF-8 to send over the netword
# The same happens in reverse with decode, we receive UTF-8 and turn in back into UNICODE
# In other words, you take a string and ENCODE it to a BYTE ARRAY
# You receive a BYTE ARRAY and DECODE it into a string
