#Now to learn a little bit about how we talk to resources on the network
#We're going to be using the Transport Control Protocol (TCP)
#This means we won't be going over the internet, but rather over a direct line between two programs: Peer-to-Peer
#So a process running on one computer, communicating with a process running on a another computer
#In Computer terms we call the data 'phonecall' between these procceses a SOCKET
#On your side you could use a webbrowser like Chrome
#On the other side could be a webserver like Apache, or nginx, or Microsoft IIS, services that receive and process your 'call'
#The 'phonecall' between these processes is the SOCKET

#TCP ports: can be seen as extensions to your call: you can call an address, but that address could host multiple things:
# Calling e.g. 192.168.1.1 might not be clear enough, you might need to add :80 or :21, depending on what service from that address you're looking for
#Common TCP ports include :80 for HTTP, :443 for HTTPS, :21 for FTP etc.

#Now, to PYTHON!
#In python we can use sockets very easily, python has built in support

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #in the socket LIBRARY, you call the socket method,
#and place the socket OBJECT in the variable mysock
#What this does is sort of like opening a filehandle, but one that is not yet finished
#It creates a socket, but does not yet associate it

mysock.connect( ('data.pr4e.org', 80) )

#Then you call the connect method, saying, hey socket called mysock, make the call to this thing:
#followed by the host and port
#The data.pr4e.org is the HOST, the 80 is the PORT
