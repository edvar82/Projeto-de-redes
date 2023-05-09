import socket
import threading

HOST = '192.168.0.106'
PORT = 5555


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((HOST, PORT))


server_socket.listen()


clients = []


def handle_client(client_socket, client_address):
    # Adiciona o cliente à lista de clientes conectados
    clients.append(client_socket)

    # Envia uma mensagem de boas-vindas ao cliente
    client_socket.send('Bem-vindo ao chat!'.encode())


    while True:
        try:
            # Recebe uma mensagem do cliente
            message = client_socket.recv(1024).decode()


            if message == 'exit':
                client_socket.send('exit'.encode())
                clients.remove(client_socket)
                client_socket.close()
                break


            for client in clients:
                client.send(f'{client_address[0]}:{client_address[1]} diz: {message}'.encode())

        except:
            # Remove o cliente da lista de clientes conectados
            clients.remove(client_socket)
            client_socket.close()
            break


while True:
    # Aceita uma nova conexão do cliente
    client_socket, client_address = server_socket.accept()

    # Cria uma nova thread para tratar as mensagens do cliente
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()