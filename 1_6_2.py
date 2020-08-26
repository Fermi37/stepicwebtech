# Echo server program
import os
import socket
import sys

HOST = '0.0.0.0'  # Symbolic name meaning all available interfaces
PORT = 2222  # Arbitrary non-privileged port

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.bind((HOST, PORT))
sckt.listen(1)

while True:
    conn, addr = sckt.accept()
    child_pid = os.fork()
    if child_pid == 0:
        data = conn.recv(1024)
        if data == 'close':
            break
        conn.sendall(data)
        conn.close()
        sys.exit()
    else:
        conn.close()

sckt.close()
