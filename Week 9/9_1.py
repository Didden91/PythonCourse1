fhand = open('words.txt')

wordsdict = dict()

for line in fhand:
    words = line.split()
    for word in words:
        wordsdict[word] = 0
print(wordsdict)
