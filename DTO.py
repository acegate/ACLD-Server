import pymysql
from datetime import datetime
import time

class Report:
    __report_no_PK = 0
    __log_no_FK = 0
    __content = None
    __status = 0
    __create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    __update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_report_no(self):
        return self.__report_no_PK
    
    def get_log_no(self):
        return self.__log_no_FK
    
    def get_content(self):
        return self.__content
    
    def get_status(self):
        return self.__status
    
    def get_create_at(self):
        return self.__create_at
    
    def get_update_at(self):
        return self.__update_at
    
    def set_report_no(self, report_no):
        self.__report_no_PK = report_no

    def set_log_no(self, log_no):
        self.__log_no_FK = log_no

    def set_content(self, content):
        self.__content = content
    
    def set_status(self, status):
        self.__status = status


class Log:
    __log_no_PK = 0
    __CAMimage_path = ''
    __screenshot_path = ''
    __detectiontype = 0
    __status = 0
    __create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    __update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_log_no(self):
        return self.__log_no_PK
    
    def get_camimg_path(self):
        return self.__CAMimage_path
    
    def get_screenshot_path(self):
        return self.__screenshot_path
    
    def get_detectiontype(self):
        return self.__detectiontype
    
    def get_status(self):
        return self.__status
    
    def get_create_at(self):
        return self.__create_at
    
    def get_update_at(self):
        return self.__update_at
    
    def set_log_no(self, log_no):
        self.__log_no_PK = log_no

    def set_camimg_path(self, path):
        self.__CAMimage_path = path

    def set_screenshot_path(self, path):
        self.__screenshot_path = path

    def set_detectiontype(self, type):
        self.__detectiontype = type

    def set_status(self, status):
        self.__status = status


class Employee:
    __MAC_Address = None
    __part_no_FK = 0
    __name = None
    __employee_img_path = None
    __phone_number = 0
    __position = None
    __rank = 0
    __join_day = None
    __create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    __update_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def get_mac_address(self):
        return self.__MAC_Address
    
    def get_part_no(self):
        return self.__part_no_FK
    
    def get_name(self):
        return self.__name
    
    def get_employee_img_path(self):
        return self.__employee_img_path
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_position(self):
        return self.__position
    
    def get_rank(self):
        return self.__rank
    
    def get_join_day(self):
        return self.__join_day
    
    def get_creata_at(self):
        return self.__create_at
    
    def get_update_at(self):
        return self.__update_at
    
    
    def set_mac_address(self, MAC_address):
        self.__MAC_Address = MAC_address

    def set_part_no(self, part_no):
        self.__part_no_FK = part_no

    def set_name(self, name):
        self.__name = name

    def set_employee_img_path(self, path):
        self.__employee_img_path = path
    
    def set_phone_number(self, phone_number):
        self.__phone_number =phone_number

    def set_position(self, position):
        self.__position = position

    def set_rank(self, rank):
        self.__rank = rank
    
    def set_join_day(self, day):
        self.__join_day = day

class Department:
    __part_no_PK = 0
    __name = None
    __position = None

    def get_part_no(self):
        return self.__part_no_PK

    def get_name(self):
        return self.__name
    
    def get_position(self):
        return self.__position

    def set_part_no(self, part_no):
        self.__part_no_PK = part_no

    def set_name(self, name):
        self.__name = name

    def set_position(self, position):
        self.__position = position

class Agent:
    __agent_no = 0
    __MAC_Address = None
    __log_no_FK = 0
    __IP = None

    def get_agent_no(self):
        return self.__agent_no
    
    def get_MAC_address(self):
        return self.__MAC_Address
    
    def get_log_no(self):
        return self.__log_no_FK
    
    def get_ip(self):
        return self.__IP
    
    def set_agent_no(self, agent_no):
        self.__agent_no = agent_no

    def set_mac_address(self, mac_address):
        self.__MAC_Address = mac_address

    def set_log_no(self, log_no):
        self.__log_no_FK = log_no

    def set_ip(self, ip):
        self.__IP = ip


    
