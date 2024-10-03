import tkinter as tk
from tkinter import messagebox, simpledialog

from mods.invoice_items.service.invoice_service import issue_invoice, get_invoices, remove_invoice


class InvoiceWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Invoices")
        self.root.geometry("500x500")

        # Buttons for managing invoices
        self.add_invoice_button = tk.Button(self.root, text="Add Invoice", command=self.add_invoice)
        self.add_invoice_button.pack(pady=10)

        self.view_invoices_button = tk.Button(self.root, text="View All Invoices", command=self.view_all_invoices)
        self.view_invoices_button.pack(pady=10)

    def add_invoice(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Invoice")
        add_window.geometry("300x300")

        # Entry fields for invoice details
        tk.Label(add_window, text="Issuer ID:").pack(pady=5)
        issuer_entry = tk.Entry(add_window)
        issuer_entry.pack()

        tk.Label(add_window, text="Recipient ID:").pack(pady=5)
        recipient_entry = tk.Entry(add_window)
        recipient_entry.pack()

        tk.Label(add_window, text="Timbrado:").pack(pady=5)
        timbrado_entry = tk.Entry(add_window)
        timbrado_entry.pack()

        tk.Label(add_window, text="Invoice Number:").pack(pady=5)
        invoice_number_entry = tk.Entry(add_window)
        invoice_number_entry.pack()

        tk.Label(add_window, text="Issue Date:").pack(pady=5)
        issue_date_entry = tk.Entry(add_window)
        issue_date_entry.pack()

        tk.Label(add_window, text="Currency:").pack(pady=5)
        currency_entry = tk.Entry(add_window)
        currency_entry.pack()

        tk.Label(add_window, text="IVA 10%:").pack(pady=5)
        iva_entry = tk.Entry(add_window)
        iva_entry.pack()

        submit_button = tk.Button(add_window, text="Submit",
                                  command=lambda: self.save_invoice(issuer_entry.get(), recipient_entry.get(),
                                                                    timbrado_entry.get(), invoice_number_entry.get(),
                                                                    issue_date_entry.get(), currency_entry.get(),
                                                                    iva_entry.get()))
        submit_button.pack(pady=10)

    def save_invoice(self, issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10):
        try:
            issue_invoice(issuer_id, recipient_id, timbrado, invoice_number, issue_date, currency, iva_10, iva_10)
            messagebox.showinfo("Success", f"Invoice '{invoice_number}' added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add invoice: {str(e)}")

    def view_all_invoices(self):
        invoices = get_invoices()
        view_window = tk.Toplevel(self.root)
        view_window.title("All Invoices")
        view_window.geometry("400x400")

        for invoice in invoices:
            tk.Label(view_window, text=str(invoice)).pack()

    def delete_invoice(self):
        invoice_id = simpledialog.askstring("Input", "Enter the ID of the invoice to delete:")
        try:
            remove_invoice(int(invoice_id))
            messagebox.showinfo("Success", f"Invoice with ID {invoice_id} deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete invoice: {str(e)}")


def launch_invoice_window():
    root = tk.Tk()
    app = InvoiceWindow(root)
    root.mainloop()
