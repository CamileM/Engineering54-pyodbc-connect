from db_product_oop import *

products_tb = NWProducts()

while True:

    print('')
    print(10 * '=', "SWITCH - BOARD", 10 * '=')
    print("Select 1 For 'All' Products")
    print("Select 2 For 'One' Product")
    print("Select 3 To Create 'One' Product")
    print("Select 4 To Delete From A Database")
    print("Select 5 To Update A Database")



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

        data = products_tb.create_one_product()

    elif user_input == '4':

        data = products_tb.delete_one_product()


    elif user_input == '5':

        data = products_tb.update_one_product()

    else:
        print('')
        print("ERROR!!! ABORT!!! ERROR!!! ABORT!!! ERROR!!! ABORT!!! ERROR!!!")
        print('')
        print("TRY AGAIN!!! ONLY CHOOSE NUMBERS FROM [1 - 5].")


        # while True:
        #
        #     records = data.fetchone()
        #     if records is None:
        #         print(records.fetchone)
        #         break
