import json
import tkinter as tk
from tkinter import ttk


# transaction class
class Transactions:
    def __init__(self, trans_type, amount, date):
        self.trans_type = trans_type
        self.amount = amount
        self.date = date


# load the file
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


# initial class
class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker - v3.0")
        self.root.geometry('1110x448')
        self.root.resizable(False, False)
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
        self.scrollbar.config(command=self.table.yview)  # scroll bar configuration

        # table binding events
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
            # using attributes for the access the object values in transaction class for loading table
            transaction_type = trans.trans_type
            amount = trans.amount
            date = trans.date
            # inserting the loaded data in the table
            self.table.insert("", "end", values=(x, date, transaction_type, amount))

    # search feature
    def search_transactions(self):
        # get the value thw user entered
        search_query = self.search_text.get().lower()

        # Remove existing entries
        for item in self.table.get_children():
            self.table.delete(item)

        # filter the data in typed value in thw entry box
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
    root.mainloop()


# main runnable constructor
if __name__ == "__main__":
    main()
