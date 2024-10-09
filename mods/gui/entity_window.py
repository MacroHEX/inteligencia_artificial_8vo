import tkinter as tk
from tkinter import messagebox, simpledialog
from mods.entities.service.entity_service import register_person, register_business, get_entities, remove_entity


def save_person(name, cedula, ruc, codigo_verificador, email, address, phone_number):
    try:
        register_person(name, cedula, ruc, codigo_verificador, email, address, phone_number)
        messagebox.showinfo("Success", f"Person '{name}' added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add person: {str(e)}")


def save_business(name, ruc, codigo_verificador, email, address, phone_number):
    try:
        register_business(name, ruc, codigo_verificador, email, address, phone_number)
        messagebox.showinfo("Success", f"Business '{name}' added successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add business: {str(e)}")


def delete_entity():
    entity_id = simpledialog.askstring("Input", "Enter the ID of the entity to delete:")
    try:
        remove_entity(int(entity_id))
        messagebox.showinfo("Success", f"Entity with ID {entity_id} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete entity: {str(e)}")


class EntityWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Manage Entities")
        self.root.geometry("500x500")

        # Create buttons for adding and managing entities
        self.add_person_button = tk.Button(self.root, text="Add Person", command=self.add_person)
        self.add_person_button.pack(pady=10)

        self.add_business_button = tk.Button(self.root, text="Add Business", command=self.add_business)
        self.add_business_button.pack(pady=10)

        self.view_all_button = tk.Button(self.root, text="View All Entities", command=self.view_all_entities)
        self.view_all_button.pack(pady=10)

    def add_person(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Person")
        add_window.geometry("300x300")

        # Entry fields for person details
        tk.Label(add_window, text="Name:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Cedula:").pack(pady=5)
        cedula_entry = tk.Entry(add_window)
        cedula_entry.pack()

        tk.Label(add_window, text="RUC (optional):").pack(pady=5)
        ruc_entry = tk.Entry(add_window)
        ruc_entry.pack()

        tk.Label(add_window, text="Codigo Verificador (optional):").pack(pady=5)
        verif_entry = tk.Entry(add_window)
        verif_entry.pack()

        tk.Label(add_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(add_window)
        email_entry.pack()

        tk.Label(add_window, text="Address:").pack(pady=5)
        address_entry = tk.Entry(add_window)
        address_entry.pack()

        tk.Label(add_window, text="Phone Number:").pack(pady=5)
        phone_entry = tk.Entry(add_window)
        phone_entry.pack()

        # Submit button
        submit_button = tk.Button(add_window, text="Submit",
                                  command=lambda: save_person(name_entry.get(), cedula_entry.get(),
                                                              ruc_entry.get(),
                                                              verif_entry.get(), email_entry.get(),
                                                              address_entry.get(), phone_entry.get()))
        submit_button.pack(pady=10)

    def add_business(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Business")
        add_window.geometry("300x300")

        tk.Label(add_window, text="Business Name:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="RUC:").pack(pady=5)
        ruc_entry = tk.Entry(add_window)
        ruc_entry.pack()

        tk.Label(add_window, text="Codigo Verificador:").pack(pady=5)
        verif_entry = tk.Entry(add_window)
        verif_entry.pack()

        tk.Label(add_window, text="Email:").pack(pady=5)
        email_entry = tk.Entry(add_window)
        email_entry.pack()

        tk.Label(add_window, text="Address:").pack(pady=5)
        address_entry = tk.Entry(add_window)
        address_entry.pack()

        tk.Label(add_window, text="Phone Number:").pack(pady=5)
        phone_entry = tk.Entry(add_window)
        phone_entry.pack()

        submit_button = tk.Button(add_window, text="Submit",
                                  command=lambda: save_business(name_entry.get(), ruc_entry.get(),
                                                                verif_entry.get(), email_entry.get(),
                                                                address_entry.get(), phone_entry.get()))
        submit_button.pack(pady=10)

    def view_all_entities(self):
        entities = get_entities()
        view_window = tk.Toplevel(self.root)
        view_window.title("All Entities")
        view_window.geometry("400x400")

        for entity in entities:
            tk.Label(view_window, text=str(entity)).pack()


def launch_entity_window():
    root = tk.Tk()
    app = EntityWindow(root)
    root.mainloop()
