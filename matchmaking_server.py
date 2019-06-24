#!/usr/bin/env python
import socket
import sys
import thread
def client_handler(clientsocker, addr):
    try:
        print >>sys.stderr, 'connection from ', addr
        while True:
            data = clientsocker.recv(1024)
            #print >>sys.stderr, 'received "$s"' % data
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
    #client_handler(connection, client_address)
    thread.start_new_thread(client_handler, (connection, client_address))
sock.close()