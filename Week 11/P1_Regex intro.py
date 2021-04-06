# REGULAR EXPRESSIONS (REGEX)
# More of an optional topic! If you like them you can use them, if you don't you can get on just fine without ever using them!
#A regular expression is a sequence of characters that define a search pattern

#You can make really clever "wild card" expressions for matching and parsing strings
#They can be quite TRICKY though, not easy to pick up
# Requires quite a lot of trial and error at first (try and check and try and check etc.)

#Regex is a little programming language in itself, difference with other languages is is that it's not LINE based, but CHARACTER based
#SEE THE QUICK GUIDE ON DESKTOP!

#Regex is NOT in base python but is distibuted with Python, you have to import it using

import re

#You can then use things like
re.search()
#To see if a string matches a inputted regular expression, similar to using the find() method for string
#You can use
re.findall()
#to extract portions of a string that match your regular expression
#So what I used to with find() and then slicing using
string[2:5]
#can be done using regex instead
