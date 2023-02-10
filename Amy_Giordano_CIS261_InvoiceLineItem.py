def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            return price
        except ValueError:
            print("Invalid price. Please enter a valid number.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid quantity. Please enter a valid integer.")

total = 0
while True:
    price = get_price()
    quantity = get_quantity()
    line_total = price * quantity
    total += line_total
    print("Price: $%.2f\tQuantity: %d\tLine Total: $%.2f" % (price, quantity, line_total))
    another = input("Do you want to enter another line item? (y/n)").lower()
    if another == "n":
        break

print("Total: $%.2f" % total)

