import socket
import threading


HOST = '192.168.0.106'
PORT = 5555


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((HOST, PORT))


def receive():
    while True:
        try:
 
            message = client_socket.recv(1024).decode()


            if message == 'exit':
                client_socket.close()
                break


            print(message)
        except:
         
            client_socket.close()
            break


def send():
    while True:

        message = input()


        if message == 'exit':
            client_socket.send('exit'.encode())
            client_socket.close()
            break


        client_socket.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
