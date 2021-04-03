#Square brackets make a LIST
for iter in [5, 4, 3, 2, 1]:
    print(iter)
print("Blastoff")

testlist = ['Ivo', 'Didden', 'Dorieke','Berends']
for i in testlist:
    print("name:",i)
print("All done with this part")

#Strings are UNmutable, cannot be changed
#Lists are mutable, can be changed
#x = 'eenstring'
#x[2] = 'b' -> does NOT work
#below here does work:
testlist[2] = 'Henkie'

print(testlist)



#In lists a function like 'len' counts the number of entries
print(len(testlist))

#RANGE function: returnd a list of numbers that range from 0 to one less than the parameter, so range (4) becomes [0, 1, 2, 3]

print(range(8))


lijstje = 'Henk', 'Sjaak', 'Herman', 'Peter'
#combining range with len function can create useful loops, say for example, run this loop as many times as this list is long so:
for x in range(len(lijstje)):
    print(x)

#You can also use each entry of the list when going through like so:

for iter in range(len(lijstje)):
    deelnemer = lijstje[iter]
    print("Welkom:", deelnemer)

#OR you can do this by doing
for iter in lijstje:
    print("Welkom:", iter)
