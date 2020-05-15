# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ----------------------------------------------------------------------------------------------------------------------
# Имя модуля: Agent.py
# Назначение: Правильный(ООП) интерактивный UDP-Client-server
# Версия интерпретатора: 3
# Автор: Дмитрий Ильюшкò ilyushko@itain.ru dm.ilyushko@gmail.com
# Создан: 10.04.2019
# Изменен: 
# Правообладатель:(c) ЗАО "Институт телекоммуникаций" www.itain.ru 2019
# Лицензия: MIT www.opensource.org/licenses/mit-license.php
# ----------------------------------------------------------------------------------------------------------------------

import socket as s
import threading

class UDP_Client_Server:
    host = ''
    port = 0
    sock = s.socket(s.AF_INET, s.SOCK_DGRAM)

    def init_socket(self):
        while True:
            print('enter IP : ')
            self.host = str(input())
            if (self.host == '0.0.0.0') or (self.host == 'localhost'):
                break
            else:
                print('host must be localhost or 0.0.0.0')
                continue
        try:
            print('enter PORT : ')
            self.port = int(input())
        except ValueError:
            print('Port must be integer with base 10')
            print('enter PORT : ')
            self.port = int(input())

        self.sock.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
        self.sock.setsockopt(s.SOL_SOCKET, s.SO_BROADCAST, 1)
        self.sock.bind((self.host, self.port))
        print('now listening port ', self.port, ' on IP ', self.host)

    def listen_sock(self):
        while 1:
            try:
                msg, addr = self.sock.recvfrom(256)
                msg = str(msg)[2:len(str(msg)) - 1]
                print(msg, 'from :', addr)
            except KeyboardInterrupt:
                print('input was interrupted by user')
                break
    def send_sock(self):
         while 1:
                print('enter text :')
                text = input()
                self.sock.sendto(text.encode('utf-8'),(self.host, self.port))

sck = UDP_Client_Server()
sck.init_socket()
threading.Thread(target=sck.listen_sock, daemon=True).start()
sck.send_sock()