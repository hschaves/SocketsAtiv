#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import threading

HOST = 'localhost'
PORT = 8888

def receive_data(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))

    sock.close()

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f'Conectado ao servidor {HOST}:{PORT}')

        user_input = input('Digite dois números inteiros separados por espaço: ')
        client.sendall(user_input.encode('utf-8'))

        receive_thread = threading.Thread(target=receive_data, args=(client,))
        receive_thread.start()

        receive_thread.join()

    finally:
        print('Conexão encerrada')
        client.close()

if __name__ == '__main__':
    main()


# In[ ]:




