stock = {"P-101": 12, 
         "P-102": 0}

code = input("Product code: ").strip().upper()

if code in stock:
    print("Stock:", stock[code])
else:
    print("Unknown code")

