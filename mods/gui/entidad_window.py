import tkinter as tk
from tkinter import messagebox, ttk

from mods.entidad.service.entidad_service import EntidadService


class EntidadWindow:
    def __init__(self, root, entidad_service: EntidadService):
        self.root = root
        self.root.title("Administrar Entidades")
        self.service = entidad_service  # Use the service, not the connection

        # Create the main frame
        self.frame = tk.Frame(self.root, bg="lightgray")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Frame for Search functionality, aligned to the left
        search_frame = tk.Frame(self.frame, bg="lightgray")
        search_frame.grid(row=0, column=0, columnspan=2, sticky="w")

        # Label and Entry for searching by ID
        self.search_label = tk.Label(search_frame, text="Buscar Entidad por ID:", bg="lightgray", font=("Arial", 12))
        self.search_label.pack(side="left", padx=(0, 10), pady=5)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.pack(side="left", padx=(0, 10), pady=5)
        self.search_button = tk.Button(search_frame, text="Buscar", command=self.search_entidad, font=("Arial", 12), bg="#5cb85c", fg="white")
        self.search_button.pack(side="left", pady=5)

        # Treeview for displaying entidades as a table
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Tipo", "RUC", "Dirección", "Teléfono", "Email", "Cédula"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("RUC", text="RUC")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Cédula", text="Cédula")

        # Adding uniform width to columns for better presentation
        for col in ("ID", "Nombre", "Tipo", "RUC", "Dirección", "Teléfono", "Email", "Cédula"):
            self.tree.column(col, width=100)

        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Button frame to hold action buttons
        button_frame = tk.Frame(self.frame, bg="lightgray")
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Add Button
        self.add_button = tk.Button(button_frame, text="Agregar Entidad", command=self.open_add_window, font=("Arial", 12), bg="#0275d8", fg="white")
        self.add_button.pack(side="left", padx=10)

        # Update Button
        self.update_button = tk.Button(button_frame, text="Actualizar Seleccionado", command=self.open_update_window, font=("Arial", 12), bg="#f0ad4e", fg="white")
        self.update_button.pack(side="left", padx=10)

        # Delete Button
        self.delete_button = tk.Button(button_frame, text="Borrar Seleccionado", command=self.delete_selected_entidad, font=("Arial", 12), bg="#d9534f", fg="white")
        self.delete_button.pack(side="left", padx=10)

        # Load all entidades into the treeview
        self.load_all_entidades()

    def search_entidad(self):
        """Search for an entity by ID and display its details."""
        entidad_id_med = self.search_entry.get()
        if not entidad_id_med.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid ID.")
            return

        entidad = self.service.get_entidad_by_id(int(entidad_id_med))
        if entidad:
            self.tree.delete(*self.tree.get_children())  # Clear the table
            self.tree.insert('', 'end', values=entidad)  # Insert the search result
        else:
            messagebox.showinfo("Not Found", "Entidad not found.")

    def load_all_entidades(self):
        """Load all entities into the treeview."""
        self.tree.delete(*self.tree.get_children())  # Clear the table
        entidades = self.service.get_all_entidades()
        for entidad in entidades:
            self.tree.insert('', 'end', values=entidad)

    def open_add_window(self):
        """Open a new window to add a new entity."""
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Agregar Entidad")

        # Create input fields for all attributes
        labels = ["Nombre", "Tipo", "RUC", "Dirección", "Teléfono", "Email", "Cédula"]
        self.entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(self.new_window, text=label_text + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            if label_text == "Tipo":
                self.entries[label_text.lower()] = ttk.Combobox(self.new_window,
                                                                values=["Persona Física", "Persona Jurídica",
                                                                        "No Contribuyente"])
                self.entries[label_text.lower()].grid(row=i, column=1, padx=10, pady=5)
            else:
                entry = tk.Entry(self.new_window, font=("Arial", 12))
                entry.grid(row=i, column=1, padx=10, pady=5)
                self.entries[label_text.lower()] = entry

        # Add Button
        self.add_button = tk.Button(self.new_window, text="Agregar", command=self.add_entidad, font=("Arial", 12), bg="#5cb85c", fg="white")
        self.add_button.grid(row=len(labels), column=1, padx=10, pady=10)

    def add_entidad(self):
        """Add a new entity to the database."""
        # Get values from input fields
        nombre_med = self.entries["nombre_med"].get()
        tipo_med = self.entries["tipo_med"].get()
        ruc_med = self.entries["ruc_med"].get()
        direccion_med = self.entries["dirección"].get()
        telefono_med = self.entries["teléfono"].get()
        enail_med = self.entries["enail_med"].get()
        cedula_med = self.entries["cédula"].get()

        # Validate required fields
        if not nombre_med or not tipo_med:
            messagebox.showerror("Error", "Nombre and Tipo are required.")
            return

        # Create the entity
        self.service.create_entidad(nombre_med, tipo_med, ruc_med, direccion_med, telefono_med, enail_med, cedula_med)
        messagebox.showinfo("Success", "Entidad added successfully.")
        self.load_all_entidades()
        self.new_window.destroy()

    def open_update_window(self):
        """Open a new window to update the selected entity."""
        selected_entity = self.tree.selection()
        if not selected_entity:
            messagebox.showerror("Error", "Please select an entity to update.")
            return

        entidad_id_med = self.tree.item(selected_entity)["values"][0]  # Get the ID from the selected row
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Actualizar Entidad")

        entidad = self.service.get_entidad_by_id(entidad_id_med)

        labels = ["Nombre", "Tipo", "RUC", "Dirección", "Teléfono", "Email", "Cédula"]
        self.update_entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(self.update_window, text=label_text + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            if label_text == "Tipo":
                self.update_entries[label_text.lower()] = ttk.Combobox(self.update_window,
                                                                       values=["Persona Física", "Persona Jurídica",
                                                                               "No Contribuyente"])
                self.update_entries[label_text.lower()].grid(row=i, column=1, padx=10, pady=5)
            else:
                entry = tk.Entry(self.update_window, font=("Arial", 12))
                entry.grid(row=i, column=1, padx=10, pady=5)
                self.update_entries[label_text.lower()] = entry

        # Pre-fill the fields with existing entity data
        self.update_entries["nombre_med"].insert(0, entidad[1])
        self.update_entries["tipo_med"].set(entidad[2])  # Combobox uses set() to pre-fill
        self.update_entries["ruc_med"].insert(0, entidad[3])
        self.update_entries["dirección"].insert(0, entidad[4])
        self.update_entries["teléfono"].insert(0, entidad[5])
        self.update_entries["enail_med"].insert(0, entidad[6])
        self.update_entries["cédula"].insert(0, entidad[7])

        # Update button
        self.update_button = tk.Button(self.update_window, text="Actualizar",
                                       command=lambda: self.update_entidad(entidad_id_med), font=("Arial", 12), bg="#f0ad4e", fg="white")
        self.update_button.grid(row=len(labels), column=1, padx=10, pady=10)

    def update_entidad(self, entidad_id_med):
        """Update the selected entity."""
        nombre_med = self.update_entries["nombre_med"].get()
        tipo_med = self.update_entries["tipo_med"].get()
        ruc_med = self.update_entries["ruc_med"].get()
        direccion_med = self.update_entries["dirección"].get()
        telefono_med = self.update_entries["teléfono"].get()
        enail_med = self.update_entries["enail_med"].get()
        cedula_med = self.update_entries["cédula"].get()

        # Validate required fields
        if not nombre_med or not tipo_med:
            messagebox.showerror("Error", "Nombre and Tipo are required.")
            return

        # Update the entity
        self.service.update_entidad(entidad_id_med, nombre_med, tipo_med, ruc_med, direccion_med, telefono_med, enail_med, cedula_med)
        messagebox.showinfo("Success", "Entidad updated successfully.")
        self.load_all_entidades()
        self.update_window.destroy()

    def delete_selected_entidad(self):
        """Delete the selected entity."""
        selected_entity = self.tree.selection()
        if not selected_entity:
            messagebox.showerror("Error", "Please select an entity to delete.")
            return

        entidad_id_med = self.tree.item(selected_entity)["values"][0]
        self.service.delete_entidad(entidad_id_med)
        messagebox.showinfo("Success", "Entidad deleted successfully.")
        self.load_all_entidades()
