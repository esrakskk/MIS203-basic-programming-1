categories = ["books", "food", "books", "office", "food", "books"]

counts = {}

for category in categories:
    counts[category] = counts.get(category, 0) + 1
    
for category, count in counts.items():
    print(category, count)
