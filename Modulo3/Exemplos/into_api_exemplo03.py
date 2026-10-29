# comunicação direta com sockets

import socket
cliente =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connec(("192.168.1.100", 9000))
cliente.sendall(b"STATUS\n")
resposta = cliente.recv(1024)
print(resposta.decode())

cliente.code()