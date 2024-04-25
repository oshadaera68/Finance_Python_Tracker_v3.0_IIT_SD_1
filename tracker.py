import json
import tkinter as tk
from tkinter import ttk


# transaction class
class Transactions:
    def __init__(self, trans_type, amount, date):
        self.trans_type = trans_type
        self.amount = amount
        self.date = date


# initial class
class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker - v3.0")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")
        self.original_transactions = self.transactions[:]  # Make a copy for original data

    # creating widgets
    def create_widgets(self):
        # frame
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # search bar, label and button
        self.label = ttk.Label(self.frame, text="Search:", font=('Arial', 19))
        self.label.grid(row=0, column=0, padx=24, pady=12)  # place the absolute position in the widget

        self.search_text = tk.StringVar()  # create the variable in the string value in search feature
        self.text_box = ttk.Entry(self.frame, width=45, textvariable=self.search_text, font='Arial, 20')
        self.text_box.grid(row=0, column=1, pady=2)

        self.search_button = ttk.Button(self.frame, text='Search', width=14, padding=5,
                                        command=self.search_transactions)  # clicking search event
        self.search_button.grid(row=0, column=2, padx=13, pady=15, sticky='e')

        # scroll bar
        self.scrollbar = ttk.Scrollbar(self.frame, orient='vertical')
        self.scrollbar.grid(row=1, column=10, sticky='ns')

        # table
        self.table = ttk.Treeview(self.frame, columns=('Index', 'Transaction', 'Date', 'Amount'), height=15,
                                  show='headings', yscrollcommand=self.scrollbar.set)

        # table headings
        self.table.heading('Index', text='Index')
        self.table.heading('Transaction', text='Transaction')
        self.table.heading('Date', text='Date')
        self.table.heading('Amount', text='Amount')

        # table columns
        self.table.column('Index', width=100)
        self.table.column('Transaction', width=320)
        self.table.column('Date', width=320)
        self.table.column('Amount', width=320)

        # Bind sorting function to column headers
        self.table.heading('Index', command=lambda: self.sort_by_column('Index', False))
        self.table.heading('Transaction', command=lambda: self.sort_by_column('Transaction', False))
        self.table.heading('Date', command=lambda: self.sort_by_column('Date', False))
        self.table.heading('Amount', command=lambda: self.sort_by_column('Amount', False))

        # table locations
        self.table.grid(row=1, column=0, columnspan=4, padx=11, pady=11)
        self.scrollbar.config(command=self.table.yview)

    # search feature
    def search_transactions(self):
        search_query = self.search_text.get().lower()
        # find the data in the transactions in search feature (using transaction type)
        searched_transactions = [trans for trans in self.original_transactions if
                                 search_query in trans.trans_type.lower()]
        # data showing the table in searched value
        self.display_transactions(searched_transactions)

    # column sorting feature
    def sort_by_column(self, col, reverse):
        # set the data in the table for sorting
        table_data = [(self.table.set(child, col), child) for child in self.table.get_children('')]

        # Print table_data for before sorting
        print("Before sorting:", table_data)

        # Sort the data based on the values in the specified column
        table_data.sort(reverse=reverse)

        # Print table_data for after sorting
        print("After sorting:", table_data)

        # Rearrange the rows in the table based on the sorted data
        for index, (_, child) in enumerate(table_data):
            self.table.move(child, '', index)

        # Update the heading to toggle sorting order
        self.table.heading(col, command=lambda: self.sort_by_column(col, not reverse))

    # load transactions
    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                print("Data:", data)
                print("Type of data:", type(data))  # Add this line for debugging
                transactions = []
                if isinstance(data, list):  # Check if data is a list
                    return transactions  # Return empty transactions list
                # load all transactions for converting the list
                for trans_type, trans_list in data.items():
                    for item in trans_list:
                        trans = Transactions(trans_type, item['amount'], item['date'])
                        transactions.append(trans)
                return transactions
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # display transactions on the table
    def display_transactions(self, transactions):
        # Remove existing entries
        for items in self.table.get_children():
            self.table.delete(items)

        for x, trans in enumerate(transactions, start=1):
            # using attributes for the access the object values for loading table
            transaction_type = trans.trans_type
            amount = trans.amount
            date = trans.date
            # inserting the loaded data in the table
            self.table.insert("", "end", values=(x, transaction_type, date, amount))

        def add_transactions_window():
            # sub window initializing
            extra = tk.Toplevel()
            extra.title('Add Transactions')
            extra.geometry('350x190')
            extra.resizable(False, False)

            category_label = ttk.Label(extra, text="Category:", font=('Arial', 12))
            category_label.grid(row=0, column=0, padx=7, pady=4)

            category_text = tk.StringVar()
            category_text_box = ttk.Entry(extra, width=20, textvariable=category_text, font='Arial, 14')
            category_text_box.grid(row=0, column=2, pady=2)

            date_label = ttk.Label(extra, text="Date:", font=('Arial', 12))
            date_label.grid(row=1, column=0, padx=7, pady=4)

            date_text = tk.StringVar()
            date_text_box = ttk.Entry(extra, width=20, textvariable=date_text, font='Arial, 14')
            date_text_box.grid(row=1, column=2, pady=2)

            amount_label = ttk.Label(extra, text="Amount:", font=('Arial', 12))
            amount_label.grid(row=2, column=0, padx=7, pady=4)

            amount_text = tk.StringVar()
            amount_text_box = ttk.Entry(extra, width=20, textvariable=amount_text, font='Arial, 14')
            amount_text_box.grid(row=2, column=2, pady=2)

            def add_transactions():
                # save_transactions()
                trans_type = category_text_box.get()
                trans_date = date_text_box.get()
                trans_amount = amount_text_box.get()

            def cancel_window():
                pass

            ok_button = ttk.Button(extra, text='OK', width=10, padding=3, command=add_transactions)
            ok_button.grid(row=3, column=0, padx=12, pady=11, sticky='w')

            cancel_button = ttk.Button(extra, text='Cancel', width=10, padding=3, command=cancel_window)
            cancel_button.grid(row=3, column=2, padx=12, pady=11, sticky='w')

            # delete transactions

        def delete_transactions():
            # save_transactions()
            pass

        add_button = ttk.Button(self.frame, text='Add Transaction', width=15, padding=7,
                                command=add_transactions_window)
        add_button.grid(row=2, column=1, padx=12, pady=11, sticky='w')

        delete_button = ttk.Button(self.frame, text='Delete Transaction', width=16, padding=7,
                                   command=delete_transactions)
        delete_button.grid(row=2, column=1, padx=12, pady=11, sticky='e')
        # delete transactions





# main runnable function
def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.geometry('1110x470')
    root.resizable(False, False)
    root.mainloop()


# main runnable constructor
if __name__ == "__main__":
    main()
