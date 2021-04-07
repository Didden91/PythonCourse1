import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )

#So now we have a socket, what do we want to do with it, what problem do we want to solve?
#What are we going to SEND, and what do we expect to GET BACK
#That is what we call the APPLICATION PROTOCOL
#The protocol we'll mostly be using in this section is the HTTP protocol
