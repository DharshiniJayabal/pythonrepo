list_items=[]
while True:
    item=input("enter an item for the list:")
    if item=='done':
        break
    list_items.append(item)
    string_item=input("enter a string item:")
    tuple_items=tuple(list_items)+(string_item,)
    print(tuple_items)
    