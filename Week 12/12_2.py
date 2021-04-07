import socket

userinp = input('Enter a URL: ')

try:
    inpparts = userinp.split('/')
    hostname = str(inpparts[2])
except:
    print('invalid url')
    quit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((hostname, 80))
except:
    print('invalid url')
    quit()

cmdstring = 'GET %s HTTP/1.0\r\n\r\n' % userinp
cmd = cmdstring.encode()
mysock.send(cmd)

count = 0
maxexceeded = 0

while True:
    data = mysock.recv(512)
    count = count + len(data)
    if len(data) < 1:
        break

    if count <= 3000:
        print(data.decode(),end='')
    elif maxexceeded == 0 :
        rest = count - 3000
        rest = len(data) - rest
        print(data[:rest].decode())
        maxexceeded = 1
        totalprinted = count - len(data) + rest

        print('Characters printed:', totalprinted)

print('Total number of characters: ',count)

mysock.close()

# http://data.pr4e.org/romeo.txt
# http://data.pr4e.org/romeo-full.txt
