import tkinter as tk
from tkinter import messagebox, ttk

from mods.producto.service.producto_service import ProductoService


class ProductoWindow:
    def __init__(self, root, producto_service: ProductoService):
        self.root = root
        self.root.title("Administrar Productos")
        self.service = producto_service

        # Create the main frame
        self.frame = tk.Frame(self.root, bg="lightgray")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Frame for Search functionality, aligned to the left
        search_frame = tk.Frame(self.frame, bg="lightgray")
        search_frame.grid(row=0, column=0, columnspan=2, sticky="w")

        # Label and Entry for searching by ID
        self.search_label = tk.Label(search_frame, text="Buscar Producto por ID:", bg="lightgray", font=("Arial", 12))
        self.search_label.pack(side="left", padx=(0, 10), pady=5)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.pack(side="left", padx=(0, 10), pady=5)
        self.search_button = tk.Button(search_frame, text="Buscar", command=self.search_producto, font=("Arial", 12),
                                       bg="#5cb85c", fg="white")
        self.search_button.pack(side="left", pady=5)

        # Treeview for displaying productos as a table
        self.tree = ttk.Treeview(self.frame, columns=(
            "ID", "Código Interno", "Nombre", "Descripción", "Precio", "Stock"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Código Interno", text="Código Interno")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Stock", text="Stock")

        # Adding uniform width to columns for better presentation
        for col in ("ID", "Código Interno", "Nombre", "Descripción", "Precio", "Stock"):
            self.tree.column(col, width=120)

        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Button frame to hold action buttons
        button_frame = tk.Frame(self.frame, bg="lightgray")
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Add Button
        self.add_button = tk.Button(button_frame, text="Agregar Producto", command=self.open_add_window,
                                    font=("Arial", 12), bg="#0275d8", fg="white")
        self.add_button.pack(side="left", padx=10)

        # Update Button
        self.update_button = tk.Button(button_frame, text="Actualizar Seleccionado", command=self.open_update_window,
                                       font=("Arial", 12), bg="#f0ad4e", fg="white")
        self.update_button.pack(side="left", padx=10)

        # Delete Button
        self.delete_button = tk.Button(button_frame, text="Borrar Seleccionado", command=self.delete_selected_producto,
                                       font=("Arial", 12), bg="#d9534f", fg="white")
        self.delete_button.pack(side="left", padx=10)

        # Load all productos into the treeview
        self.load_all_productos()

    def search_producto(self):
        """Search for a producto by ID and display its details."""
        producto_id_med = self.search_entry.get()
        if not producto_id_med.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid ID.")
            return

        producto = self.service.get_producto_by_id(int(producto_id_med))
        if producto:
            self.tree.delete(*self.tree.get_children())  # Clear the table
            self.tree.insert('', 'end', values=producto)  # Insert the search result
        else:
            messagebox.showinfo("Not Found", "Producto not found.")

    def load_all_productos(self):
        """Load all productos into the treeview."""
        self.tree.delete(*self.tree.get_children())  # Clear the table
        productos = self.service.get_all_productos()
        for producto in productos:
            self.tree.insert('', 'end', values=producto)

    def open_add_window(self):
        """Open a new window to add a new producto."""
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Agregar Producto")

        # Create input fields for all attributes
        labels = ["Código Interno", "Nombre", "Descripción", "Precio", "Stock"]
        self.entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(self.new_window, text=label_text + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.new_window, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label_text.lower().replace(" ", "_")] = entry

        # Add Button
        self.add_button = tk.Button(self.new_window, text="Agregar", command=self.add_producto, font=("Arial", 12),
                                    bg="#5cb85c", fg="white")
        self.add_button.grid(row=len(labels), column=1, padx=10, pady=10)

    def add_producto(self):
        """Add a new producto to the database."""
        # Get values from input fields
        codigo_interno_med = self.entries["código_interno"].get()
        nombre_med = self.entries["nombre_med"].get()
        descripcion_med = self.entries["descripción"].get()
        precio_med = self.entries["precio_med"].get()
        stock_med = self.entries["stock_med"].get()

        # Validate required fields
        if not codigo_interno_med or not nombre_med or not precio_med or not stock_med:
            messagebox.showerror("Error", "Código Interno, Nombre, Precio, and Stock are required.")
            return

        # Create the producto
        self.service.create_producto(codigo_interno_med, nombre_med, descripcion_med, float(precio_med), int(stock_med))
        messagebox.showinfo("Success", "Producto added successfully.")
        self.load_all_productos()
        self.new_window.destroy()

    def open_update_window(self):
        """Open a new window to update the selected producto."""
        selected_entity = self.tree.selection()
        if not selected_entity:
            messagebox.showerror("Error", "Please select a producto to update.")
            return

        producto_id_med = self.tree.item(selected_entity)["values"][0]  # Get the ID from the selected row
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Actualizar Producto")

        producto = self.service.get_producto_by_id(producto_id_med)

        labels = ["Código Interno", "Nombre", "Descripción", "Precio", "Stock"]
        self.update_entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(self.update_window, text=label_text + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.update_window, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.update_entries[label_text.lower().replace(" ", "_")] = entry

        # Pre-fill the fields with existing producto data
        self.update_entries["código_interno"].insert(0, producto[1])
        self.update_entries["nombre_med"].insert(0, producto[2])
        self.update_entries["descripción"].insert(0, producto[3])
        self.update_entries["precio_med"].insert(0, producto[4])
        self.update_entries["stock_med"].insert(0, producto[5])

        # Update button
        self.update_button = tk.Button(self.update_window, text="Actualizar",
                                       command=lambda: self.update_producto(producto_id_med), font=("Arial", 12),
                                       bg="#f0ad4e", fg="white")
        self.update_button.grid(row=len(labels), column=1, padx=10, pady=10)

    def update_producto(self, producto_id_med):
        """Update the selected producto."""
        codigo_interno_med = self.update_entries["código_interno"].get()
        nombre_med = self.update_entries["nombre_med"].get()
        descripcion_med = self.update_entries["descripción"].get()
        precio_med = self.update_entries["precio_med"].get()
        stock_med = self.update_entries["stock_med"].get()

        # Validate required fields
        if not codigo_interno_med or not nombre_med or not precio_med or not stock_med:
            messagebox.showerror("Error", "Código Interno, Nombre, Precio, and Stock are required.")
            return

        # Update the producto
        self.service.update_producto(producto_id_med, codigo_interno_med, nombre_med, descripcion_med, float(precio_med), int(stock_med))
        messagebox.showinfo("Success", "Producto updated successfully.")
        self.load_all_productos()
        self.update_window.destroy()

    def delete_selected_producto(self):
        """Delete the selected producto."""
        selected_entity = self.tree.selection()
        if not selected_entity:
            messagebox.showerror("Error", "Please select a producto to delete.")
            return

        producto_id_med = self.tree.item(selected_entity)["values"][0]
        self.service.delete_producto(producto_id_med)
        messagebox.showinfo("Success", "Producto deleted successfully.")
        self.load_all_productos()
