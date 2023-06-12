import pymysql

class DataBase:
    def __init__(self, user_name, user_pwd, db_name):
        try:
            self.conn = pymysql.connect(self.get_host(), user=user_name, password=user_pwd, db=db_name, charset='utf8')
            print('>> DB Connected...')
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass