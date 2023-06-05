import pymysql


class DataTransferObject:
    def __init__(self):
        self.db_connection()

    def db_connection(self):
        self.conn = pymysql.connect(host='192.168.50.248', user='jeawon', password='1735', db='acdd', charset='utf8')
        print('>> DB Connected...')
        self.cur = self.conn.cursor()
