import re

userinput = input('Enter a file name: ')
try:
    fhand = open(userinput)
except:
    print('invalid file name')
    quit()

total = 0

for line in fhand:
    line = line.rstrip()
    thing = re.findall('[0-9]+', line)
    if len(thing) < 1 : continue
    for num in thing:
        num = int(num)
        total = total + num

print('TOTAL:',total)


#regex_sum_42.txt
