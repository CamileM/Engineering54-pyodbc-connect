from db_product_oop import *

products_tb = NWProducts()

employees_tb = NWProducts()

while True:

    print('')
    print(10 * '=', "SWITCH - BOARD", 10 * '=')
    print("Select 1 For 'All' Products")
    print("Select 2 For 'One' Product")
    print("Select 3 To Create 'One' Product")
    print(14 * '=', "BORDER", 14 * '=')

    user_input = input('')

    if user_input == '1':

        data = products_tb.all_products()
        # Get ALL Our Product Using Our New Method
        # ITERATE And Display Them Nicely
        for items in data:
            print(items)

    elif user_input == '2':

        data = products_tb.one_product()
        print(data.fetchone())

    elif user_input == '3':

        data = employees_tb.create_one_product()
        print(data.fetchone())

        while True:

            records = data.fetchone()
            if records is None:
                print(records.fetchone)
                break
