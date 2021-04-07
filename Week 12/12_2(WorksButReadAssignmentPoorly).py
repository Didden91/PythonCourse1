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
while True:
    if count >= 3000:
        break
    if count + 512 < 3000:
        data = mysock.recv(512)     # if count plus 512 is less than 3000, receive next 512
    else:
        data = mysock.recv(3000 - count)   #else receive 3000 - count
    if len(data) < 1:
        break
    for c in data.decode():
        count += 1

    print(data.decode())

print(count)

mysock.close()

# http://data.pr4e.org/romeo.txt
# http://data.pr4e.org/romeo-full.txt
