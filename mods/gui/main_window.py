import tkinter as tk
from tkinter import messagebox
from mods.entities.service.entity_service import register_person, register_business


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice App")
        self.root.geometry("400x300")

        # Create buttons for actions
        self.add_person_button = tk.Button(self.root, text="Add Person", command=self.add_person)
        self.add_person_button.pack(pady=10)

        self.add_business_button = tk.Button(self.root, text="Add Business", command=self.add_business)
        self.add_business_button.pack(pady=10)

    def add_person(self):
        # Window to add a new person
        add_person_window = tk.Toplevel(self.root)
        add_person_window.title("Add Person")
        add_person_window.geometry("300x300")

        # Entry fields for person details
        tk.Label(add_person_window, text="Name:").pack(pady=5)
        name_entry = tk.Entry(add_person_window)
        name_entry.pack()

        tk.Label(add_person_window, text="Cedula:").pack(pady=5)
        cedula_entry = tk.Entry(add_person_window)
        cedula_entry.pack()

        tk.Label(add_person_window, text="RUC (optional):").pack(pady=5)
        ruc_entry = tk.Entry(add_person_window)
        ruc_entry.pack()

        tk.Label(add_person_window, text="Codigo Verificador (optional):").pack(pady=5)
        verif_entry = tk.Entry(add_person_window)
        verif_entry.pack()

        tk.Label(add_person_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(add_person_window)
        email_entry.pack()

        tk.Label(add_person_window, text="Address:").pack(pady=5)
        address_entry = tk.Entry(add_person_window)
        address_entry.pack()

        tk.Label(add_person_window, text="Phone Number:").pack(pady=5)
        phone_entry = tk.Entry(add_person_window)
        phone_entry.pack()

        # Submit button
        submit_button = tk.Button(add_person_window, text="Submit",
                                  command=lambda: self.save_person(name_entry.get(), cedula_entry.get(),
                                                                   ruc_entry.get(), verif_entry.get(),
                                                                   email_entry.get(), address_entry.get(),
                                                                   phone_entry.get()))
        submit_button.pack(pady=10)

    def add_business(self):
        # Window to add a new business
        add_business_window = tk.Toplevel(self.root)
        add_business_window.title("Add Business")
        add_business_window.geometry("300x200")

        # Entry fields for business details
        tk.Label(add_business_window, text="Business Name:").pack(pady=5)
        name_entry = tk.Entry(add_business_window)
        name_entry.pack()

        tk.Label(add_business_window, text="RUC:").pack(pady=5)
        ruc_entry = tk.Entry(add_business_window)
        ruc_entry.pack()

        tk.Label(add_business_window, text="Codigo Verificador:").pack(pady=5)
        verif_entry = tk.Entry(add_business_window)
        verif_entry.pack()

        tk.Label(add_business_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(add_business_window)
        email_entry.pack()

        tk.Label(add_business_window, text="Address:").pack(pady=5)
        address_entry = tk.Entry(add_business_window)
        address_entry.pack()

        tk.Label(add_business_window, text="Phone Number:").pack(pady=5)
        phone_entry = tk.Entry(add_business_window)
        phone_entry.pack()

        # Submit button
        submit_button = tk.Button(add_business_window, text="Submit",
                                  command=lambda: self.save_business(name_entry.get(), ruc_entry.get(),
                                                                     verif_entry.get(), email_entry.get(),
                                                                     address_entry.get(), phone_entry.get()))
        submit_button.pack(pady=10)

    def save_person(self, name, cedula, ruc, codigo_verificador, email, address, phone_number):
        # Register the person using the service layer
        try:
            register_person(name, cedula, ruc, codigo_verificador, email, address, phone_number)
            messagebox.showinfo("Success", f"Person '{name}' added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add person: {str(e)}")

    def save_business(self, name, ruc, codigo_verificador, email, address, phone_number):
        # Register the business using the service layer
        try:
            register_business(name, ruc, codigo_verificador, email, address, phone_number)
            messagebox.showinfo("Success", f"Business '{name}' added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add business: {str(e)}")


def launch_gui():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
