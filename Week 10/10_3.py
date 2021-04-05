import string

fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('invalid file name')
    quit()

dixie = dict()
listoflet = list()

for line in fhand:
    if len(line) < 1: continue
    words = line.split()
    words = str(words)
    words = words.translate(str.maketrans('', '', string.punctuation))
    words = words.lower()

    count = 0
    while count < 10:
        words = words.replace("%d" % count, "")
        count += 1
    words = words.replace(" ", "")

    for let in words:
        dixie[let] = dixie.get(let, 0) + 1

endlst = list()
for letter, count in dixie.items():
    newtup = count, letter
    endlst.append(newtup)

endlst = sorted(endlst, reverse=True)

for count, letter in endlst:
    print(letter, count)



# mbox-tiny.txt
