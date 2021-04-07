fhand = open('testje.txt')
count = 0

for line in fhand:
    count = count + len(line)

print(count)
