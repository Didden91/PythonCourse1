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

    print(words)

    words = words.translate(str.maketrans('', '', string.punctuation))
    words = words.lower()
    print(words)

    #What I looked up, which worked but of which I'm not sure what it does
    # words = ''.join(i for i in words if not i.isdigit())

    # What I did, and it FUCKING WORKS
    count = 0
    while count < 10:
        words = words.replace("%d" % count, "")
        count += 1
    words = words.replace(" ", "")

    print(words)

    # for letters in words:                             DIT         < gotta review this shit
    #     print("LETTERS:",letters)                     WAS         < gotta review this shit
    #     listoflet.append(letters)                     DE          < gotta review this shit
    # print("LISTOFLETTERS:",listoflet)                 BUG!!       < gotta review this shit
    for let in words:
        print("Iteration of let:",let)
        dixie[let] = dixie.get(let, 0) + 1
        print(dixie)

print(dixie)

endlst = list()
for letter, count in dixie.items():
    newtup = letter, count
    endlst.append(newtup)

endlst = sorted(endlst)

for letter, count in endlst:
    print(letter, count)



# mbox-tiny.txt
