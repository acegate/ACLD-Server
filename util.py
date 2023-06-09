import os
from datetime import datetime
import json

class Util:
    def __init__(self):
        self.__path = os.getcwd()
        self.YEAR = datetime.now().year
        self.MONTH = '%02d' % datetime.now().month
        self.DAY = '%02d' % datetime.now().day
        self.YEAR, self.MONTH, self.DAY = list(map(str, [self.YEAR, self.MONTH, self.DAY]))

    def create_folder(self, ip) -> None:
        try:
            if not os.path.exists(self.get_path() + '\\' + str(ip)):
                os.makedirs(self.get_path() + '\\' + str(ip))
        except OSError:
            print('Error : Creating directory')

    def get_save_path(self, ip):
        return self.get_pwd_path() + '\\' + self.YEAR + '\\' + self.MONTH + '\\' + self.DAY + '\\' + str(ip)
    
    def get_path(self):
        return self.get_pwd_path() + '\\' + self.YEAR + '\\' + self.MONTH + '\\' + self.DAY
    
    def get_pwd_path(self):
        return self.__path
    
    