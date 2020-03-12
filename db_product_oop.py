from db_connect_oop import *

class NWProducts(MSDBConnection):
    def __init__(self):
        super().__init__()
        self.products_table = 'Products'
        self.employees_table = 'Employees'


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
        rows = self.__sql_query(f"INSERT INTO {self.employees_table} (EmployeeID, LastName, FirstName) VALUES ('SPG4757', 'Malungu', 'Camile De Jong.')").commit
        return rows
        # TIP : Search Commit For 'pyodbc'


    # U - Update (UPDATE)

    # D - Delete (DELETE)