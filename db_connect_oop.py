import pyodbc

class MSDBConnection():
    # We Need To Connect To Our DataBase.

    def __init__(self):
        self.database = 'Northwind'
        self.user_id = 'SA'
        self.password = 'Passw0rd2018'

        self.conn = pyodbc.connect('DSN=MYMSSQL;DATABASE='+ self.database +';UID='+ self.user_id +';PWD=' + self.password +'')

        self.cursor = self.conn.cursor()

    def sql_query(self, query):
        return self.cursor.execute(query)


nw_db_object = MSDBConnection()

nw_db_object.sql_query("SELECT * FROM Products")

print(nw_db_object)
print(nw_db_object)
