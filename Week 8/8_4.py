fhand = open('romeo.txt')
finallist = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word in finallist: continue
        finallist.append(word)

finallist.sort()
print(finallist)
