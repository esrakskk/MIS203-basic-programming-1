stock = {"P-101": 12, 
         "P-102": 30}

code = "P-101"
sold = 3

if code in stock and sold <= stock[code]:
    stock[code] -= sold
    print("Remaining:", stock[code])
else:
    print("Sale rejected")
