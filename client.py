# -*- coding: utf-8 -*-

import socket
import os
os.system('clear')


def ClientMain():
    server_ip = str(input('CONNECTION IP (Ex: "localhost"): '))  # Ip que será usado na conexão

    server_port = int(input('CONNECTION PORT (Ex: "8888"): '))  # Porta que será usada na conexão

    os.system('clear')

    color_yellow = '\033[1;33m'
    color_reset = '\033[0;0m'

    # Comunicação de client-side e server-side através do protocolo TCP-IP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Estabelece conexão com ip e porta informados
    client.connect((server_ip, server_port))
    print('Connected!')

    # Loop será alterado somente quando o valor for alterado
    end = False
    print('Write "/exit" to exit\n')

    while not end:
        # Informação de quantidade de bits passando e decodificação utf-8
        # Mensagem que será enviada
        client.send(input('Message: ').encode('utf-8'))
        msg = client.recv(1024).decode('utf-8')

        if msg == '/exit':  # Mensagem para fim de conexão
            end = True
        else:
            print(
                f'{color_yellow}(SERVER)({server_ip}:{server_port}){color_reset} --> ' + msg)  # Print da msg recebida
    client.close()  # Fecha a conexão com client
    exit()  # Fecha script


ClientMain()
