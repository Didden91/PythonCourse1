fhand = open('test.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('Dit'):
        print(line)

    if not 'test' in line :
        continue
    print(line)

for line in fhand:
    line = line.rstrip()
    if not 'test' in line :
        continue
    print(line)
    print('poop')
