#Using REGEX to not only match data but also extract it!
#Example: don't just print out all the lines that match, but return me a list of all the ones that match
#We can use re.findall() for this
#Whereas re.search() returns a True/False, re.findall() returns a LIST of strings that match

import re
x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print (y)

#This prints: ['2', '19', '42']

#things in brackets like [0-9] mean ALLOWED characters, in this context it means A SINGLE DIGIT
# and + means 'one or more'
# So [0-9]+ means ONE OR MORE DIGITS
# You can do the same with say, [AEIOU]+ which would mean ANY UPPER CASE VOWEL, ONE OR MORE
y = re.findall('[AEIOU]+', x)
print (y)

#This prints an empty list because nothing matched.
