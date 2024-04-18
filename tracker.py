import json
import tkinter as tk
from tkinter import ttk


class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")

    def create_widgets(self):
        # frame
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # search bar, label and button
        self.label = ttk.Label(self.frame, text="Search:", font=('Arial', 18))
        self.label.grid(row=0, column=0, padx=23, pady=12)
        self.label.pack()

        self.search_text = tk.StringVar()
        self.text_box = ttk.Entry(self.frame, width=53, textvariable=self.search_text, font='Arial, 24')
        self.text_box.grid(row=0, column=1, pady=4)
        self.text_box.pack()

        self.search_button = ttk.Button(self.frame, text='Search', width=10, command=self.search_transactions,
                                        padding=10)
        self.search_button.grid(row=0, column=2, pady=15)
        self.search_button.pack()

        # scroll bar
        self.scroll_bar = ttk.Scrollbar(self.root)
        self.scroll_bar.pack(side='right')

        #table


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
    root.geometry('1285x725')
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
