def order_chai():
    print("what would you like to prfer  ")
    order = yield # he ask give me a value but when you doesnt he not print
    while True:
        print(f"hey the order is {order}")
        order = yield  # as same he asking valiue after the first yield and break the infinite loop 


total_order = order_chai()

next(total_order)

total_order.send("one ice cream")
total_order.send("butter scotch")