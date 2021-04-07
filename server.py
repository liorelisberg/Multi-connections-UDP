## Server side
## for multi-connection UDP clients 
## Server should be running first, before clients connect to the server.
## UDP_IP & UDP_PORT are both on a default values.

import socket

UDP_IP = '127.0.0.1' # Standard loopback interface address (localhost)
UDP_PORT = 9999 # Port to listen on (non-privileged ports are > 1023)

#socket.AF_INET - port is an integer, socket.SOCK_DGRAM - UDP protocol,0 - protocol specified as 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 
sock.bind((UDP_IP,UDP_PORT)) 
print('SERVER IS ON\n')

clients = dict() # all clients will be registered in the clients dictionary for the current session.

while True:
    data, addr = sock.recvfrom(1024) # unpacking the received socket request.
    data = data.decode() # msg needs to be decoded first
    if addr in clients.values():
        data = data.split(": ")
        if data[0] in clients:
            sender = list(clients.keys())[list(clients.values()).index(addr)] # find the sender of the msg from clients' dict
            sock.sendto((sender+': '+data[1]).encode(),clients[data[0]]) # encode msg, send the sender's msg to the client
            print('A msg from client {} to client {}'.format(sender, data[0]))
        else: # if no valid client found to send to
            msg = "User Undefined"
            sock.sendto(msg.encode(),addr) # send an error msg back to the sender
    else: # if client's addr not known, add to clients
        clients[data] = addr
        print("Added to clients:")
        print(data, addr)
