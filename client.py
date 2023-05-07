import socket
import threading

# Define o endereço IP e a porta de conexão do servidor
HOST = '192.168.0.106'  # Coloque seu ender
PORT = 3333         # Porta de conexão


def enviaMensagem(cliente):
    while True:
        try:
            mensagem = input('Cliente: ')
            cliente.send(mensagem.encode('utf-8'))
            
            if mensagem == 'exit':
                print('Encerrando conexão...')
                cliente.close()
                break
        except:
            pass
    
def recebeMensagem(cliente):
        while True:
            try:
                resposta = cliente.recv(1024).decode('utf-8')
                print('\nServidor: ',resposta)
                
            except:
                break


# Loop principal do cliente
def main():
    # Cria um objeto socket TCP/IP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta o socket ao endereço IP e à porta especificada
    cliente.connect((HOST, PORT))

    
    t1 = threading.Thread(target=recebeMensagem,args=[cliente])
    t2 = threading.Thread(target=enviaMensagem,args=[cliente])
    
    t1.start()
    t2.start()

    # while True:
        # Envia uma mensagem ao servidor
        # mensagem = input('Cliente: ')
        # cliente.send(mensagem.encode('utf-8'))

        # threading.Thread(target=enviaMensagem(cliente)).start()

        # Verifica se o usuário digitou "exit"
        # if mensagem == 'exit':
        #     print('Encerrando conexão...')
        #     cliente.close()
        #     break
        # threading.Thread(target=enviaMensagem).start()
        # threading.Thread(target=recebeMensagem).start()

        # Recebe a resposta do servidor
        # resposta = cliente.recv(1024).decode('utf-8')

        # Exibe a resposta recebida
        # print('Servidor:', resposta)

# Fecha a conexão
main()
# cliente.close()
