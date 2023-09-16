# Listener/Server
import socket
import subprocess

host = '127.0.0.1'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Listening for incoming connections on {host}:{port}")

conn, addr = server.accept()
print(f"Connection from {addr[0]}:{addr[1]}")

while True:
    command = input("Shell> ")
    conn.send(command.encode())

    if command.lower() == "exit":
        break

    output = conn.recv(1024)
    print(output.decode(), end='')

conn.close()
