fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('invalid file name')
    quit()

dixie = dict()
for line in fhand:
    if not line.startswith('From'): continue
    words = line.split()
    words = words[2:3]
    for word in words:
        dixie[word] = dixie.get(word, 0) + 1
print(dixie)
