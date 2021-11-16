from database import create_table, add_entry, get_entries, close_database, del_entry

create_table()
menu = """
Please select one of the following option:
1. Add new entry
2. View entries
3. Delete entries
4. Exit

Your selection: """


def prompt_new_entry():
    entry_id = input("Enter ID: ")
    entry_name = input("Enter name of what: ")
    entry_dateDelivery = input("Enter delivery date: ")
    entry_time = input("Enter delivery time: ")
    entry_paymentMode = input("Enter payment mode used: ")
    entry_contactNum = input("Enter contact number: ")
    add_entry(entry_id, entry_name, entry_dateDelivery, entry_time, entry_paymentMode, entry_contactNum)


def view_entries(entries):
    for entry in entries:
        print(f"-----------------------------")
        print(f"{entry[0]}\n{entry[1]}\n {entry[2]} - {entry[3]}\n {entry[4]}\n {entry[5]}")

def prompt_del_entry():
    id_for_deletion = input("Enter ID needed to be deleted: ")
    del_entry(id_for_deletion)


welcome = "Welcome to the Delivery Record App!"
print(welcome)
user_input = input(menu)

while user_input != "4":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    elif user_input =="3":
        prompt_del_entry()
    else:
        print("Invalid options, please try again")

    user_input = input(menu)

close_database()