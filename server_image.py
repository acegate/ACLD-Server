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
                self.client_socket, self.addr = self.server_socket.accept()
                self.utility.create_folder(self.addr[0])
                self.client_socket.settimeout(100)
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
                # length = self.recvall(self.client_socket, 64).decode('utf-8')
                screen_shot = self.recvall_Test()

                # length = self.recvall(self.client_socket ,64)
                # cam_img = self.recvall_Test()
 
                # nowtime = self.recvall_Test()
                # print(nowtime)
                # info_length = self.recvall(self.client_socket, 64)

                # info_decode_length = info_length.decode('utf-8')
                # infomation = self.recvall_Test()

                screen_shot_data = np.frombuffer(base64.b64decode(screen_shot), dtype='uint8')
                # cam_img_data = np.frombuffer(base64.b64decode(cam_img), dtype='uint8')
                
                decimg = cv2.imdecode(screen_shot_data, 1)
                cv2.imwrite(self.utility.get_path(self.addr[0]) + '\\' + f'screen_shot_{img_count}.png', decimg)
                # decimg = cv2.imdecode(cam_img_data, cv2.IMREAD_UNCHANGED)

                # cv2.imwrite(self.ROOT_path + '\\' + str(self.addr[0]) + '\\' + f'{self.addr[0]}_{img_count}.png', decimg)

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
    

    def recvall_Test(self):
        data = b""
        while True:
            packet = self.client_socket.recv(4096)
            if not packet:
                break
            data += packet
        return data

    

host_name = socket.gethostname()
HOST = socket.gethostbyname(host_name)
PORT = 9999

print(HOST)

server = Server(HOST, PORT)