#lists part 2
# + works with integers and strings but also works with lists.
# It concatenates (=aaneenschakelen) them together
# for example:
a = [1, 2, 3]
b = ['poop', 5, 6.97867]
c = a + b
print(c)

#You can SLICE lists just like you can with strings
print(c[2:4])
#remember this prints UPTO slot 4, not upto and including, so it only prints slot 2 and 3, being '3' and 'poop'
#you can also leave parts out:
print(c[3:])
print(c[:4])
#you can make an empty list by using the 'constructor' list():
stuff = list()
# and then add things to it by appending:
stuff.append('book')
stuff.append('99')
print(stuff)
#checking if something is in a list, you can use the 'in' operator which returns a true of false
if 'book' in stuff:
    print("yes")
else:
    print("no")

if 'poop' in stuff:
    print("poop's there")
else:
    print("no poop")

#same goes for 'not in'

if 'poop' not in stuff:
    print("poop's really not in the list")
else:
    print("Oh no wait it is there")

#you can sort lists with the sort() method (basic function is sorting alphabetically, or from low to high)
letters = ['C', 'B', 'A']
numbers = [3, 6, 2 ,1]
print(letters)
print(numbers)
letters.sort()
numbers.sort()
print(letters)
print(numbers)
