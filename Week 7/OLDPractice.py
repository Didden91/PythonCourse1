filehandler = open('test.txt')
for line in filehandler:
#    line = line.rstrip()
    print(line)

length = filehandler.read()
asdasd = len(length)
print('Test 1:',asdasd)
print('Test 2:',len(length))
print(length[:10])
