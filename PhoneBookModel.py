import uuid
import mysql.connector

config = dict()
config = {
    'user': 'root',
    'password': 'root',
    'host': '34.68.0.204',
    'database': 'phonebookdb'
}

class PhoneBook:
    def __init__(self):
        self.conn = mysql.connector.connect(config)
        self.cursor = self.conn.cursor()
        self.namafile = 'phonebook.db'
        self.cursor.execute(
            " CREATE TABLE IF NOT EXISTS `phonebook` ("
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

    def commit(self,query):
        self.cursor.execute(query)
        return self.conn.commit()

    def list(self):
        data = []
        try:
            query = "select * from phonebook"
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            # for i in self.db.keys():
            #     data.append(dict(id=i,data=self.db[i]))
            return dict(status='OK',data=data)
        except:
            return dict(status='ERR',msg='Error')

    def create(self,info):
        try:
            id = str(uuid.uuid1())
            # self.db[id] = info
            query = "insert into phonebook (id,nama,alamat,notelp) values (%s,%s,%s,%s)",(id,info['nama'],info['alamat'],info['notelp'],)
            if self.commit(query):
                return dict(status='OK',id=id)
            else:
                raise ValueError('query gagal')
        except:
            return dict(status='ERR',msg='Tidak bisa Create')

    def delete(self,id):
        try:
            query = "delete from phonebook where id = %s",(id)
            if self.commit(query):
                return dict(status='OK',msg='{} deleted' . format(id), id=id)
            else:
                raise ValueError('query gagal')
        except:
            return dict(status='ERR',msg='Tidak bisa Delete')

    def update(self,id,info):
        try:
            query = 'update phonebook set nama = %s, alamat = %s, notelp = %s where id = %s',(info['nama'],info['alamat'],info['notelp'],id,)
            if self.commit(query):
                return dict(status='OK',msg='{} updated' . format(id), id=id)
            else:
                raise ValueError("query gagal")
        except:
            return dict(status='ERR',msg='Tidak bisa Update')
    def read(self,id):
        try:
            query = "select * from phonebook where id = %s",(id,)
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            return dict(status='OK',msg=data)
        except:
            return dict(status='ERR',msg='Tidak Ketemu')

if __name__=='__main__':
    pd = PhoneBook()
#    ----------- create
#    result = pd.create(dict(nama='royyana',alamat='ketintang',notelp='6212345'))
#    print(result)
#    result = pd.create(dict(nama='ibrahim',alamat='ketintang',notelp='6212341'))
#    print(result)
#    result = pd.create(dict(nama='Ananda', alamat='Dinoyo Sekolahan', notelp='6212345'))
#    print(result)
#    ------------ list
    print(pd.list())
#    ------------ info
#    print(pd.read('c516b780-2fa2-11eb-bf35-7fc0bd24c845'))



