#How we FIRST tore apart strings:
# Say we want to find only the address in the string

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')          #Find the first @ in the string
print(atpos)

sppos = data.find(' ',atpos)    #Find the first space after the @ slot
print (sppos)

address = data [atpos+1 : sppos]    #Address is one slot after @ position up to but not including the space position
print(address)

#The SECOND way we learned to do this was with the DOUBLE SPLIT PATTERN

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = data.split()                                                # split whole line into seperate words loaded into list called words
email = words[1]                                                    # take item in slot 1 of list and place in variable email
pieces = email.split('@')                                           # take variable email and split contents by the '@' character, place split items in list called pieces
print(pieces[1])                                                    # print what's in slot 1 of list pieces

#AND NOW... the REGEX way of doing it!

import re

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', data)
print(y)

#Beautiful! This returns ['uct.ac.za'] because findall() places found items in a LIST
#Let's break this down!
# What '@([^ ]*)' does is this:
# Look through the string until you find an @ sign (@)  <-- This is the MATCHING or searching section
# Then comes the EXTRACTION part, because you open parentheses (()
# now Match Non-Blank characters [^ ]       In this case ^ means NOT followed by a space, so it equals NOT space/BLANK, the square brackets indicate ALLOWED characters within
# Match zero or more times (*)
# End when it reaches a blank character (a space in this case)
