import pyodbc

# Setup Variables
server = 'localhost,1433'
database = 'Northwind'
user_id = 'SA'
password = 'Passw0rd2018'

# Make The Connection
conn = pyodbc.connect('DSN=MYMSSQL;DATABASE=Northwind;UID=SA;PWD=Passw0rd2018')

# Creating A 'cursor object' From A Connection
    # Imagine Like A Real Cursor On Your Azure Data Studio
    # This Will Maintain State
crsr = conn.cursor()

# Running SQL Quaries using '.execute()'
crsr.execute("SELECT * FROM Customers")
# Using The 'fetchall()' - It Is DANGEROUS Because You Can Crash The Server Due To A High Amount Of Data
all_rows = crsr.fetchall()
print(all_rows)
print(type(all_rows))

counter = 0
for item in all_rows:
    print(counter, item.ContactName, '-', 'Fax:', item.Fax)
    counter += 1

# Best Practices Is To Use A 'while loop' And 'fetchone()' Until Your Entry Is None.
rows = crsr.execute("SELECT * FROM CUSTOMERS")

while True:

        record = rows.fetchone()
        if record is None:
            break
        print(record.ContactName)

rows = crsr.execute("SELECT * FROM PRODUCTS")

new_values = []

while True:

    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice * 200)
    new_values.append(record.UnitPrice * 200)

# row = crsr.fetchone() # Chooses An Entry In The Cursor
# print(row)
#
# row = crsr.fetchone() # Then Gets The Next Entry In The Cursor
# print(row)
#
# print(row.CompanyName)
# print(row.ContactName)
# print(row.Fax)
#
# print(type(crsr))
# print(type(row))