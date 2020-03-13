from db_connect_oop import *

class NWProducts(MSDBConnection):
    def __init__(self):
        super().__init__()
        self.products_table = 'Products'


    def __sql_query(self, query):
        return self.cursor.execute(query)

    # Write All The CRUD Methods:

    # R - Read ALL Products (SELECT)
    def all_products(self):
        # Return Data With All Products
        data = self.__sql_query(f"SELECT * FROM {self.products_table}")
        return data

    # R - Read One Product
    def one_product(self):
        rows = self.__sql_query(f"SELECT * FROM {self.products_table}")
        return rows

    # C - Create One Product (INSERT)
    def create_one_product(self):
        values = input('Enter A Product Name.\n')
        rows = self.__sql_query(f"INSERT INTO {self.products_table} (ProductName) VALUES ('{values}')")
        self.conn.commit()
        return rows
        # TIP : Search Commit For 'pyodbc'

    # D - Delete (DELETE)
    def delete_one_product(self):
        user_input = input('Delete A Product Name.\n')
        rows = self.__sql_query(f"DELETE FROM {self.products_table} WHERE ProductName = '{user_input}'")
        self.conn.commit()
        return rows

    # U - Update (UPDATE)
    def update_one_product(self):
        new_name = input("Update The Product Name To A New Name \n")
        old_name = input("Update The Product Name To The Old Name \n")
        rows = self.__sql_query(f"UPDATE {self.products_table} SET ProductName = '{new_name}' WHERE ProductName = '{old_name}'")
        self.conn.commit()
        return rows
