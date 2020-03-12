from db_connect_oop import *

class NWProducts(MSDBConnection):
    def __init__(self):
        super().__init__()
        self.table = 'Products'


    def __sql_query(self, query):
        return self.cursor.execute(query)

    # Write All The CRUD Methods

    # R - Read One Product and Read ALL Products (SELECT)
    def all(self):
        # Return Data With All Products
        rows = self.__sql_query(f"SELECT * FROM {self.table}")
        return rows

    def __filter_sql_injections(self, query):

        # Do Some Regular Expression To Filter SQL Attacks
        # Return Clean Expressions (Like No DROP Or DELETE WHERE)
        pass

    # C - Create One Product (INSERT)
        # TIP : Search Commit For 'pyodbc'

    # D - Delete (DELETE)