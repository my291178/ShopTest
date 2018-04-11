money = 0
sales = []

goods = [{

    "ID": 1,
    "Name": "concrete",
    "Price": 250,
    "Count": 100
},

    {
        "ID": 2,
        "Name": "steel",
        "Price": 1200,
        "Count": 2000
    },

    {
        "ID": 3,
        "Name": "blocks",
        "Price": 30,
        "Count": 2000
    }]

command_labels = ["Buy", "Print warehouse", "Print money", "Exit"]


def print_menu():
    # count = 1
    # for label in command_labels:
    #    print("%d. %s" % (count, label))
    #    count += 1

    for num, label in enumerate(command_labels, start=1):
        print("%d. %s" % (num, label))


def get_command():
    return int(input("Input command: "))


def is_in_interval(command):
    return 1 <= command <= len(command_labels)


def print_goods(goods):
    for i in goods:
        print("ID: %d Name: %s Price: %d Count: %d" % (i["ID"], i["Name"], i["Price"], i["Count"]))


def print_money():
    print_goods(sales)
    print("Current money %d" % money)


def print_warehouse():
    print_goods(goods)


def buy():
    global money
    global goods
    global sales
    print_warehouse()
    buy_id = int(input("Input goods id: "))
    is_in_goods = False
    good = None
    for i in goods:
        if i["ID"] == buy_id:
            is_in_goods = True
            good = i

    if is_in_goods == True:

        count = int(input("Input count: "))

        if good["Count"] >= count:
            good["Count"] -= count
            money += count * good["Price"]
            sales.append({
                "ID": good["ID"],
                "Name": good["Name"],
                "Price": good["Price"],
                "Count": count

            })
        else:
            print("Not enought in warehouse")

    else:
        print("Id doesn't exist")


command_funcs = [buy, print_warehouse, print_money, exit]

# print(list(enumerate(command_labels, start=1)))

while True:

    print_menu()

    # command = int(input("Input command: "))
    command = get_command()

    if is_in_interval(command):

        command_funcs[command - 1]()

    else:
        print("Wrong command!")
