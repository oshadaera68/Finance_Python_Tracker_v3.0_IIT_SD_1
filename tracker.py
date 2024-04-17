import tkinter as tk
from tkinter import ttk
import json


class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")

    def create_widgets(self):
        # Frame for table and scrollbar

        # Treeview for displaying transactions

        # Scrollbar for the Treeview

        # Search bar and button

        pass

    def load_transactions(self, filename):
        try:
            with open(filename, 'r') as file:
                json.load(file)
        except FileNotFoundError:
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
    root.mainloop()


if __name__ == "__main__":
    main()
