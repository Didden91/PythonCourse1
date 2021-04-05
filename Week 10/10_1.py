fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('invalid file name')
    quit()

dixie = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    words = words[1:2]
    for word in words:
        dixie[word] = dixie.get(word, 0) + 1

#There is now a histogram in dixie
lst = list()

for email, count in dixie.items():
    newtup = (count, email)
    lst.append(newtup)
lst = sorted(lst, reverse=True)

for value, key in lst[:1]:
    print(key, value)





# mbox-short.txt
