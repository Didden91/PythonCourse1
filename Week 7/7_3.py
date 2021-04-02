fname = input('Enter the file name: ')
count = 0
numbtotal = 0

if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    quit()


try:
    fhand = open(fname)
except:
    print('Invalid file name')
    exit()



for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        foundnumbers = line[20:]
        foundnumbers = float(foundnumbers)
        numbtotal = numbtotal + foundnumbers
print('Average spam confidence:',numbtotal / count)
