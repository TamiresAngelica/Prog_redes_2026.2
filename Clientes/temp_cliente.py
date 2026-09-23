import socket
ip_servidor = "127.0.0.1"
porta =  5555

while True:
 msg_envio = "Sensor ativado e enviando sinal!"
 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 server.connect((ip_servidor, porta))
 server.send("Sensor ativado e enviando sinal!".encode())
 dados = server.recv(1024)
 msg = dados.decode()
 print(msg)
 continuar = input("Deseja enviar outra mensagem do cliente? [S/N]: ").upper()
 if continuar == "N":
    print("Encerrando cliente.")
    break