#DICTIONARIES
#DICTIONARIES are a form of collections, just like last weeks lists
#Difference: List is a linear collection of values that stay in order
#Dictionary is a "bag" of values, each with its own LABEL (also called KEY)
#wiki: associative array
#different languages use different names for the same thing

#to create a dictionary use dict()
purse = dict()
#then use the dictionary to add a 'key' which holds the value, so 'money' (KEY) = 12 (VALUE)
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

#you can add to values of keys like so:
purse['money'] = purse['money'] + 3
#or change it like so
purse['candy'] = 45
print(purse)

#Dictionary literals (literals=data given in a variable or constant) use curly braces and have a list of KEY : VALUE pairs
#You can make empty dictionaries using empty curly braces (as seen above you can also make an empty dictionary using dict())
#dict() is a constructor with which you say 'make a new dictionary', the { } is an empty dictionary constant you can call.
#They do pretty much THE SAME THING, { } is something of a shortcut for dict()
jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)
jje = {}
print(jje)
