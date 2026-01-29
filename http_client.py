# Name: Ramanpreet Grover
# Student ID: N01698437
# Course: CPAN-226
# Lab 1 – HTTP Client using Sockets

from socket import *

server_name = 'gaia.cs.umass.edu'
server_port = 80

# Create TCP socket (IPv4)
client_socket = socket(AF_INET, SOCK_STREAM)

# Connect to server
client_socket.connect((server_name, server_port))

# HTTP GET request
request = (
    "GET /kurose_ross/interactive/index.php HTTP/1.1\r\n"
    "Host: gaia.cs.umass.edu\r\n"
    "\r\n"
)

client_socket.send(request.encode())
response = client_socket.recv(4096)
print(response.decode())

client_socket.close()
