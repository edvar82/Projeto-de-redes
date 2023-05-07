import socket
import threading
# Define o endereço IP e a porta de conexão do servidor
HOST = '192.168.0.106'  # Endereço IP do servidor
PORT = 3333         # Porta de conexão

# Cria um objeto socket TCP/IP

# Espera por uma conexão
    
# Loop principal do servidor


def main():
    
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liga o socket ao endereço IP e à porta especificada
    servidor.bind((HOST, PORT))

    #Define o número máximo de conexões simultâneas
    servidor.listen(2)
    print('Aguardando conexão...')

    conexao, endereco = servidor.accept()
    
    
    print('Conexão estabelecida com:', endereco)

    threading.Thread(target=recebeMensagem, args=[conexao]).start()
    # t2 = threading.Thread(target=enviaMensagem,args=[conexao])
    # t2.start()
        

    # while True:
        # Recebe a mensagem do cliente
        # mensagem = conexao.recv(1024).decode('utf-8')

        # Verifica se a mensagem é vazia
        # if not mensagem:
        #     print('Encerrando conexão...')
        #     conexao.close()
        #     break

        # break
        # t1.start()
        # enviaMensagem(conexao)

        
        # t2 = threading.Thread(target=enviaMensagem, args=conexao).start()

        # t2.start()

        # # Verifica se o usuário digitou "exit"
        # if mensagem == 'exit':
        #     print('Encerrando conexão...')
        #     conexao.close()
        #     break

        # # Exibe a mensagem recebida
        # print('Cliente:', mensagem)

        # Envia uma mensagem de resposta ao cliente
        # resposta = input('Servidor: ')
        # conexao.send(resposta.encode('utf-8'))
        
    # conexao.close()

def recebeMensagem(conexao):
    while True:
        try:
            mensagem = conexao.recv(1024).decode('utf-8')
            print('Cliente: ', mensagem)
            enviaMensagem(conexao)
        except:
            pass

def enviaMensagem(conexao):
    # while True:
    #     try:
        resposta = input('Servidor: ')
        conexao.send(resposta.encode('utf-8'))
        # except:
        #     pass
        
# Fecha a conexão
main()
