import socket

ip_cliente = "0.0.0.0"
porta = 5555


sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind((ip_cliente, porta))

sever.listen(10)
leituras = []
print('Aguardando conexões')

while True:
    conn, endereço = sever.accept()
    dados = conn.recv(1024)
    msg = dados.decode()
    print(msg)
    s = input('Nome do sensor [Ex.: sensor01]: ').lower() 
    t = float(input('Digite a temperatura: [Ex.: 25.5 ou 20]:'))
    c = input('Deseja continuar: [S/N]').upper()[0]
    while c != "S" and c != "N":
        print("RESPOSTA INVÁLIDA")
        c = input('Deseja continuar: [S/N]').upper()[0]
    dic_sensor = {"nome":s, "temperatura": t}
    leituras.append(dic_sensor)
        # Mostra como a sua lista de dicionários está ficando na memória
    print(f"Lista atual de leituras: {leituras}\n")
    if c == "N":
        conn.close()
        break


