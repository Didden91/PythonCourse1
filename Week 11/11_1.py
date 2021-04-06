import re

fhand = open('mbox.txt')

userinput = input('Enter a regular expression: ')
wordlist = list()

count = 0
for line in fhand:
    line = line.rstrip()
    stuff = re.findall(userinput, line)
    if len(stuff) != 1 : continue
    wordlist.append(stuff)

print('mbox.txt had',len(wordlist),'lines that matched',userinput)
