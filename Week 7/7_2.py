fname = input('Enter the file name: ')
count = 0
numbtotal = 0
try:
    fhand = open(fname)
except:
    print('Invalid file name')
    exit()

#print(fhand)

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        foundnumbers = line[20:]
        foundnumbers = float(foundnumbers)
        numbtotal = numbtotal + foundnumbers
print('Average spam confidence:',numbtotal / count)
