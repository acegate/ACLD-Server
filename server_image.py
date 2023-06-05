#!/usr/bin/python
import socket
import cv2
import numpy as np
from _thread import *
import base64
import threading
import os
import json
from datetime import datetime
import pymysql
import time

class Server:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.count = 0
        self.lock = threading.Lock()
        self.path = os.getcwd()
        self.YEAR = str(datetime.today().year)
        self.MONTH = str(datetime.today().month)
        self.DAY = str(datetime.today().day)
        self.ROOT_PATH = self.path + '\\' + self.YEAR + '\\' + self.MONTH + '\\' + self.DAY
        self.client_sockets = []
        self.server_open()

    def server_open(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()
        print('>> Server start')
        self.server_accept()

    def server_accept(self):
        while True:
            try:
                print('>> Server Wait!!')
                self.lock.acquire()
                self.client_socket, self.addr = self.server_socket.accept()
                self.client_socket.settimeout(100)
                thread = threading.Thread(target=self.receiveTarget)
                thread.start()
                self.lock.release()
                self.createFolder()
            except Exception as e:
                print(e)
                self.client_socket.close()

    def receiveTarget(self):
        print('>> Connected by :', self.addr[0], ':', self.addr[1])
        image_count = 0
        while True:
            try:
                length = self.recvall(self.client_socket ,64)

                if length != None:
                    decode_length = length.decode('utf-8')
                    stringData = self.recvall(self.client_socket, int(decode_length))
                    stime = self.recvall(self.client_socket, 64).decode('utf-8')
                    print(stime)

                    info_length = self.recvall(self.client_socket, 64)

                    if info_length != None:
                        info_decode_length = info_length.decode('utf-8')
                        infomation = self.recvall(self.client_socket, int(info_decode_length))
                        print(json.loads(infomation))

                        data = np.frombuffer(base64.b64decode(stringData), dtype='uint8')
                        decimg = cv2.imdecode(data, 1)
                        cv2.imwrite(self.ROOT_PATH + '\\' + str(self.addr[0]) + '\\' + f'{self.addr[0]}_{image_count}.png', decimg)
                        print(self.addr[0])
                        image_count += 1
                time.sleep(1)

            except Exception as e:
                print(e)
                print('>> Disconnected by ' + self.addr[0], ':', self.addr[1])
                self.client_socket.close()
                break

    def recvall(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf
    
    def createFolder(self):
        try:
            path = os.getcwd()
            if not os.path.exists(self.ROOT_PATH + '\\' + str(self.addr[0])):
                os.makedirs(self.ROOT_PATH + '\\' + str(self.addr[0]))
        except OSError:
            print('Error : Creating directory')

host_name = socket.gethostname()
HOST = socket.gethostbyname(host_name)
PORT = 9999

server = Server(HOST, PORT)