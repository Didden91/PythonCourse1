# FOR REFERENCE:
#YOUR PROGRAM =
#SOCKET
#CONNECT
#SEND
#RECV


import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET makes that it is suitable to go accross the internet
#The SOCK_STREAM makes it able to stream data
mysock.connect( ('data.pr4e.org', 80) )

#With the socket in place, let's write a command to send using the socket
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

#I had to add \r\n\r\n instead of \n\n to make it work, he mentioned this could happen, so it's fine

#That puts that whole command, encoded through the .encode() method, into the cmd variable
#now let's send it using
mysock.send(cmd)

#now to check if we're receiving data and to close the socket once we stop receiving date
while True:
    data = mysock.recv(512)     #call the receive method on mysock with a maximum of 512 characters at a time,
                                # and place received data in variable called data
    if (len(data) < 1) :
        break                   # If the amount of data is less than 1, aka 0, break out of the loop,
                                # because this probably means we've received all the data
    print(data.decode(),end='')        # print the received decoded version of the data
                                    #other little dink in the code, without the end='' it prints upto the middle of the last line and then
                                    #prints the rest in a new line, presumably because it hits that 512 character limit we enstated.
                                    #I believe the end='' does something like, finish the decode at the first empty character you hit,
                                    #so when it hits a newline or something.
mysock.close()                      # closes the sockets once you're done looping

#This program prints all the HEADERS FIRST, which look like this:

# HTTP/1.1 200 OK
# Date: Sun, 10 Jan 2021 13:28:55 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "a7-54f6609245537"
# Accept-Ranges: bytes
# Content-Length: 167
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain

#Followed by A BLANK LINE, followed by the DATA YOU REQUESTED
#Sooo.. if you want to parse only the DATA you want, first search for that initial BLANK LINE!
