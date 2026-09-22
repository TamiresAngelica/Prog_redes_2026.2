import socket
import webbrowser 

ip_servidor = "127.0.0.1"
porta = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((ip_servidor, porta))
server.send("/abrir".encode())
dados = server.recv(1024)
comando = dados.decode()
print(comando)

       