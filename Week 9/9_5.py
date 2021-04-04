fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('invalid file name')
    quit()

dixie = dict()
for line in fhand:
    if not line.startswith('From '): continue
    line = line.rstrip()
    words = line.split() # THIS turns it into a list
    words = words[1:2]
    strwords = str(words)
    strwords = strwords.strip("['']")
    words = strwords.split('@')
    words = words[1:]
    for word in words:
        dixie[word] = dixie.get(word, 0) + 1

print(dixie)
