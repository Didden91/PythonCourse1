finp = input("enter a file name: ")
try:
    fhand = open(finp)
except:
    print("file not found")
    quit()

count = 0
for line in fhand:
    if line.startswith('From'):
        if len(line) < 2: continue
        if line.startswith('From:') : continue
        pieces = line.split()
        count = count + 1
        print(pieces[1])
print("There were %d lines in the file with From as the first word" %count)
