# -*- coding: utf-8 -*-

import cryptocode
import socket
import os
os.system('clear')


def ServerMain():
    server_ip = str(input('CONNECTION IP (Ex: "localhost"): '))  # Ip que será usado na conexão
    server_port = int(input('CONNECTION PORT (Ex: "8888"): '))  # Porta que será usada na conexão
    key = input('Key: ')

    os.system('clear')

    color_yellow = '\033[1;33m'
    color_reset = '\033[0;0m'
    color_cyan = '\033[1;36m'

    # Comunicação de client-side e server-side através do protocolo TCP-IP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Estabelece conexão com ip e porta informados
    server.bind((server_ip, server_port))
    print('Connected!')

    # Função para escutar as conexões que estão sendo 'ditas'
    server.listen()
    client, addr = server.accept()  # Aceita as conexões

    # Loop será alterado somente quando o valor for alterado
    end = False

    while not end:
        # Informação de quantidade de bits passando, decodificação utf-8 e recebimento da msg
        msg = client.recv(1024).decode('utf-8')

        # Verificação
        if msg == '/exit':
            end = True
        else:
            print(
                f'{color_yellow}(CLIENT)({server_ip}:{server_port}){color_reset} --> ' + cryptocode.decrypt(msg, key))  # Print de msg recebida
        # Mensagem que será enviada
        client.send(cryptocode.encrypt(input(f'{color_cyan}(YOU) -->{color_reset}  '), key).encode('utf-8'))
    client.close()  # Fecha conexão com client
    server.close()  # Fecha conexão com server
    exit()  # Fecha script


ServerMain()
