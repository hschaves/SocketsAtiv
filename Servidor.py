#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

def calculate_sum_of_even_numbers(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    total_sum = 0
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            total_sum += i
    return total_sum

HOST = 'localhost'
PORT = 8888

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f'Servidor TCP está ouvindo na porta {PORT}')

    while True:
        conn, addr = server.accept()
        print(f'Cliente conectado: {addr}')

        data = conn.recv(1024).decode('utf-8')
        num1, num2 = map(int, data.split())

        result = calculate_sum_of_even_numbers(num1, num2)

        conn.send(f'A soma dos números pares entre {num1} e {num2} é: {result}\n'.encode('utf-8'))
        conn.close()
        print('Cliente desconectado')

if __name__ == '__main__':
    main()


# In[ ]:




