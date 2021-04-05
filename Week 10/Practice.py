# TUPLES
#THIRD kind of collection after lists and dictionaries.
#Kind of a reductionist version of lists
#Tuple uses ROUND paranthesis
#Made like so:
t = (1, 9, 2)
#Some functions that work with lists also work with tuples, like max
print(max(t))
#You can put a tuple at the end of a for statement just the same
for iter in t:
    print(iter)
#Big DIFFERENCE between tuples and lists, is that tuples are IMMUTABLE, cannot be changed
#The reason it is not modifiable is for efficiency, they take up less storage, are quicker to access than lists etc.
#If all you want to do is store a list, look at it, then throw it away, you should probably use a tuple instead.
#Things NOT to do with tuples: list methods such as .sort() .append() .reverse() .. all because, again, tuples are immutable
#The dir() function is useful for reference, it returns what methods and attributes an object has
#So you can check what you can do with a list and what you can do with a tuple by:
l = list()
print(dir(l))

t = tuple()
print(dir(t))
#IGNORE the __functions__ for now

#Again, tuples are useful as temporary variables, whereas lists are used to build things up over longer periods
