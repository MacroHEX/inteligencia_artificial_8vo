import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox

from mods.detalle_factura.service.detalle_factura_service import DetalleFacturaService
from mods.entidad.service.entidad_service import EntidadService
from mods.factura.service.factura_service import FacturaService
from mods.producto.service.producto_service import ProductoService
from mods.timbrado.service.timbrado_service import TimbradoService


class FacturaWindow:
    def __init__(self, root, factura_service: FacturaService, detalle_factura_service: DetalleFacturaService,
                 producto_service: ProductoService, entidad_service: EntidadService, timbrado_service: TimbradoService):
        self.root = root
        self.root.title("Administrar Facturas")
        self.factura_service = factura_service
        self.detalle_factura_service = detalle_factura_service
        self.producto_service = producto_service
        self.entidad_service = entidad_service
        self.timbrado_service = timbrado_service
        self.selected_productos = []  # Store selected products
        self.total = 0
        self.iva = 0
        self.current_factura_id = None  # Store factura ID

        # Create the main frame
        self.frame = tk.Frame(self.root, bg="lightgray")
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Treeview for displaying facturas as a table
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Fecha", "Entidad", "Timbrado", "Total", "Estado"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Fecha", text="Fecha Emisión")
        self.tree.heading("Entidad", text="Entidad")
        self.tree.heading("Timbrado", text="Número Timbrado")
        self.tree.heading("Total", text="Total")
        self.tree.heading("Estado", text="Estado")

        # Adding uniform width to columns for better presentation
        for col in ("ID", "Fecha", "Entidad", "Timbrado", "Total", "Estado"):
            self.tree.column(col, width=120)

        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Button frame to hold action buttons
        button_frame = tk.Frame(self.frame, bg="lightgray")
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Add Button
        self.add_button = tk.Button(button_frame, text="Agregar Factura", command=self.open_add_window,
                                    font=("Arial", 12), bg="#0275d8", fg="white")
        self.add_button.pack(side="left", padx=10)

        # Update Button
        self.update_button = tk.Button(button_frame, text="Actualizar Seleccionado", command=self.open_update_window,
                                       font=("Arial", 12), bg="#f0ad4e", fg="white")
        self.update_button.pack(side="left", padx=10)

        # Delete Button
        self.delete_button = tk.Button(button_frame, text="Borrar Seleccionado", command=self.delete_selected_factura,
                                       font=("Arial", 12), bg="#d9534f", fg="white")
        self.delete_button.pack(side="left", padx=10)

        # Load all facturas into the treeview
        self.load_all_facturas()

    def load_all_facturas(self):
        """Load all facturas into the treeview."""
        self.tree.delete(*self.tree.get_children())  # Clear the table
        facturas = self.factura_service.get_all_facturas()
        for factura in facturas:
            # Fetch entidad name and timbrado number
            entidad = self.entidad_service.get_entidad_by_id(factura[2])
            timbrado = self.timbrado_service.get_timbrado_by_id(factura[3])
            self.tree.insert('', 'end',
                             values=(factura[0], factura[1], entidad[1], timbrado[1], factura[4], factura[5]))

    def open_add_window(self):
        """Open a new window to add a new factura."""
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Agregar Factura")

        # Input fields for Factura
        labels = ["Fecha Emisión", "Entidad ID", "Timbrado ID", "Total", "IVA 10%", "Estado"]
        self.factura_entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(self.new_window, text=label_text + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            if label_text == "Estado":
                entry = Combobox(self.new_window, values=["Pagada", "Pendiente", "Cancelada"], font=("Arial", 12))
            elif label_text == "Fecha Emisión":
                entry = tk.Entry(self.new_window, font=("Arial", 12))
                entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Automatically set to today's date
            else:
                entry = tk.Entry(self.new_window, font=("Arial", 12))
                if label_text in ["Total", "IVA 10%"]:
                    entry.config(state="readonly")

            entry.grid(row=i, column=1, padx=10, pady=5)
            self.factura_entries[label_text.lower().replace(" ", "_")] = entry

        # Add search for Entidad
        self.entidad_search_button = tk.Button(self.new_window, text="Buscar Entidad", command=self.search_entidad,
                                               font=("Arial", 12), bg="#0275d8", fg="white")
        self.entidad_search_button.grid(row=1, column=2, padx=10, pady=5)

        # Add search for Timbrado
        self.timbrado_search_button = tk.Button(self.new_window, text="Buscar Timbrado", command=self.search_timbrado,
                                                font=("Arial", 12), bg="#0275d8", fg="white")
        self.timbrado_search_button.grid(row=2, column=2, padx=10, pady=5)

        # Add Detalles Button
        self.add_detalles_button = tk.Button(self.new_window, text="Agregar Productos",
                                             command=self.open_detalle_window, font=("Arial", 12), bg="#0275d8",
                                             fg="white")
        self.add_detalles_button.grid(row=len(labels), column=1, padx=10, pady=10)

        # Add Finalizar Factura Button
        self.add_factura_button = tk.Button(self.new_window, text="Finalizar Factura", command=self.finalizar_factura,
                                            font=("Arial", 12), bg="#5cb85c", fg="white")
        self.add_factura_button.grid(row=len(labels) + 1, column=1, padx=10, pady=10)

    def search_entidad(self):
        """Open a window to select an Entidad."""
        entidad_window = tk.Toplevel(self.root)
        entidad_window.title("Seleccionar Entidad")

        # Create Treeview to display Entidades
        tree = ttk.Treeview(entidad_window, columns=("ID", "Nombre", "Tipo"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Tipo", text="Tipo")

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        entidades = self.entidad_service.get_all_entidades()
        for entidad in entidades:
            tree.insert("", "end", values=(entidad[0], entidad[1], entidad[2]))

        def select_entidad():
            selected_item = tree.selection()
            if selected_item:
                entidad_id = tree.item(selected_item)["values"][0]
                self.factura_entries["entidad_id"].delete(0, tk.END)
                self.factura_entries["entidad_id"].insert(0, entidad_id)
                entidad_window.destroy()

        select_button = tk.Button(entidad_window, text="Seleccionar", command=select_entidad)
        select_button.pack(pady=10)

    def search_timbrado(self):
        """Open a window to select a Timbrado."""
        timbrado_window = tk.Toplevel(self.root)
        timbrado_window.title("Seleccionar Timbrado")

        # Create Treeview to display Timbrados
        tree = ttk.Treeview(timbrado_window, columns=("ID", "Numero", "Establecimiento"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Numero", text="Número Timbrado")
        tree.heading("Establecimiento", text="Establecimiento")

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        timbrados = self.timbrado_service.get_all_timbrados()
        for timbrado in timbrados:
            tree.insert("", "end", values=(timbrado[0], timbrado[2], timbrado[3]))

        def select_timbrado():
            selected_item = tree.selection()
            if selected_item:
                timbrado_id = tree.item(selected_item)["values"][0]
                self.factura_entries["timbrado_id"].delete(0, tk.END)
                self.factura_entries["timbrado_id"].insert(0, timbrado_id)
                timbrado_window.destroy()

        select_button = tk.Button(timbrado_window, text="Seleccionar", command=select_timbrado)
        select_button.pack(pady=10)

    def open_detalle_window(self):
        """Open a window to select Productos and add to the factura."""
        self.detalle_window = tk.Toplevel(self.root)
        self.detalle_window.title("Agregar Productos")

        # Create Treeview to display Productos
        tree = ttk.Treeview(self.detalle_window, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.heading("Stock", text="Stock")

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        productos = self.producto_service.get_all_productos()
        for producto in productos:
            tree.insert("", "end",
                        values=(producto[0], producto[2], producto[4], producto[5]))  # Adjusted column positions

        # Create a quantity input
        tk.Label(self.detalle_window, text="Cantidad:").pack(padx=10, pady=5)
        self.cantidad_entry = tk.Entry(self.detalle_window)
        self.cantidad_entry.pack(padx=10, pady=5)

        def select_producto():
            selected_item = tree.selection()
            if selected_item:
                producto_id = tree.item(selected_item)["values"][0]  # ID is at index 0
                nombre_producto = tree.item(selected_item)["values"][1]  # Nombre is at index 1
                precio_unitario = float(tree.item(selected_item)["values"][2])  # Precio is at index 2
                stock = int(tree.item(selected_item)["values"][3])  # Stock is at index 3
                cantidad = int(self.cantidad_entry.get())

                # Validate stock
                if cantidad > stock:
                    messagebox.showerror("Error", f"El stock disponible es insuficiente. Stock disponible: {stock}")
                    return

                subtotal = cantidad * precio_unitario
                self.total += subtotal
                self.iva = self.total * 0.10

                # Update total and IVA fields dynamically
                self.factura_entries["total"].config(state="normal")
                self.factura_entries["iva_10%"].config(state="normal")
                self.factura_entries["total"].delete(0, tk.END)
                self.factura_entries["total"].insert(0, str(self.total))
                self.factura_entries["iva_10%"].delete(0, tk.END)
                self.factura_entries["iva_10%"].insert(0, str(self.iva))
                self.factura_entries["total"].config(state="readonly")
                self.factura_entries["iva_10%"].config(state="readonly")

                # Store selected product details
                self.selected_productos.append((producto_id, cantidad, precio_unitario, subtotal))

                messagebox.showinfo("Success", f"Producto {nombre_producto} agregado a la factura.")
                self.detalle_window.destroy()

        # Add selection functionality for the product
        select_button = tk.Button(self.detalle_window, text="Seleccionar Producto", command=select_producto)
        select_button.pack(pady=10)

    def finalizar_factura(self):
        """Finalize the factura by saving it to the database and deducting stock."""
        entidad_id = self.factura_entries["entidad_id"].get()
        timbrado_id = self.factura_entries["timbrado_id"].get()
        estado = self.factura_entries["estado"].get()

        # Validate required fields
        if not entidad_id or not timbrado_id or not self.selected_productos:
            messagebox.showerror("Error", "Complete todos los campos y agregue productos.")
            return

        # Save factura to the database
        self.current_factura_id = self.factura_service.create_factura(
            datetime.now().strftime("%Y-%m-%d"), entidad_id, timbrado_id, self.total, estado
        )

        # Save detalles and deduct stock
        for producto_id, cantidad, precio_unitario, subtotal in self.selected_productos:
            # Retrieve the product details
            producto = self.producto_service.get_producto_by_id(producto_id)

            # Ensure the Producto object is passed correctly with correct column mapping
            new_stock = producto[5] - cantidad  # Stock is at index 5

            # Update product using all required parameters
            self.producto_service.update_producto(
                producto_id,
                producto[1],  # codigo_interno (index 1)
                producto[2],  # nombre (index 2)
                producto[3],  # descripcion (index 3)
                producto[4],  # precio (index 4)
                new_stock  # updated stock
            )

            # Add detalle_factura
            self.detalle_factura_service.create_detalle_factura(
                self.current_factura_id, producto_id, cantidad, precio_unitario, subtotal
            )

        messagebox.showinfo("Success", "Factura finalizada y guardada exitosamente.")
        self.new_window.destroy()
        self.load_all_facturas()

    def open_update_window(self):
        """Open a new window to update the selected factura."""
        selected_entity = self.tree.selection()
        if not selected_entity:
            messagebox.showerror("Error", "Seleccione una factura para actualizar.")
            return

        factura_id = self.tree.item(selected_entity)["values"][0]
        self.update_window = tk.Toplevel(self.root)
        self.update_window.title("Actualizar Factura")

        factura = self.factura_service.get_factura_by_id(factura_id)

        # Input fields for Factura update
        labels = ["Fecha Emisión", "Entidad ID", "Timbrado ID", "Total", "Estado"]
        self.update_entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(self.update_window, text=label_text + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.update_window, font=("Arial", 12))
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.update_entries[label_text.lower().replace(" ", "_")] = entry

        # Pre-fill the fields with existing factura data
        self.update_entries["fecha_emision"].insert(0, factura[1])
        self.update_entries["entidad_id"].insert(0, factura[2])
        self.update_entries["timbrado_id"].insert(0, factura[3])
        self.update_entries["total"].insert(0, factura[4])
        self.update_entries["estado"].insert(0, factura[5])

        # Update button
        self.update_button = tk.Button(self.update_window, text="Actualizar",
                                       command=lambda: self.update_factura(factura_id), font=("Arial", 12),
                                       bg="#f0ad4e", fg="white")
        self.update_button.grid(row=len(labels), column=1, padx=10, pady=10)

    def update_factura(self, factura_id):
        """Update the selected factura."""
        fecha_emision = self.update_entries["fecha_emision"].get()
        entidad_id = self.update_entries["entidad_id"].get()
        timbrado_id = self.update_entries["timbrado_id"].get()
        total = self.update_entries["total"].get()
        estado = self.update_entries["estado"].get()

        if not fecha_emision or not entidad_id or not timbrado_id or not total or not estado:
            messagebox.showerror("Error", "Todos los campos son requeridos.")
            return

        self.factura_service.update_factura(factura_id, fecha_emision, entidad_id, timbrado_id, float(total), estado)
        messagebox.showinfo("Success", "Factura actualizada exitosamente.")
        self.load_all_facturas()
        self.update_window.destroy()

    def delete_selected_factura(self):
        """Delete the selected factura."""
        selected_entity = self.tree.selection()
        if not selected_entity:
            messagebox.showerror("Error", "Seleccione una factura para eliminar.")
            return

        factura_id = self.tree.item(selected_entity)["values"][0]
        self.factura_service.delete_factura(factura_id)
        messagebox.showinfo("Success", "Factura eliminada exitosamente.")
        self.load_all_facturas()
