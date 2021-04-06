# Using re.search() like we did with find()
#find() went like this

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:             #btw: greater than or equal to zero is because find() returns -1 if something is not found
        print(line)

# re.search() goes like this:
print('EN NU MET REGEX!')

import re

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

#With REGEX you can FINE TUNE, which makes it really nice
# You can do the same thing:


fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if re.search('^From:', line):       # ONE ^ CHARACTER ADDED
        print(line)

#and now it asks, IF LINE STARTS WITH 'From:' instead of if it contains 'From:'
#Because (you can check the quick guide) the ^ character refers to 'line begins with'
