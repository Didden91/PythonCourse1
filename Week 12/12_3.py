import urllib.request, urllib.parse, urllib.error

userinp = input('Enter a URL: ')

try:
    fhand = urllib.request.urlopen(userinp)
except:
    print('invalid url')
    quit()
count = 0
maxexceeded = 0

for line in fhand:
    count = count + len(line)
    if count >= 3000:
        if maxexceeded == 0:
            rest = count - 3000
            rest = len(line) - rest
            print(line[:rest].decode())
            maxexceeded = 1
            totalprinted = count - len(line) + rest
            print('Total characters printed:', totalprinted)
    else:
        print(line.decode(), end='')

print('Total number of characters:',count)










# count = 0
# maxexceeded = 0
#
# while True:
#     data = mysock.recv(512)
#     count = count + len(data)
#     if len(data) < 1:
#         break
#
#     if count <= 3000:
#         print(data.decode(),end='')
#     elif maxexceeded == 0 :
#         rest = count - 3000
#         rest = len(data) - rest
#         print(data[:rest].decode())
#         maxexceeded = 1
#         totalprinted = count - len(data) + rest
#
#         print('Characters printed:', totalprinted)
#
# print('Total number of characters: ',count)
#

# http://data.pr4e.org/romeo.txt
# http://data.pr4e.org/romeo-full.txt
