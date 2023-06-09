import pymysql


class DataTransferObject:
    def __init__(self, HOST):
        self.__HOST = HOST
        self.db_connection()

    def db_connection(self):
        try:
            self.conn = pymysql.connect(self.get_host(), user='jeawon', password='1735', db='acdd', charset='utf8')
            print('>> DB Connected...')
            self.cur = self.conn.cursor()
        except:
            pass

    def get_host(self):
        return self.__HOST
    

