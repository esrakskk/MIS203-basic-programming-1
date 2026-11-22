inventory = {
    "P-101": {"name": "Notebook", 
              "price": 75.0, 
              "stock": 12},
    
    "P-102": {"name": "Pen", 
              "price": 20.0, 
              "stock": 30},
            }

for code, item in inventory.items():
    print(f"{code}: {item['name']} ({item['stock']} units)")


for pair in inventory.items():
    code = pair[0]   # anahtar → "P-101"
    item = pair[1]   # değer   → {"name": "Notebook", ...}
    print(f"{code}: {item['name']} ({item['stock']} units)")


for pair in inventory.items():
    print(f"{pair[0]}: {pair[1]['name']} ({pair[1]['stock']} units)")
