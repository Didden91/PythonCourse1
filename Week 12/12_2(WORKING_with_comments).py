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
altcount = 0
maxexceeded = 0
rest = 0

while True:
    data = mysock.recv(512)
    count = count + len(data)
    print('COUNT IS: ', count)
    if len(data) < 1:
        break

    for c in data:
        altcount += 1
    print('ALTCOUNT IS: ',altcount)
    if count <= 3000:
        print(data.decode(),end='')
    elif maxexceeded == 0 :
        rest = count - 3000
        rest = 512 - rest
        print('REST IS:',rest)
        print(data[:rest].decode(),end='')


        maxexceeded = 1

    # Zodra je 3000 overschrijd, draai EENMALIG een vergelijking,
    # neem het getal, dus bijvoorbeeld 3092 en doe dat min 3000, houd je 92 over, dat is hoeveel karakers je nog moet weergeven
    # weergeef die karakters door de datastroom te nemen, en te zeggen, van deze laatst ontvangen stroom van karakters, weergeef alleen 0 t/m het restgetal
    # bijvoorbeeld 92








mysock.close()

# http://data.pr4e.org/romeo.txt
# http://data.pr4e.org/romeo-full.txt
