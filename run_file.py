from db_product_oop import *

products_tb = NWProducts()

while True:

    print("Select 1 For All Products")

    user_input = input(">>>")

    if user_input == '1':

        data = products_tb.read_all()
        # Get ALL Our Product Using Our New Method
        # ITERATE And Display Them Nicely
        print(data)

        while True:

            records = data.fetchone()
            if records is None:
                break
                print(records)