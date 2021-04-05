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
    words = words[5:6]
    tothours = list()
    for i in words:
        hours, minutes, seconds = i.split(":")
        tothours.append(hours)

    for word in tothours:
        dixie[word] = dixie.get(word, 0) + 1

endlst = list()
for hour, count in dixie.items():
    newtup = hour, count
    endlst.append(newtup)

endlst = sorted(endlst)
for hour, count in endlst:
    print(hour, count)






# mbox-short.txt
