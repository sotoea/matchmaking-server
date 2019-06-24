#!/usr/bin/env python
import socket
import sys
import thread
import signal

clients = []

def handle_exit(killsocket):
    killsocket.close()


def client_handler(clientsocker, addr):
    try:
        print >>sys.stderr, 'connection from ', addr
        while True:
            data = clientsocker.recv(1024)
            #print >>sys.stderr, 'received "$s"' % data
            if(len(clients) > 1):
                clientsocker.sendall(b(clients[0]), " ", b(clients[1]), "                    ")
                print(clients)
                clients.pop()
                clients.pop()
            
            if data:
                print >>sys.stderr, 'sending back to ', addr
                clientsocker.sendall(b'Searching for Other Players...')
    finally:
        clientsocker.close()
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('0.0.0.0', 80)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    clients.append[client_address]
    #client_handler(connection, client_address)
    thread.start_new_thread(client_handler, (connection, client_address))

atexit.register(handle_exit,sock)
signal.signal(signal.SIGTERM, handle_exit,sock)
signal.signal(signal.SIGINT, handle_exit,sock)
sock.close()