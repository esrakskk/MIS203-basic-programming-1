"""Week 7 project A: a small dictionary-based inventory application."""

def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Enter a whole number.")
            continue
        if value > 0:
            return value
        print("Enter a number above zero.")


def add_product(inventory):
    code = input("Code: ").strip().upper()
    if not code or code in inventory:
        print("Code is empty or already exists.")
        return
    
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    price = float(input("Unit price: "))
    stock = int(input("Opening stock: "))
    if price < 0 or stock < 0:
        print("Price and stock must be nonnegative.")
        return
    inventory[code] = {"name": name, "price": price, "stock": stock}
    print("Product added.")


def sell_product(inventory):
    code = input("Code to sell: ").strip().upper()
    
    if code not in inventory:
        print("Unknown product.")
        return
    
    quantity = read_positive_int("Quantity: ")
    product = inventory[code]
    if quantity > product["stock"]:
        print("Insufficient stock.")
        return
    product["stock"] -= quantity
    print(f"Sale: {quantity * product['price']:.2f} TRY")
    print(f"Remaining stock: {product['stock']}")


def restock(inventory):
    code = input("Code to restock: ").strip().upper()
    if code not in inventory:
        print("Unknown product.")
        return
    quantity = read_positive_int("Quantity received: ")
    inventory[code]["stock"] += quantity
    print("New stock:", inventory[code]["stock"])


def report(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    total_value = 0.0
    print(f"{'CODE':10} {'NAME':20} {'PRICE':>9} {'STOCK':>7}")
    for code, product in sorted(inventory.items()):
        print(f"{code:10} {product['name']:20} {product['price']:9.2f} {product['stock']:7d}")
        total_value += product["price"] * product["stock"]
    print(f"Inventory value: {total_value:.2f} TRY")


def main():
    inventory = {
        "P-101": {"name": "Notebook", "price": 75.0, "stock": 12},
        "P-102": {"name": "Pen", "price": 20.0, "stock": 30},
    }
    while True:
        command = input("add / sell / restock / report / quit: ").strip().lower()
        if command == "quit":
            break
        if command == "add":
            add_product(inventory)
        elif command == "sell":
            sell_product(inventory)
        elif command == "restock":
            restock(inventory)
        elif command == "report":
            report(inventory)
        else:
            print("Unknown command.")
    print("Session ended.")


if __name__ == "__main__":
    main()
