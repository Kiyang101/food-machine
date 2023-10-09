import os
item = [
    {"name": "ไข่เจียวหมูสับ", "price": 35},
    {"name": "ผัดกะเพราหมูสับ", "price": 40},
    {"name": "กระเพราหมูกรอบ", "price": 45},
    {"name": "ผัดไทยกุ้งสด", "price": 50},
    {"name": "เย็นตาโฟ", "price": 50},
    {"name": "NameOfItem_6", "price": 60},
    {"name": "NameOfItem_7", "price": 70},
]

Rice = [
    {"name": "ข้าวสวย", "price": 10},
    {"name": "ข้าวกล้อง", "price": 15},
    {"name": "ข้าวไรซ์เบอร์รี่", "price": 20},
    {"name": "ข้าวมัน", "price": 15},
    {"name": "ข้าวเหนียว", "price": 10},
]

Face = [
    {"name":"ไก่ทอด","price": 10},
    {"name":"ไก่ย่าง","price": 10},
    {"name":"ไก่ทอดวิงซ์แซ่บ","price": 10},
    {"name":"ไก่ทอด_4","price": 10},
    {"name":"ไก่ทอด_5","price": 10},
]

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def menu():
    while True:
        print(" Dawning Store\n")
        print(" 1.shop\n 2.edit menu\n 0.exist\n")
        try:
            select = int(input("Select your work : "))
            clear_screen()
            return select
        except ValueError:
            clear_screen()
            continue

def edit():
    while True:
        clear_screen()
        print(" Edit")
        print("1.edit menu\n2.edit custom menu\n0.exit edit menu")
        try:
            n = int(input("\nSelect your work : "))
            if n == 1:
                edit_menu()
                continue
            if n == 2:
                edit_custom_menu()
                continue
            if n == 0:
                break
        except ValueError:
            clear_screen()
            continue

def edit_menu():
    while True:
        clear_screen()
        print(" List of menu")
        for i, item_dict in enumerate(item, start=1):
            print(f"{i}. {item_dict['name']} : {item_dict['price']} baht")
        
        print("\n Edit Menu:")
        print(" 1. Add Item")
        print(" 2. Remove Item")
        print(" 3. Update Item")
        print(" 0. Return to Main Menu")
        
        try:
            n = int(input("\nSelect your option : "))
        except ValueError:
            continue
        
        if n == 1:
            add_item(1)
            continue
        
        if n == 2:
            remove_item()
            continue
        
        if n == 3:
            update_item()
            continue
        
        if n == 0:
            break

def add_item(e):
    global item 
    global Rice
    global Face
    clear_screen()
    print(" Add Item\n")
    name = input("Enter item name : ")
    while True:
        try:
            price = int(input("Enter item price : "))
            break
        except ValueError:
            print("Error: you price must be number")
    if e == 1:
        item.append({"name": name, "price": price})
    elif e == 2:
        Rice.append({"name": name, "price": price})
    elif e == 3:
        Face.append({"name": name, "price": price})

def remove_item():
    global item 
    while True:
        clear_screen()
        print(" Remove Item\n")
        for i, item_dict in enumerate(item, start=1):
            print(f" {i}. {item_dict['name']} : {item_dict['price']} baht")
        print("\ntype '0' for exit Remove Item")
        try:
            n = int(input("\nEnter the number of the item to remove : "))
        except ValueError:
            continue
        index = n-1
        if n == 0:
            break 
        if 0 <= index < len(item):
            item.pop(index)
   
def remove_rice():
    global Rice
    while True:
        clear_screen()
        print(" Remove\n")
        for i, item in enumerate(Rice, start=1):
            print(f" {i}. {item['name']} : {item['price']} baht")
        print("\ntype '0' for exit Remove Rice")
        try:
            n = int(input("\nEnter the number of the item to remove : "))
        except ValueError:
            continue
        index = n-1
        if n == 0:
            break 
        if 0 <= index < len(Rice):
            Rice.pop(index)

def remove_face():
    global Face
    while True:
        clear_screen()
        print(" Remove\n")
        for i, item in enumerate(Face, start=1):
            print(f" {i}. {item['name']} : {item['price']} baht")
        print("\ntype '0' for exit Remove Face")
        try:
            n = int(input("\nEnter the number of the item to remove : "))
        except ValueError:
            continue
        index = n-1
        if n == 0:
            break 
        if 0 <= index < len(Face):
            Face.pop(index)
   
def update_item():
    global item
    while True:
        clear_screen()
        print(" Update Item\n")
        for i, item_dict in enumerate(item, start=1):
            print(f"{i}. {item_dict['name']} : {item_dict['price']} baht")
        print("\ntype '0' for exist Update Item")
        n = int(input("\nEnter the number of the item to update : "))
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(item):
            name = input("Enter new item name : ")
            while True:
                try:
                    price = int(input("Enter new item price : "))
                    break
                except ValueError:
                    print("Error: you price must be number")
            item[index] = {"name": name, "price": price}
            
def update_rice():
    global Rice
    while True:
        clear_screen()
        print(" Update Rice\n")
        for i, item in enumerate(Rice, start=1):
            print(f"{i}. {item['name']} : {item['price']} baht")
        print("\ntype '0' for exist Update Rice")
        try:
            n = int(input("\nEnter the number of the rice to update : "))
        except ValueError:
            continue
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(Rice):
            name = input("Enter new rice name : ")
            while True:
                try:
                    price = int(input("Enter new rice price : "))
                    break
                except ValueError:
                    print("Error: you price must be number")
            Rice[index] = {"name": name, "price": price}
            
def update_face():
    global Face
    while True:
        clear_screen()
        print(" Update Face\n")
        for i, item in enumerate(Face, start=1):
            print(f"{i}. {item['name']} : {item['price']} baht")
        print("\ntype '0' for exist Update Face")
        n = int(input("\nEnter the number of the face to update : "))
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(Face):
            name = input("Enter new face name : ")
            while True:
                try:
                    price = int(input("Enter new face price : "))
                    break
                except ValueError:
                    print("Error: you price must be number")
            Face[index] = {"name": name, "price": price}
        
def edit_custom_menu():
    while True:
        clear_screen()
        print("Edit custom menu")
        print("\n1. Rice\n2. Face\n0. Exit")
        try:
            n = int(input("\nSelect your work : "))
        except ValueError:
            clear_screen()
            continue
        if n == 1:
            while True:
                clear_screen()
                print(" List of rice")
                for i, item_dict in enumerate(Rice, start=1):
                    print(f"{i}. {item_dict['name']} : {item_dict['price']} baht")
                
                print("\n Edit Menu:")
                print(" 1. Add Item")
                print(" 2. Remove Item")
                print(" 3. Update Item")
                print(" 0. Exit")
                try:
                    n = int(input("\nSelect your option : "))
                except ValueError:
                    continue
                    
                if n == 0:
                    break
                    
                if n == 1:
                    add_item(2)
                    continue
                    
                if n == 2:
                    remove_rice()
                    continue
                    
                if n == 3:
                    update_rice()
                    continue
            continue
            
        if n == 2:
            while True:
                clear_screen()
                print(" List of face")
                for i, item in enumerate(Face, start=1):
                    print(f"{i}. {item['name']} : {item['price']} baht")
                
                print("\n Edit Menu:")
                print(" 1. Add Item")
                print(" 2. Remove Item")
                print(" 3. Update Item")
                print(" 0. Exit")
                try:
                    n = int(input("\nSelect your option : "))
                except ValueError:
                    continue
                    
                if n == 0:
                    break
                    
                if n == 1:
                    add_item(3)
                    continue
                    
                if n == 2:
                    remove_face()
                    continue
                    
                if n == 3:
                    update_face()
                    continue
            continue
        if n == 0:
            break
        
def shop():
    total_price = 0
    cart = []
    while True:
        clear_screen()
        print(" Dawning Store \n")
        for i, item_dict in enumerate(item, start=1):
            print(f" {i}.{item_dict['name']} : {item_dict['price']} baht")
            i += 1
        print("\nType '77' for custom menu")
        print("Type '88' for view or edit your cart")
        print(f"All price you need to pay {total_price } Baht")
        print("type '99' for pay")
        print("\ntype '0' for exist shop to main menu\n")

        try:
            select_menu = int(input("Select number of menu : "))
        except ValueError:
            clear_screen()
            continue

        if select_menu == 0:
            clear_screen()
            break

        if select_menu == 88:
            cart, total_price = view_cart(cart, total_price)
            continue
        
        if select_menu == 77:
            cart, total_price = custom(cart, total_price)
            continue
        
        if select_menu == 99:
            cart, total_price = payment(cart, total_price)
            break
        
        index = select_menu -1
        if 0 <= index < len(item):
            total_price += item[select_menu-1]["price"]
            cart.append({"name": item[select_menu-1]['name'], "price": item[select_menu-1]['price']})
            clear_screen()
            continue
    return

def custom(cart, total_price):
    sim_cart = cart.copy()
    sim_total_price = total_price
    box = {"first":"", "last":"" , "name":"", "price":0}
    clear_screen()
    exit = -1
    while True:
        clear_screen()
        print(" Custom Menu\n")
        print("Select Rice")
        for i, item_dict in enumerate(Rice, start=1):
            print(f"{i}. {item_dict['name']} : {item_dict['price']} baht")
            
        print("\nType 0 for exit custom menu")
        try:
            n = int(input("\nSelect your rice : "))
            exit = n
            if exit == 0:
                break
            index = n-1
            if 0 <= index < len(Rice):
                box["first"] = Rice[index]["name"]
                box["price"] += Rice[index]["price"]
                break
            else:
                continue
        except ValueError:
            continue
            
    while True:
        if exit == 0:
            break
        clear_screen()
        print(" Custom Menu\n")
        print("Select ...")
        for i, item_dict in enumerate(Face, start=1):
            print(f"{i}. {item_dict['name']} : {item_dict['price']} baht")

        print("\nType 0 for exit custom menu")
        try:
            n = int(input("\nSelect your face of rice : "))
            exit = n
            if exit == 0:
                break
            index = n-1
            if 0 <= index < len(Face):
                box["last"] = Face[index]["name"]
                box["price"] += Face[index]["price"]
                break
            else:
                continue
        except ValueError:
            continue    
    
    box['name'] = box['first'] + " + " + box['last']
    sim_cart.append({"name":box['name'], "price":box['price']})
    sim_total_price += box['price']
    return sim_cart, sim_total_price
        
def view_cart(cart, total_price):
    sim_cart = cart.copy()
    sim_total_price = total_price
    while True:
        try:
            clear_screen()
            print(" list of item in your cart\n")
            for i, item_dict in enumerate(sim_cart, start=1):
                print(f" {i}.{item_dict['name']} : {item_dict['price']} baht")

            print(f"\nAll price you need to pay {sim_total_price} Baht\n")
            print("if you want to delete item in your cart")
            print("type 'd' followed by the number of the item, such as 'd1' ")
            print("type '0' for retuen to menu\n ")
            
            n = input("Select your work : ")
            try:
                if n[0] == "d" and n[1:].isdigit() and int(n[1:]) > 0:
                    index = int(n[1:]) - 1
                    sim_total_price -= sim_cart[index]['price']
                    sim_cart.pop(index)
                    continue
            except IndexError:
                continue
            if n == "0":
                clear_screen()
                break
        except ValueError:
            clear_screen()
            continue
        
    return sim_cart, sim_total_price

def payment(cart, total_price):
    clear_screen()
    count_item = {}
    count_price = {}
    total_count = 0
    tp = 0
    for data in cart:
        name = data["name"]
        price = data["price"]
        
        count_price[name] = price
        
        if name in count_item:
            count_item[name] += 1
        else:
            count_item[name] = 1
        tp += price
        total_count += 1  
        
    count_list_of_item_and_price = []
    for string, count in count_item.items():
        count_list_of_item_and_price.append({
            "name": string,
            "count": count,
            "price": count_price.get(string, 0) 
        })

    print(" list of all items\n")
    for item in count_list_of_item_and_price:
        print(f"{item['count']}   {item['name']}   {item['price']} Baht")
    
    print(f"\nNet amount {total_count} item    {tp} Baht")
    
    n = input("\nnext order press an Enter ... ")
    
    return [], 0

def main():
    while True:
        clear_screen()
        select = menu()
        if select == 1:
            shop()
            continue
        if select == 2:
            edit()
            continue
        if select == 0:
            break

if __name__ == "__main__":
    clear_screen()
    main()
