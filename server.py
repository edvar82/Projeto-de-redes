import socket

# Define o endereço IP e a porta de conexão do servidor
HOST = ''  # Endereço IP do servidor
PORT = 5000         # Porta de conexão

# Cria um objeto socket TCP/IP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket ao endereço IP e à porta especificada
servidor.bind((HOST, PORT))

# Define o número máximo de conexões simultâneas
servidor.listen(1)

# Espera por uma conexão
print('Aguardando conexão...')
conexao, endereco = servidor.accept()
print('Conexão estabelecida com:', endereco)

# Loop principal do servidor
while True:
    # Recebe a mensagem do cliente
    mensagem = conexao.recv(1024).decode('utf-8')

    # Verifica se a mensagem é vazia
    if not mensagem:
        print('Encerrando conexão...')
        conexao.close()
        break

    # Verifica se o usuário digitou "exit"
    if mensagem == 'exit':
        print('Encerrando conexão...')
        conexao.close()
        break

    # Exibe a mensagem recebida
    print('Cliente:', mensagem)

    # Envia uma mensagem de resposta ao cliente
    resposta = input('Servidor: ')
    conexao.send(resposta.encode('utf-8'))

# Fecha a conexão
conexao.close()
