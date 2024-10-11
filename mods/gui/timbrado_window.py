import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

from mods.timbrado.service.timbrado_service import TimbradoService


class TimbradoWindow:
    def __init__(self, root, timbrado_service: TimbradoService):
        self.root = root
        self.root.title("Administrar Timbrado")
        self.service = timbrado_service

        # Create the main frame
        self.frame = tk.Frame(self.root, bg="lightgray")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Frame for Search functionality, aligned to the left
        search_frame = tk.Frame(self.frame, bg="lightgray")
        search_frame.grid(row=0, column=0, columnspan=2, sticky="w")

        # Label and Entry for searching by ID
        self.search_label = tk.Label(search_frame, text="Buscar Timbrado por ID:", bg="lightgray", font=("Arial", 12))
        self.search_label.pack(side="left", padx=(0, 10), pady=5)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.pack(side="left", padx=(0, 10), pady=5)
        self.search_button = tk.Button(search_frame, text="Buscar", command=self.search_timbrado, font=("Arial", 12),
                                       bg="#5cb85c", fg="white")
        self.search_button.pack(side="left", pady=5)

        # Treeview for displaying timbrado as a table
        self.tree = ttk.Treeview(self.frame, columns=(
            "ID", "Tipo", "Número Timbrado", "Establecimiento", "Punto Exp.", "Número Documento", "Fecha Inicio"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tipo", text="Tipo de Documento")
        self.tree.heading("Número Timbrado", text="Número Timbrado")
        self.tree.heading("Establecimiento", text="Establecimiento")
        self.tree.heading("Punto Exp.", text="Punto Expedición")
        self.tree.heading("Número Documento", text="Número Documento")
        self.tree.heading("Fecha Inicio", text="Fecha Inicio")

        # Adding uniform width to columns for better presentation
        for col in (
        "ID", "Tipo", "Número Timbrado", "Establecimiento", "Punto Exp.", "Número Documento", "Fecha Inicio"):
            self.tree.column(col, width=120)

        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Button frame to hold action buttons
        button_frame = tk.Frame(self.frame, bg="lightgray")
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Add Button
        self.add_button = tk.Button(button_frame, text="Agregar Timbrado", command=self.open_add_window,
                                    font=("Arial", 12), bg="#0275d8", fg="white")
        self.add_button.pack(side="left", padx=10)

        # Update Button
        self.update_button = tk.Button(button_frame, text="Actualizar Seleccionado", command=self.open_update_window,
                                       font=("Arial", 12), bg="#f0ad4e", fg="white")
        self.update_button.pack(side="left", padx=10)

        # Delete Button
        self.delete_button = tk.Button(button_frame, text="Borrar Seleccionado", command=self.delete_selected_timbrado,
                                       font=("Arial", 12), bg="#d9534f", fg="white")
        self.delete_button.pack(side="left", padx=10)

        # Load all timbrados into the treeview
        self.load_all_timbrados()

    def search_timbrado(self):
        """Search for a timbrado by ID and display its details."""
        timbrado_id_med = self.search_entry.get()
        if not timbrado_id_med.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid ID.")
            return

        timbrado = self.service.get_timbrado_by_id(int(timbrado_id_med))
        if timbrado:
            self.tree.delete(*self.tree.get_children())  # Clear the table
            self.tree.insert('', 'end', values=timbrado)  # Insert the search result
        else:
            messagebox.showinfo("Not Found", "Timbrado not found.")

    def load_all_timbrados(self):
        """Load all timbrados into the treeview."""
        self.tree.delete(*self.tree.get_children())  # Clear the table
        timbrados = self.service.get_all_timbrados()
        for timbrado in timbrados:
            self.tree.insert('', 'end', values=timbrado)

    def open_add_window(self):
        """Open a new window to add a new timbrado."""
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Agregar Timbrado")

        # Create input fields for all attributes
        labels = ["Tipo de Documento", "Número Timbrado", "Establecimiento", "Punto Expedición", "Número Documento",
                  "Fecha Inicio"]
        self.entries = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(self.new_window, text=label_text + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            if label_text == "Tipo de Documento":
                # Add combobox for 'Tipo de Documento'
                self.entries[label_text.lower().replace(" ", "_")] = ttk.Combobox(self.new_window,
                                                                                  values=["Factura", "Nota de Crédito",
                                                                                          "Nota de Débito", "Recibo"])
                self.entries[label_text.lower().replace(" ", "_")].grid(row=i, column=1, padx=10, pady=5)
            elif label_text == "Fecha Inicio":
                # Add simple entry for the date (expecting "YYYY-MM-DD" format)
                self.entries[label_text.lower().replace(" ", "_")] = tk.Entry(self.new_window, font=("Arial", 12))
                self.entries[label_text.lower().replace(" ", "_")].insert(0, datetime.now().strftime(
                    "%Y-%m-%d"))  # Set current date as default
                self.entries[label_text.lower().replace(" ", "_")].grid(row=i, column=1, padx=10, pady=5)
            else:
                entry = tk.Entry(self.new_window, font=("Arial", 12))
                entry.grid(row=i, column=1, padx=10, pady=5)
                self.entries[label_text.lower().replace(" ", "_")] = entry

        # Add Button
        self.add_button = tk.Button(self.new_window, text="Agregar", command=self.add_timbrado, font=("Arial", 12),
                                    bg="#5cb85c", fg="white")
        self.add_button.grid(row=len(labels), column=1, padx=10, pady=10)

    def add_timbrado(self):
        """Add a new timbrado to the database."""
        # Get values from input fields
        tipo_de_documento_med = self.entries["tipo_de_documento_med"].get()
        numero_timbrado_med = self.entries["número_timbrado"].get()
        establecimiento_med = self.entries["establecimiento_med"].get()
        punto_expedicion_med = self.entries["punto_expedición"].get()
        numero_documento_med = self.entries["número_documento"].get()
        fecha_inicio_med = self.entries["fecha_inicio_med"].get()

        # Validate required fields
        if not tipo_de_documento_med or not numero_timbrado_med:
            messagebox.showerror("Error", "Tipo de Documento and Número Timbrado are required.")
            return

        # Create the timbrado
        self.service.create_timbrado(tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med,
                                     numero_documento_med, fecha_inicio_med)
        messagebox.showinfo("Success", "Timbrado added successfully.")
        self.load_all_timbrados()
        self.new_window.destroy()

    def open_update_window(self):
        """Open a new window to update the selected timbrado."""
        selected_entity = self.tree.selection()
        if not selected_entity:
            messagebox.showerror("Error", "Please select a timbrado to update.")
            return

        timbrado_id_med = self.tree.item(selected_entity)["values"][0]  # Get the ID from the selected row
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Actualizar Timbrado")

        timbrado = self.service.get_timbrado_by_id(timbrado_id_med)

        labels = ["Tipo de Documento", "Número Timbrado", "Establecimiento", "Punto Expedición", "Número Documento",
                  "Fecha Inicio"]
        self.update_entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(self.update_window, text=label_text + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            if label_text == "Tipo de Documento":
                self.update_entries[label_text.lower().replace(" ", "_")] = ttk.Combobox(self.update_window,
                                                                                         values=["Factura",
                                                                                                 "Nota de Crédito",
                                                                                                 "Nota de Débito",
                                                                                                 "Recibo"])
                self.update_entries[label_text.lower().replace(" ", "_")].set(
                    timbrado[1])  # Pre-fill with existing data
                self.update_entries[label_text.lower().replace(" ", "_")].grid(row=i, column=1, padx=10, pady=5)
            elif label_text == "Fecha Inicio":
                self.update_entries[label_text.lower().replace(" ", "_")] = tk.Entry(self.update_window,
                                                                                     font=("Arial", 12))
                self.update_entries[label_text.lower().replace(" ", "_")].insert(0, timbrado[6])
                self.update_entries[label_text.lower().replace(" ", "_")].grid(row=i, column=1, padx=10, pady=5)
            else:
                entry = tk.Entry(self.update_window, font=("Arial", 12))
                entry.grid(row=i, column=1, padx=10, pady=5)
                entry.insert(0, timbrado[i + 1])  # Pre-fill with existing data
                self.update_entries[label_text.lower().replace(" ", "_")] = entry

        # Update button
        self.update_button = tk.Button(self.update_window, text="Actualizar",
                                       command=lambda: self.update_timbrado(timbrado_id_med), font=("Arial", 12),
                                       bg="#f0ad4e", fg="white")
        self.update_button.grid(row=len(labels), column=1, padx=10, pady=10)

    def update_timbrado(self, timbrado_id_med):
        """Update the selected timbrado."""
        tipo_de_documento_med = self.update_entries["tipo_de_documento_med"].get()
        numero_timbrado_med = self.update_entries["número_timbrado"].get()
        establecimiento_med = self.update_entries["establecimiento_med"].get()
        punto_expedicion_med = self.update_entries["punto_expedición"].get()
        numero_documento_med = self.update_entries["número_documento"].get()
        fecha_inicio_med = self.update_entries["fecha_inicio_med"].get()

        # Validate required fields
        if not tipo_de_documento_med or not numero_timbrado_med:
            messagebox.showerror("Error", "Tipo de Documento and Número Timbrado are required.")
            return

        # Update the timbrado
        self.service.update_timbrado(timbrado_id_med, tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med,
                                     numero_documento_med, fecha_inicio_med)
        messagebox.showinfo("Success", "Timbrado updated successfully.")
        self.load_all_timbrados()
        self.update_window.destroy()

    def delete_selected_timbrado(self):
        """Delete the selected timbrado."""
        selected_entity = self.tree.selection()
        if not selected_entity:
            messagebox.showerror("Error", "Please select a timbrado to delete.")
            return

        timbrado_id_med = self.tree.item(selected_entity)["values"][0]
        self.service.delete_timbrado(timbrado_id_med)
        messagebox.showinfo("Success", "Timbrado deleted successfully.")
        self.load_all_timbrados()
