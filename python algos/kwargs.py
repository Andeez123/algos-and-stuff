print("Hello word")


#args
def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza")
    print(toppings)
    print(details)

order_pizza("large", "cheese", "pepperoni", delivery=True, tip=5)
# * packs cheese and pepperoni into a tuple named toppings