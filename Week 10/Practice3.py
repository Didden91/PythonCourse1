#Tuples are COMPARABLE
#It goes through the items systematically, left to right
#So it compare item 0 with item 0, then item 1 with 1, etc
#This means that if it finds an answer to your question it returns the answer and stops looking further

#So if you say
if (0, 1, 2) < (5, 1, 2):
    print('true')
#it prints true
#if you say
if (0, 1, 2000000) < (0, 3, 4):
    print('true')
#It also prints true: slot 0 compared to slot 0 does not answer the question:
# 'they're both zero so I don't know, moving on to slot 1 and slot 1'
#So it does not even reach the 2 million to compare it to 4
#you can also compare strings (with greater or smaller than it looks at aplhabetical order):
if ('Jones', 'Sally') < ('Jones', 'Sam'):
    print('true')
# This prints true once again as Sally is lower than Sam


#A great use of tuples is their ability to SORT a dictionary
#You can use the items() method to convert a dictionary to a list of tuples,
# convert that list, and then you have a sorted list of dictionary items
#The sorted() function does this for you.
d = {'a':10, 'b': 1, 'c':22}
print(d.items())
print(sorted(d.items()))

#using sorted() and tuples:
# We can produce a sorted list by doing:
tup = sorted(d.items())
print(tup)
#and we can use a for loop:
for k, v in sorted(d.items()):
    print(k, v)
#This is of course all sorted by KEY, not value
