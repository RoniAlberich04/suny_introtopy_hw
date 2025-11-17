#Simple order

orders = []
choice = -1 

while choice != 0:
    print("1. Add order")
    print("2. View orders")
    print("0. EXIT")
    choice = int(input("SELECT > "))

    if choice == 1:
        print("====== ADD ORDER ======")
        descr = input("Description: ")
        price = float(input("Price: "))
        order = {'descr': descr, 'price': price}
        orders.append(order)
    elif choice == 2:
        print('======ORDERS======')
        if len(orders) > 0:
            for order in orders:
                print(order['descr'])
                print('Price:', orders['price'])
                print('----------------------------------------------')
        else:
            print('No orders yet')
    elif choice == 0:
        print("Bye!")
    else:
        print("Wrong choice")