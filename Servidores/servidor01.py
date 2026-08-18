import socket 


servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor.bind(("127.0.0.1", 5000))
servidor.listen(5)
print("Aguardando conexões...")
socket_cliente, endereco_cliente = servidor.accept()
print('Servidor conectado ao cliente')
dados = socket_cliente.recv(1024)
mensagem = dados.decode("utf-8")
print(f" Mensagem recebida do cliente: {mensagem}")
resposta = "Mensagem recebida com sucesso pelo servidor!"
socket_cliente.send(resposta.encode("utf-8"))
socket_cliente.close()
servidor.close()
print("Conexões encerradas.")
