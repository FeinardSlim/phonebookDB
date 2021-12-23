import time
import uuid
import warnings

import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': '34.68.0.204',
    'database': 'phonebookdb'
}

class PhoneBook:
    def __init__(self):
        self.conn = mysql.connector.connect(user='root',host='34.68.0.204',database='phonebook')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS `phonebook` ("
              "`id` varchar(50) NOT NULL,"
              "`nama` varchar(50) NOT NULL,"
              "`alamat` text NOT NULL,"
              "`notelp` varchar(50) NOT NULL,"
              "`created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,"
              "`updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
              "PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"
        )
        self.conn.commit()
        self.conn.close()

    def connections(self):
        self.conn = mysql.connector.connect(user='root', host='34.68.0.204', database='phonebook')
        self.cursor = self.conn.cursor()

    def query(self,query):
        self.connections()
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self,query):
        self.connections()
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()

    def list(self):
        try:
            query = "select * from phonebook"
            data = self.query(query)
            return dict(status='OK',data=data)
        except:
            return dict(status='ERR',msg='Error')

    def create(self,info):
        try:
            id = str(uuid.uuid1())
            # self.db[id] = info
            query = "insert into phonebook (id,nama,alamat,notelp) values ('%s','%s','%s','%s')"%(id,info['nama'],info['alamat'],info['notelp'],)
            print(query)
            self.commit(query)
            return dict(status='OK', id=id)
        except Exception as e:
            print(e)
            return dict(status='ERR',msg='Tidak bisa Create')

    def delete(self,id):
        try:
            query = "delete from phonebook where id = '%s'"%(id)
            self.commit(query)
            return dict(status='OK',msg='{} deleted' . format(id), id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Delete')

    def update(self,id,info):
        try:
            query = "update phonebook set nama = '%s', alamat = '%s', notelp = '%s' where id = '%s'"%(info['nama'],info['alamat'],info['notelp'],id,)
            self.commit(query)
            return dict(status='OK',msg='{} updated' . format(id), id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Update')
    def read(self,id):
        try:
            query = "select * from phonebook where id = '%s'"%(id,)
            data = self.query(query)
            return dict(status='OK',msg=data)
        except:
            return dict(status='ERR',msg='Tidak Ketemu')

    def measure(self):
        time_start = time.time()*1000.0
        try:
            query = "select * from phonebook"
            self.query(query)
            return dict(status='OK',msg=time.time()*1000.0 - time_start)
        except:
            return  dict(status='ERR',msg='Terdapat permaslaahan didalam query/perhitungan')

if __name__=='__main__':
    pd = PhoneBook()
# #    ----------- create
#     # result = pd.create(dict(nama='royyana',alamat='ketintang',notelp='6212345'))
#     # print(result)
#     # result = pd.create(dict(nama='ibrahim',alamat='ketintang',notelp='6212341'))
#     # print(result)
#     # result = pd.create(dict(nama='Ananda', alamat='Dinoyo Sekolahan', notelp='6212345'))
#     # print(result)
# #    ------------ list
#     print(pd.list())
# #    ------------ info
#     print(pd.read('204ee471-63cc-11ec-906f-c0b6f9cbf346'))
#
# #    ------------ Delete
#     print(pd.delete('204ee471-63cc-11ec-906f-c0b6f9cbf346'))
#
#     print(pd.list())
    print(pd.measure())


