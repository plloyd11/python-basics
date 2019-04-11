shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter "DONE" to stop adding items.
Enter "HELP for this help.
Enter "SHOW" to show current list of items.
""")


def add_to_list(item):
    shopping_list.append(item)
    print(item, "was added to the list.", "There are currently {} item(s) in your cart.".format(len(shopping_list)))


def show_list():
    for item in shopping_list:
        print("* ", item)


show_help()

while True:
    new_item = input("> ")
    # break stops the loop / continue keeps going with the current iteration
    if new_item == "DONE":
        print(shopping_list)
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    else:
        add_to_list(new_item)