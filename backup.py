import os
item = [
    {"name": "ไข่เจียวหมูสับ", "price": 35},
    {"name": "ผัดกะเพราหมูสับ", "price": 40},
    {"name": "กระเพราหมูกรอบ", "price": 45},
    {"name": "ข้าวหมูแดง", "price": 45},
    {"name": "ข้าวขาหมู", "price": 45},
    {"name": "ผัดไทยกุ้งสด", "price": 50},
    {"name": "เย็นตาโฟ", "price": 50},
    {"name": "กุ้งอบวุ้นเส้น", "price": 40},
    {"name": "ข้าวผัดปู", "price": 60},
    {"name": "ข้าวแกงกะหรี่", "price": 60},
    {"name": "ราเม็งหมูตุ๋น", "price": 250},
]

Rice = [
    {"name": "ข้าวสวย", "price": 10},
    {"name": "ข้าวกล้อง", "price": 15},
    {"name": "ข้าวไรซ์เบอร์รี่", "price": 20},
    {"name": "ข้าวมัน", "price": 15},
    {"name": "ข้าวเหนียว", "price": 10},
    {"name": "ข้าวต้ม", "price": 10},
]

topping = [
    {"name": "ไก่ทอด", "price": 20},
    {"name": "ไก่ย่าง", "price": 20},
    {"name": "ไก่ทอดวิงซ์แซ่บ", "price": 30},
    {"name": "ไก่คาราเกะ", "price": 30},
    {"name": "ไข่เจียว", "price": 15},
    {"name":"ไข่ดาว","price": 10},
    {"name":"ไข่ตอก","price": 15},
    {"name":"ไข่ชะอม","price": 15},
    {"name":"ไข่ชะอม","price": 15},
    {"name":"ไข่เข็ม","price": 15},
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    error = ""
    while True:
        print(" Dawning Store\n")
        print(" 1.shop\n 2.edit menu\n 0.exit\n")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            select = int(input("Select your work : "))
            clear_screen()
            return select
        except ValueError:
            error = "// The input must be a number !! //\n"
            clear_screen()
            continue


def edit():
    error = ""
    while True:
        clear_screen()
        print(" Edit")
        print("1.edit menu\n2.edit custom menu\n0.exit edit menu")
        try:
            if len(error) > 0:
                print(error)
                error = ""
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
            error = "\n// The input must be a number !! //"
            clear_screen()
            continue


def edit_menu():
    error = ""
    while True:
        clear_screen()
        print(" List of menu")
        for i, items in enumerate(item, start=1):
            print(f"{i}. {items['name']}: {items['price']} baht")

        print("\n Edit Menu:")
        print(" 1. Add Item")
        print(" 2. Remove Item")
        print(" 3. Update Item")
        print(" 0. Return to Main Menu")

        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nSelect your option : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
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
    global topping
    clear_screen()
    print(" Add Item\n")
    while True:
        name = input("Enter item name : ")
        if name.isnumeric():
            print("// Error: The name must be character //")
        else:
            break
    while True:
        try:
            price = int(input("Enter item price : "))
            break
        except ValueError:
            print("// Error: The price must be a number //")
    if e == 1:
        item.append({"name": name, "price": price})
    elif e == 2:
        Rice.append({"name": name, "price": price})
    elif e == 3:
        topping.append({"name": name, "price": price})


def remove_item():
    global item
    error = ""
    while True:
        clear_screen()
        print(" Remove Item\n")
        for i, items in enumerate(item, start=1):
            print(f" {i}. {items['name']}: {items['price']} baht")
        print("\ntype '0' for exit Remove Item")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nEnter the number of the item to remove : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
            continue
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(item):
            item.pop(index)


def remove_rice():
    global Rice
    error = ""
    while True:
        clear_screen()
        print(" Remove\n")
        for i, item in enumerate(Rice, start=1):
            print(f" {i}. {item['name']}: {item['price']} baht")
        print("\ntype '0' for exit Remove Rice")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nEnter the number of the item to remove : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
            continue
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(Rice):
            Rice.pop(index)


def remove_topping():
    global topping
    error = ""
    while True:
        clear_screen()
        print(" Remove\n")
        for i, item in enumerate(topping, start=1):
            print(f" {i}. {item['name']}: {item['price']} baht")
        print("\ntype '0' for exit remove topping")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nEnter the number of the item to remove : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
            continue
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(topping):
            topping.pop(index)


def update_item():
    global item
    while True:
        clear_screen()
        print(" Update Item\n")
        for i, items in enumerate(item, start=1):
            print(f"{i}. {items['name']}: {items['price']} baht")
        print("\ntype '0' for exist Update Item")
        n = int(input("\nEnter the number of the item to update : "))
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(item):
            while True:
                name = input("Enter new item name : ")
                if name.isnumeric():
                    print("// Error: The name must be character !! //")
                else:
                    break
            while True:
                try:
                    price = int(input("Enter new item price : "))
                    break
                except ValueError:
                    print("// Error: The price must be a number //")
            item[index] = {"name": name, "price": price}


def update_rice():
    global Rice
    while True:
        clear_screen()
        print(" Update Rice\n")
        for i, item in enumerate(Rice, start=1):
            print(f"{i}. {item['name']}: {item['price']} baht")
        print("\ntype '0' for exist Update Rice")
        try:
            n = int(input("\nEnter the number of the rice to update : "))
        except ValueError:
            continue
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(Rice):
            while True:
                name = input("Enter new rice name : ")
                if name.isnumeric():
                    print("// Error: The name must be character !! //")
                else:
                    break
            while True:
                try:
                    price = int(input("Enter new rice price : "))
                    break
                except ValueError:
                    print("// Error: The price must be a number //")
            Rice[index] = {"name": name, "price": price}


def update_topping():
    global topping
    while True:
        clear_screen()
        print(" Update topping\n")
        for i, item in enumerate(topping, start=1):
            print(f"{i}. {item['name']}: {item['price']} baht")
        print("\ntype '0' for exist Update topping")
        n = int(input("\nEnter the number of the topping to update : "))
        index = n-1
        if n == 0:
            break
        if 0 <= index < len(topping):
            while True:
                name = input("Enter new topping name : ")
                if name.isnumeric():
                    print("// Error: The name must be character //")
                else:
                    break
            while True:
                try:
                    price = int(input("Enter new topping price : "))
                    break
                except ValueError:
                    print("// Error: The price must be a number //")
            topping[index] = {"name": name, "price": price}


def edit_custom_menu():
    error = ""
    while True:
        clear_screen()
        print("Edit custom menu")
        print("\n1. Rice\n2. Topping\n0. Exit")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nSelect your work : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
            clear_screen()
            continue
        if n == 1:
            edit_rice_menu()
            continue

        if n == 2:
            edit_topping_menu()
            continue

        if n == 0:
            break


def edit_rice_menu():
    error = ""
    while True:
        clear_screen()
        print(" List of rice")
        for i, items in enumerate(Rice, start=1):
            print(f"{i}. {items['name']}: {items['price']} baht")

        print("\n Edit Menu:")
        print(" 1. Add Item")
        print(" 2. Remove Item")
        print(" 3. Update Item")
        print(" 0. Exit")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nSelect your option : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
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


def edit_topping_menu():
    error = ""
    while True:
        clear_screen()
        print(" List of topping")
        for i, item in enumerate(topping, start=1):
            print(f"{i}. {item['name']}: {item['price']} baht")

        print("\n Edit Menu:")
        print(" 1. Add Item")
        print(" 2. Remove Item")
        print(" 3. Update Item")
        print(" 0. Exit")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nSelect your option : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
            continue

        if n == 0:
            break

        if n == 1:
            add_item(3)
            continue

        if n == 2:
            remove_topping()
            continue

        if n == 3:
            update_topping()
            continue


def shop():
    total_price = 0
    cart = []
    error = ""
    while True:
        clear_screen()
        print(" Dawning Store \n")
        for i, items in enumerate(item, start=1):
            print(f" {i}.{items['name']}: {items['price']} baht")
            i += 1
        print("\nType '77' for custom menu")
        print("Type '88' for view or edit your cart")
        print(f"All price you need to pay {total_price} Baht")
        print("Type '99' for pay")
        print("\nType '0' for exist shop to main menu\n")

        try:
            if len(error) > 0:
                print(error)
                error = ""
            select_menu = int(input("Select number of menu : "))
        except ValueError:
            error = "// The input must be a number !! //\n"
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

        index = select_menu - 1
        if 0 <= index < len(item):
            total_price += item[select_menu-1]["price"]
            cart.append(
                {"name": item[select_menu-1]['name'], "price": item[select_menu-1]['price']})
            clear_screen()
            continue
    return


def custom(cart, total_price):
    sim_cart = cart.copy()
    sim_total_price = total_price
    box = {"first": "", "last": "", "name": "", "price": 0}
    clear_screen()
    exit = -1
    error = ""
    while True:
        clear_screen()
        print(" Custom Menu\n")
        print("Select Rice")
        for i, items in enumerate(Rice, start=1):
            print(f"{i}. {items['name']}: {items['price']} baht")

        print("\nType 0 for exit custom menu")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nSelect your rice : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
            continue
        exit = n
        if exit == 0:
            break
        index = n-1
        if 0 <= index < len(Rice):
            box["first"] = Rice[index]["name"]
            box["price"] += Rice[index]["price"]
            break
        else:
            error = f"\n// Error: {n} isn't in list of rice !! //"
            continue

    while True:
        if exit == 0:
            break
        clear_screen()
        print(" Custom Menu\n")
        print("Select your topping")
        for i, item in enumerate(topping, start=1):
            print(f"{i}. {item['name']}: {item['price']} baht")

        print("\nType 0 for exit custom menu")
        try:
            if len(error) > 0:
                print(error)
                error = ""
            n = int(input("\nSelect your topping of rice : "))
        except ValueError:
            error = "\n// The input must be a number !! //"
            continue
        exit = n
        if exit == 0:
            break
        index = n-1
        if 0 <= index < len(topping):
            box["last"] = topping[index]["name"]
            box["price"] += topping[index]["price"]
            break
        else:
            error = f"\n// Error: {n} isn't in list of topping rice !! //"
            continue

    box['name'] = box['first'] + " + " + box['last']
    sim_cart.append({"name": box['name'], "price": box['price']})
    sim_total_price += box['price']
    return sim_cart, sim_total_price


def view_cart(cart, total_price):
    sim_cart = cart.copy()
    sim_total_price = total_price
    error = ""
    while True:
        try:
            clear_screen()
            print(" list of item in your cart\n")
            for i, items in enumerate(sim_cart, start=1):
                print(f" {i}.{items['name']}: {items['price']} baht")

            print(f"\nAll price you need to pay {sim_total_price} Baht\n")
            print("if you want to delete item in your cart")
            print("type 'd' followed by the number of the item, such as 'd1' ")
            print("type '0' for return to menu\n ")

            if len(error) > 0:
                print(error)
                error = ""
            n = input("Select your work : ")
            try:
                if n[0] == "d" or n[0] == "D" and n[1:].isdigit() and int(n[1:]) > 0:
                    index = int(n[1:]) - 1
                    sim_total_price -= sim_cart[index]['price']
                    sim_cart.pop(index)
                    continue
            except IndexError:
                error = f"// Error: {int(n[1:])} isn't in list of cart !! //\n"
                continue
            if n == "0":
                clear_screen()
                break
        except ValueError:
            error = "// The input must be a number !! //\n"
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

    NameWidth = 18
    print("\n", "-"*16, "Receipt", "-"*16, "\n")
    print(f"{"Amount": <8}{"Goods": <20}{"Price": >10}\n")
    for item in count_list_of_item_and_price:
        space = NameWidth - len(item['name'])
        if len(item['name']) > NameWidth:
            parts = item['name'].split('+')
            print(f"{item['count']: <8}{parts[0].strip(
            )}+{'': <{space + len(parts[0].strip())}}{item['price']: >13} Baht")
            print(f"{'': <{8}}{parts[1].strip()}")
        else:
            print(f"{item['count']: <8}{item['name']}{
                  '': <{space}}{item['price']: >10} Baht")

    print(f"\n Net amount {total_count} item {tp} Baht\n")
    print("-"*41)
    press = input("\nNext order press an Enter ... ")
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
