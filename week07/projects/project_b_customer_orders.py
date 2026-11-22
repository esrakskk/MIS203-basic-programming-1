"""Week 7 project B: keep customer orders in nested dictionaries."""

def add_customer(customers):
    customer_id = input("Customer ID: ").strip().upper()
    if not customer_id or customer_id in customers:
        print("ID is empty or already exists.")
        return
    name = input("Customer name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    customers[customer_id] = {"name": name, "orders": []}
    print("Customer saved.")


def add_order(customers):
    customer_id = input("Customer ID: ").strip().upper()
    customer = customers.get(customer_id)
    if customer is None:
        print("Unknown customer.")
        return
    description = input("Order description: ").strip()
    try:
        amount = float(input("Order amount: "))
    except ValueError:
        print("Amount must be numeric.")
        return
    if not description or amount < 0:
        print("Description is required and amount must be nonnegative.")
        return
    order = {"description": description, "amount": amount}
    customer["orders"].append(order)
    print("Order saved.")


def customer_total(customer):
    total = 0.0
    for order in customer["orders"]:
        total += order["amount"]
    return total


def print_report(customers):
    print("=" * 58)
    print("CUSTOMER ORDER REPORT")
    print("=" * 58)
    grand_total = 0.0
    for customer_id, customer in sorted(customers.items()):
        total = customer_total(customer)
        grand_total += total
        print(f"{customer_id}: {customer['name']}")
        for order in customer["orders"]:
            print(f"   {order['description']:28} {order['amount']:9.2f} TRY")
        print(f"   Customer total: {total:.2f} TRY")
    print("-" * 58)
    print(f"Customers: {len(customers)}")
    print(f"Grand total: {grand_total:.2f} TRY")


def main():
    customers = {}
    print("Customer Order Register")
    while True:
        command = input("customer / order / report / quit: ").strip().lower()
        if command == "quit":
            break
        if command == "customer":
            add_customer(customers)
        elif command == "order":
            add_order(customers)
        elif command == "report":
            print_report(customers)
        else:
            print("Unknown command.")
    print_report(customers)


if __name__ == "__main__":
    main()
