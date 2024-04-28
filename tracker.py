# finance tracker v2.0: using dictionaries + json
# importing json module
import json
import tkinter as tk
from tkinter import ttk

# initialize the empty directory
transactions = {}


# file handling
# load the file
def load_transactions():
    global transactions
    try:
        with open("trans.json", "r") as file:
            json.load(file)
    except FileNotFoundError:
        print("No transactions. Please try again")
    except json.decoder.JSONDecodeError:
        transactions = {}


# save the transactions into file
def save_transactions():
    # write the data in the json file
    with open("trans.json", "w") as file:
        json.dump(transactions, file)
        file.write('\n')


# date validation
def date_validation(date_text):
    try:
        year, month, day = map(int, date_text.split('-'))  # Split the date string and convert parts to integers
        if month < 1 or month > 12 or day < 1 or day > 31:
            return False  # Invalid month or day
        # Check for months with 30 days
        if month in [4, 6, 9, 11] and day > 30:
            return False
        # Check for February
        if month == 2:
            if day > 29:
                return False  # February cannot have more than 29 days
            if day == 29 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                return False  # Not a leap year
        return True
    except ValueError:
        return False


# read bulk lines
def read_bulk_transactions_from_file(file_name):
    file_name = file_name + ".txt"
    try:
        # open the file
        with open(file_name, 'r') as file:
            for line in file:  # iterate the line by line in the txt file
                lines = line.split()  # splitting the all lines in the txt file

                # same logic of add transaction
                add = {"amount": lines[1], "date": lines[2]}
                if lines[0] in transactions:
                    transactions[lines[0]].append(add)
                else:
                    transactions[lines[0]] = [add]
            save_transactions()
    except FileNotFoundError:
        print(f"{file_name} is Not found.")


# Feature implementations
def add_transaction():
    print("---------------------------------")
    print("|\t\t Add Transaction \t\t|")
    print("---------------------------------")
    # inputting data with validation
    while True:
        insert_type = input("Enter the type: ")
        if not insert_type:
            print("Please input the type..")
            continue
        else:
            insert_amount = int(input("Enter the amount: "))
            if insert_amount <= 0:
                print("Enter the valid amount. Don't type the negative amount.")
                continue
            else:
                insert_date = input("Enter the date: ")
                if not date_validation(insert_date):
                    print("Invalid date format. Please enter valid date in YYYY-MM-DD format.")
                    continue
                break

    # adding the transactions
    add = {"amount": insert_amount, "date": insert_date}

    # check the adding transactions for in the transactions dictionary
    if insert_type in transactions:
        transactions[insert_type].append(add)  # If you added new transaction, it works
    else:
        transactions[insert_type] = [add]  # same type, adding the new value
    save_transactions()

    enter_choice = input("Transaction Added. Do you want to add the another Transaction? [Y/N]: ")
    if enter_choice == "y" or enter_choice == "Y":
        add_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


# viewing all data
def view_transactions():
    print("---------------------------------")
    print("|\t\t View Transactions \t\t|")
    print("---------------------------------")

    for key_value, pair_value in transactions.items():  # iterating all items in transaction dictionary
        print(f"{key_value}:")  # print the all key values
        for index, transaction in enumerate(pair_value, 1):  # enumerating the all pair values and value
            print(f"\t{index}. {transaction['amount']} {transaction['date']}")  # print the formatted data


# update the data
def update_transaction():
    print("-------------------------------------")
    print("|\t\t Update Transactions \t\t|")
    print("-------------------------------------")

    # Showing All Transactions
    print("All Transactions List")

    for key_value, pair_value in transactions.items():  # iterating all items in transaction dictionary
        print(f"{key_value:}")  # print the all key values
        for x, transaction in enumerate(pair_value, 1):  # enumerating the all pair values and value
            print(f"\t{x}. Amount: {transaction['amount']} Date: {transaction['date']}")  # print the formatted data

    # input the wanted type
    update_type = input("Enter the Type: ")
    # check the update type in the transactions dict
    if update_type in transactions.keys() and len(transactions[update_type]) > 0:
        index_number = int(input("Ënter the index number: ")) - 1
        # Check if index_number is within the valid range of indices for transactions[update_type]
        if 0 <= index_number < len(transactions[update_type]):
            print("\nwhat do you want to the update?")
            print("1. Amount")
            print("2. Date")
            print("3. Cancel Update")
            choice = input("Enter the choice to update: ")

            # updating process
            while True:
                if choice == "1":
                    while True:
                        try:
                            # print the current value in the amount
                            print(f"current amount: {transactions[update_type][0]['amount']}")
                            amount = int(input("Enter the new Amount: "))
                            if amount < 0:
                                print("Amount must be a positive integer.")
                            else:
                                break
                        except ValueError:
                            print("Invalid Number. Please type the valid number")

                    # new value updating to current value
                    transactions[update_type][0]['amount'] = amount
                    break

                elif choice == "2":
                    print(f"current amount: {transactions[update_type][0]['date']}")
                    date = input("Enter the new date (YYYY-MM-DD): ")
                    if not date_validation(date):
                        print("Invalid date format. Please enter valid date in YYYY-MM-DD format.")
                    else:
                        transactions[update_type][0]['date'] = date
                        break

                # cancelling updates
                elif choice == "3":
                    print("Update is canceled.")
                    main_menu()
                    break
                else:
                    print("Invalid Choice. Try Again.")
                    main_menu()
                    break
        else:
            print("You typed invalid index. Type the valid index number.")
    else:
        print("Not any Keys in this dictionary. Please add the key and try to update.")
        main_menu()

    save_transactions()

    enter_choice = input("Transaction Updated. Do you want to update the another Transaction? [Y/N]: ")
    if enter_choice == "y" or enter_choice == "Y":
        update_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


# delete function
def delete_transaction():
    print("-------------------------------------")
    print("|\t\t Delete Transactions \t\t|")
    print("-------------------------------------")

    # print all transactions list
    print("All Transactions List")
    for key_value, pair_value in transactions.items():  # iterating all items in transaction dictionary
        print(f"{key_value:}")  # print the all key values
        for index, transaction in enumerate(pair_value, 1):  # enumerating the all pair values and value
            # print the formatted data
            print(f"\t{index}. Amount: {transaction['amount']} Date: {transaction['date']}")

    delete_type = input("Enter the type for delete: ")
    if delete_type in transactions.keys():  # check the if exists the user inputted type in the transaction dict.
        del transactions[delete_type]  # delete the type of the dictionary.
    save_transactions()

    enter_choice = input("Transaction Removed. Do you want to delete the another Transaction? [Y/N]: ")
    if enter_choice == "y" or enter_choice == "Y":
        delete_transaction()
    elif enter_choice == "n" or enter_choice == "N":
        main_menu()
    else:
        print("Invalid Value. Please Try Again!!")


# showing all total expenses
def display_summary():
    print("---------------------------------")
    print("|\t\t Display Summary \t\t|")
    print("---------------------------------")
    total_exp = 0
    for keys, pairs in transactions.items():  # iterating all items
        print("-----------------------------")
        print(f"|\t\t\t {keys} \t\t\t|")
        print("-----------------------------")
        total_cate = 0
        for trans in pairs:  # iterating all items in transaction dictionary
            net_amount = trans.get('amount', 0)  # Get the amount, default to 0 if not found
            print(f"Net Expense: {net_amount}")
            total_cate += net_amount  # Add amount to category total
        print(f"Total Expense for {keys}: {total_cate}")
        total_exp += total_cate  # Add category total to overall total
        print()
    print("Total Expense for all categories:", total_exp)  # showing the total calculation of expenses


# sorting and searching function
def search_sort_UI():
    class Transactions:
        def __init__(self, trans_type, amount, date):
            self.trans_type = trans_type
            self.amount = amount
            self.date = date

    # initial class

    def load_transaction(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                transactions = []
                # load all transactions for converting the list
                for trans_type, trans_list in data.items():
                    for item in trans_list:
                        trans = Transactions(trans_type, item['amount'], item['date'])
                        transactions.append(trans)
                return transactions
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    class FinanceTrackerGUI:
        def __init__(self, root):
            self.root = root
            self.root.title("Personal Finance Tracker - v3.0")
            self.create_widgets()
            self.transactions = load_transaction("trans.json")

        # creating widgets
        def create_widgets(self):
            # frame
            self.frame = ttk.Frame(self.root)
            self.frame.pack(fill="both", expand=True)

            # search bar, label and button
            self.label = ttk.Label(self.frame, text="Search:", font=('Arial', 19))
            self.label = ttk.Label(self.frame, text="Search:", font=('Arial', 19))
            self.label.grid(row=0, column=0, padx=27, pady=12)  # place the absolute position in the widget

            self.search_text = tk.StringVar()  # create the variable in the string value in search feature
            self.text_box = ttk.Entry(self.frame, width=45, textvariable=self.search_text, font='Arial, 20')
            self.text_box.grid(row=0, column=1, pady=4)

            self.search_button = ttk.Button(self.frame, text='Search', width=14, padding=5,
                                            command=self.search_transactions)  # clicking search event
            self.search_button.grid(row=0, column=2, padx=13, pady=15, sticky='e')

            # scroll bar
            self.scrollbar = ttk.Scrollbar(self.frame, orient='vertical')
            self.scrollbar.grid(row=1, column=10, sticky='ns')

            # table
            self.table = ttk.Treeview(self.frame, columns=('Index', 'Date', 'Transaction', 'Amount'), height=15,
                                      show='headings', yscrollcommand=self.scrollbar.set)

            # table headings
            self.table.heading('Index', text='Index', anchor='center')
            self.table.heading('Transaction', text='Transaction', anchor='center')
            self.table.heading('Date', text='Date', anchor='center')
            self.table.heading('Amount', text='Amount', anchor='center')

            # table columns
            self.table.column('Index', width=100, anchor='center')
            self.table.column('Transaction', width=320, anchor='center')
            self.table.column('Date', width=320, anchor='center')
            self.table.column('Amount', width=320, anchor='center')

            self.table.grid(row=1, column=0, columnspan=4, padx=11, pady=11)
            self.scrollbar.config(command=self.table.yview)

            # table binding click events
            self.table.heading('Index', command=lambda: self.sort_by_column('Index', False))
            self.table.heading('Transaction', command=lambda: self.sort_by_column('Transaction', False))
            self.table.heading('Date', command=lambda: self.sort_by_column('Date', False))
            self.table.heading('Amount', command=lambda: self.sort_by_column('Amount', False))

        # display transactions on the table
        def display_transactions(self, transactions):
            # Remove existing entries
            for items in self.table.get_children():
                self.table.delete(items)

            # Add transactions to the treeview
            for x, trans in enumerate(transactions, start=1):
                # using attributes for the access the object values for loading table
                transaction_type = trans.trans_type
                amount = trans.amount
                date = trans.date
                # inserting the loaded data in the table
                self.table.insert("", "end", values=(x, date, transaction_type, amount))

        # search feature
        def search_transactions(self):
            search_query = self.search_text.get().lower()
            # find the data in the transactions in search feature

            for item in self.table.get_children():
                self.table.delete(item)

            searched_transactions = [trans for trans in self.transactions if search_query in trans.trans_type.lower()]
            # data showing the table in searched value
            self.display_transactions(searched_transactions)

        # column sorting feature
        def sort_by_column(self, col, reverse):
            # get the data into the table
            table_data = [(self.table.set(child, col), child) for child in self.table.get_children('')]

            # Sort the data based on the values in the specified column
            table_data.sort(reverse=reverse)

            # Rearrange the rows in the table based on the sorted data
            for index, (_, child) in enumerate(table_data):
                self.table.move(child, '', index)

            # Update the heading to toggle sorting order
            self.table.heading(col, command=lambda: self.sort_by_column(col, not reverse))

    # main runnable function
    def main():
        root = tk.Tk()
        app = FinanceTrackerGUI(root)
        app.display_transactions(app.transactions)
        root.geometry('1110x448')
        root.resizable(False, False)
        root.mainloop()

    # main runnable constructor
    if __name__ == "__main__":
        main()


def main_menu():
    # load all transactions in the json file
    load_transactions()
    while True:
        print("-----------------------------------------")
        print("|\t\t Personal Finance Tracker \t\t|")
        print("-----------------------------------------")
        print("1. Add Transaction")
        print("2. View Transaction")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Read Bulk Transactions")
        print("7. Search, Sort UI")
        print("8. Exit")
        choice = input("Enter your choice: ")

        # main menu choices
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            file = input("Input File Name: ")
            read_bulk_transactions_from_file(file)
        elif choice == '7':
            search_sort_UI()
        elif choice == '8':
            exit_the_program()
        else:
            print("Invalid choice. Please try again.")


# exiting program
def exit_the_program():
    exit_choice = input("Did you want to exit the System? [Y/N]: ")
    if exit_choice == "y" or exit_choice == "Y":
        print("Program Exited")
        exit()
    elif exit_choice == "n" or exit_choice == "N":
        main_menu()
    else:
        print("Invalid Input.")
        exit(0)


# runnable main constructor
if __name__ == "__main__":
    main_menu()
