import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Conectando ao servidor...")
cliente.connect(("127.0.0.1", 5000))
print("Cliente conectado")
mensagem_envio = "Olá Servidor!"
cliente.send(mensagem_envio.encode("utf-8"))
print(f"Mensagem enviada: {mensagem_envio}")
dados_resposta = cliente.recv(1024)
resposta_servidor = dados_resposta.decode("utf-8")
print(f"Resposta recebida do servidor: {resposta_servidor}")
cliente.close()
print("Conexão do cliente encerrada.")