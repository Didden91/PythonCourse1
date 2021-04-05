#TUPLES AND ASSIGNMENT
#You can put a tuple on the LEFT side of an assignment as well, neat!
#example:
(x, y) = (123, 'poop')
print(y)
#You can even leave out the paranthesis
r, t = 2, 4
print(r)
print(t + 1)


#Tuples and dictionaries:
#As we've touched upon briefly  before, you can use tuples on dictionaries
#the items() method used on a dictionary returns a list of (key, value) tuples
#so for example:
d = dict()
d['eenitem'] = 6
d['eenanderitem'] = 100
#Then we can use a tuple in a for loop to extract the pairs
for (k, v) in d.items():
    print(k, v)
#you can also place those items in a variable which becomes a dict_items list (somthing covered later probably)
#But essentially a list of tuple values, like so:
tups = d.items()
print(tups)
