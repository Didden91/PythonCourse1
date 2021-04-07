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

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

# http://data.pr4e.org/romeo.txt
