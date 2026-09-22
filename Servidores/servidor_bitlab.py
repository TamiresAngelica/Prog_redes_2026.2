import socket
import webbrowser

ip_cliente = "127.0.0.1"
porta = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip_cliente, porta))

server.listen(10)  # número de conexões


while True:

    conn, endereco = server.accept()

    dados = conn.recv(1024)

    comando = dados.decode()

    print(comando)

    while True:

        print("""
        1 - Abrir página do laboratório LAICA
        2 - SAIR
        """)

        op = int(input("DIGITE A OPÇÃO DESEJADA: "))

        while op != 1 and op != 2:
            print("Opção inválida!")
            op = int(input("DIGITE A OPÇÃO DESEJADA: "))

        if op == 1:

            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            url = "https://laica.ifrn.edu.br/"

            webbrowser.register(
                'chrome',
                None,
                webbrowser.BackgroundBrowser(chrome_path)
            )

            webbrowser.get('chrome').open_new_tab(url)

            conn.send("Página aberta!".encode())

            print("Página aberta!")

            r = input("Deseja continuar [S/N]: ").upper()[0]

            while r != "S" and r != "N":
                print("Opção inválida!")
                r = input("Deseja continuar [S/N]: ").upper()[0]

            if r == "N":
                conn.close()
                break

            # Se for S, volta para o menu
            if r == "S":
                continue

        elif op == 2:

            conn.send("Servidor encerrando!".encode())

            conn.close()

            break

    if op == 2 or r == "N":
        break


server.close()