a = input("enter the elements:")

dup_items = set()
for x in a:
    if x not in dup_items:
        dup_items.add(x)

print(dup_items)
