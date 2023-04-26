import socket

# Define o endereço IP e a porta de conexão do servidor
HOST = ''  # Coloque seu ender
PORT = 5000         # Porta de conexão

# Cria um objeto socket TCP/IP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket ao endereço IP e à porta especificada
cliente.connect((HOST, PORT))

# Loop principal do cliente
while True:
    # Envia uma mensagem ao servidor
    mensagem = input('Cliente: ')
    cliente.send(mensagem.encode('utf-8'))

    # Verifica se o usuário digitou "exit"
    if mensagem == 'exit':
        print('Encerrando conexão...')
        cliente.close()
        break

    # Recebe a resposta do servidor
    resposta = cliente.recv(1024).decode('utf-8')

    # Exibe a resposta recebida
    print('Servidor:', resposta)

# Fecha a conexão
cliente.close()
