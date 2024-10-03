import tkinter as tk
from tkinter import messagebox, simpledialog

from mods.invoices.service.item_service import add_invoice_item, get_items_for_invoice, remove_invoice_item


class ItemWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Invoice Items")
        self.root.geometry("500x500")

        # Buttons for managing items
        self.add_item_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_item_button.pack(pady=10)

        self.view_items_button = tk.Button(self.root, text="View All Items for Invoice",
                                           command=self.view_items_for_invoice)
        self.view_items_button.pack(pady=10)

    def add_item(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Item")
        add_window.geometry("300x300")

        # Entry fields for item details
        tk.Label(add_window, text="Invoice ID:").pack(pady=5)
        invoice_id_entry = tk.Entry(add_window)
        invoice_id_entry.pack()

        tk.Label(add_window, text="Description:").pack(pady=5)
        description_entry = tk.Entry(add_window)
        description_entry.pack()

        tk.Label(add_window, text="Quantity:").pack(pady=5)
        quantity_entry = tk.Entry(add_window)
        quantity_entry.pack()

        tk.Label(add_window, text="Unit Price:").pack(pady=5)
        price_entry = tk.Entry(add_window)
        price_entry.pack()

        submit_button = tk.Button(add_window, text="Submit",
                                  command=lambda: self.save_item(invoice_id_entry.get(), description_entry.get(),
                                                                 quantity_entry.get(), price_entry.get()))
        submit_button.pack(pady=10)

    def save_item(self, invoice_id, description, quantity, unit_price):
        try:
            add_invoice_item(invoice_id, description, float(quantity), float(unit_price))
            messagebox.showinfo("Success", f"Item '{description}' added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add item: {str(e)}")

    def view_items_for_invoice(self):
        invoice_id = simpledialog.askstring("Input", "Enter the Invoice ID:")
        items = get_items_for_invoice(invoice_id)
        view_window = tk.Toplevel(self.root)
        view_window.title("Invoice Items")
        view_window.geometry("400x400")

        for item in items:
            tk.Label(view_window, text=str(item)).pack()

    def delete_item(self):
        item_id = simpledialog.askstring("Input", "Enter the ID of the item to delete:")
        try:
            remove_invoice_item(int(item_id))
            messagebox.showinfo("Success", f"Item with ID {item_id} deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete item: {str(e)}")


def launch_item_window():
    root = tk.Tk()
    app = ItemWindow(root)
    root.mainloop()
