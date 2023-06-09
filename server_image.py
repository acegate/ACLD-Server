import socket
import cv2
import numpy as np
from _thread import *
import base64
import threading
from datetime import datetime
import time
from util import Util

class Server:
    def __init__(self, HOST : str, PORT : int):
        self.__HOST = HOST
        self.__PORT = PORT
        self.STREAM_BYTE = 64
        self.__utility = Util()
        self.COUNT = 0
        self.__client_sockets = []
        self.server_open()

    def server_open(self) -> None:
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.get_server().setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 10)
        self.get_server().bind((self.get_host(), self.get_port()))
        self.get_server().listen()
        print('>> Server start')
        self.server_accept()

    def server_accept(self) -> None:
        while True:
            try:
                print('>> Server Wait!!')
                self.__client_socket, self.__addr = self.get_server().accept()
                self.get_util().create_folder(self.get_client_ip())
                self.get_client().settimeout(10000)
                self.add_client((self.COUNT, self.get_client()))
                thread = threading.Thread(target=self.receiveTarget)
                thread.start()
                self.COUNT += 1
            except Exception as e:
                self.get_client().close()
                self.get_server().close()
                self.__init__(self.get_host(), self.get_client())

    def receiveTarget(self):
        print('>> Connected by :', self.get_client_ip(), ':', self.get_client_port())
        img_count = 0
        while True:
            try:
                img_data = self.get_img()
                self.img_save(img_data, img_count)
                
                # img_data = self.get_img()
                # self.img_save(img_data, img_count)

                test = self.get_data()
                print(test)

                img_count += 1
                time.sleep(0.95)
            except Exception as e:
                print(e)
                self.get_client().close()
                break

    def recive_data(self, count : int) -> bytes:
        buf = b''
        while count:
            newbuf = self.get_client().recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf
    
    def get_img(self):
        recive_length = self.recive_data(self.STREAM_BYTE).decode('utf-8')
        recive_img = self.recive_data(int(recive_length))
        return np.frombuffer(base64.b64decode(recive_img), dtype='uint8')
       
    def img_save(self, buf_img, count):
        decimg = cv2.imdecode(buf_img, cv2.IMREAD_COLOR)
        cv2.imwrite(self.get_util().get_save_path(self.get_client_ip()) + '\\' + f'CAM_{self.get_client_ip()}_{count}.jpg', decimg)

    def get_data(self):
        data_length = self.get_client().recv(64).decode('utf-8')
        data = self.recive_data(int(data_length))
        return data

    
    def get_host(self):
        return self.__HOST
    
    def get_port(self):
        return self.__PORT
    
    def get_util(self):
        return self.__utility
    
    def get_client_count(self):
        return len(self.__client_sockets)
    
    def add_client(self, client):
        return self.__client_sockets.append(client)
    
    def get_client_ip(self):
        return self.__addr[0]
    
    def get_client_port(self):
        return self.__addr[1]
    
    def get_client(self):
        return self.__client_socket
    
    def get_server(self):
        return self.__server_socket
    

    

host_name = socket.gethostname()
HOST = socket.gethostbyname(host_name)
PORT = 9999

server = Server(HOST, PORT)