import json
import tkinter as tk
from tkinter import ttk


class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker - v3.0")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")

    def create_widgets(self):
        # frame
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # search bar, label and button
        self.label = ttk.Label(self.frame, text="Search:", font=('Arial', 18))
        self.label.grid(row=0, column=0, padx=27, pady=12)

        self.search_text = tk.StringVar()
        self.text_box = ttk.Entry(self.frame, width=45, textvariable=self.search_text, font='Arial, 24')
        self.text_box.grid(row=0, column=1, pady=4)

        self.search_button = ttk.Button(self.frame, text='Search', width=15, padding=5,
                                        command=self.search_transactions)
        self.search_button.grid(row=0, column=2, padx=13, pady=15, sticky='e')

        # scroll bar
        self.scrollbar = ttk.Scrollbar(self.frame, orient='vertical')
        self.scrollbar.grid(row=1, column=10, sticky='ns')

        # table
        self.table = ttk.Treeview(self.frame, columns=('Index', 'Date', 'Transaction', 'Amount'), height=15,
                                  show='headings', yscrollcommand=self.scrollbar.set)
        self.table.heading('Index', text='Index')
        self.table.heading('Transaction', text='Transaction')
        self.table.heading('Date', text='Date')
        self.table.heading('Amount', text='Amount')

        self.table.column('Index', width=100)
        self.table.column('Transaction', width=320)
        self.table.column('Date', width=320)
        self.table.column('Amount', width=320)

        self.table.grid(row=1, column=0, columnspan=4, padx=11, pady=11)
        self.scrollbar.config(command=self.table.yview)

    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as file:
                transactions = json.load(file)
                return transactions
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def display_transactions(self, transactions):
        # Remove existing entries

        # Add transactions to the treeview
        pass

    def search_transactions(self):
        # Placeholder for search functionality
        pass

    def sort_by_column(self, col, reverse):
        # Placeholder for sorting functionality
        pass


def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.geometry('1110x448')
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
