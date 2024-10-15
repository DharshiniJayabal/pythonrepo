tuple_items=("apple","banana","cherry")
list_items=list(tuple_items)
while True:
    item=input("enter an item to append to the list:")
    if item=='done':
        break
    list_items.append(item)
    updated_tuple=tuple(list_items)
    print(updated_tuple)