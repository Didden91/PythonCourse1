import re

userinput = input('Enter a file name: ')
try:
    fhand = open(userinput)
except:
    print('invalid file name')
    quit()

count = 0
total = 0

for line in fhand:
    line = line.rstrip()
    thing = re.findall('New Revision: ([0-9]+)', line)
    if len(thing) != 1 : continue
    thing = float(thing[0])
    total = total + thing
    count += 1

average = total / count
print(int(average))
