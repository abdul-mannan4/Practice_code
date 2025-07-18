def viewitems(inventory):
    for items in inventory:
        info,data=items
        name,category=info
        price,stock=data
        print(f"Name: {name} Category: {category} | Price: {price} Stock: {stock}")
    return


def addnew(inventory):
    itemname=input("Enter item Name: ")
    itemcategory=input("Enter item Category: ")
    itemprice=int(input("Enter th Price: "))
    itemstock=int(input("Enter the Stock: "))
    inventory.append(((itemname,itemcategory),[itemprice,itemstock]))
    print("Item Added Succesfully")
    return

def update(inventory):
    updatingitem=input("Enter the Item(name) whose Price/Stcok you want to add: ")
    choice=int(input('''Do you want to update Stock/Price?
                If Price,Press 1
                If Stock,press 2: '''))
    
    for items in inventory:
        info,data=items
        name,category=info
        if(updatingitem==name):
            if choice==1:
                newprice=int(input(f"Enter new Price of {name}: "))
                data[0]=newprice
                return
            elif choice ==2:
                newstock=int(input(f"Enter new Stock of {name}: "))
                data[1]=newstock
                return 
        

def search(inventory):
    choice=input("Enter(name) what You want to search: ")
    found=False
    for items in inventory:
        info,data=items
        name,category=info
        if choice==name:
            found=True
            print(f"Name: {name}\tCategory: {category}\n Price: {data[0]}\tStcok: {data[1]}")
            return
    if found==False:
        print("Nothing Found Based on Your Search")


def remove(inventory):
    choice=input("Enter(name) what You want to remove: ")
    found=False
    for items in inventory:
        info,data=items
        name,category=info
        if choice==name:
            found=True
            inventory.remove(items)
            print("Item Removed Successfully")
            return
    if found==False:
        print("Nothing Found Based on Your Search")




inventory = [
    (("Banana", "Fruit"), [100, 30]),
    (("Milk", "Dairy"), [200, 50])
]

print('''=====================================          
                Menu
=====================================
        1. View Items
        2. Add new Item
        3. Update Stock/Price
        4. Search Item
        5. Remove Items
        6. Exit
======================================''')
        
def menu():
    while True:
        choice=int(input("Enter Your Choice: "))

        if choice==1:
            viewitems(inventory)
        elif choice==2:
            addnew(inventory)
        elif choice==3:
            update(inventory)
        elif choice==4:
            search(inventory)
        elif choice==5:
            remove(inventory)
        elif choice==6:
            break
        else:
            print("Inalid Choice,Add a new number")
        


menu()
