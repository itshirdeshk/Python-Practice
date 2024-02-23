items = ["apple", "banana", "orange", "apple", "mango"]

# Method 1:
for item in items:
    if items.count(item) > 1:
        print(item)
        exit()

print("List is Unique")

# Method 2:
unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate:", item)
        break
    unique_items.add(item)