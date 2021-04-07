## client side
## for multi-connection UDP clients 
## server should be running first, before clients connect to the server.
## Server's IP and Port are both on a default values.

from threading import Thread
import socket
import sys

server_addr = ('127.0.0.1', 9999) # server's default address

# socket.AF_INET - port is an integer, socket.SOCK_DGRAM - UDP protocol,0 - protocol specified as 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
my_name = input('Enter your name: ')
sock.sendto(my_name.encode(), server_addr) # encodes msg, send the client's name to the server to be added

def output_recvfrom(sock):
    while True:
        data, _ = sock.recvfrom(1024) # unpacking the received socket request.
        if not data:
            break
        print(data.decode()) #prints received & decoded data to the client. 


# creates a thread that will listen to received data from the server and will call the output_recvfrom with that data
x = Thread(target=output_recvfrom, args=(sock, )) 
x.start()

for line in sys.stdin:
    sock.sendto(line.strip().encode(), server_addr) # encodes msg, sends the client's msg to the server to pass to another client
    
sock.close() 
x.join() # close socket and kill thread.
