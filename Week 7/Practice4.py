filename = input('please enter a file name:')
try:
    fhand = open(filename)
except:
    print('Invalid filename:',filename)
    exit()

count = 0
for lines in fhand:
    if lines.startswith('Dit'):
        count = count + 1

print('Number of lines with Dit:',count)
