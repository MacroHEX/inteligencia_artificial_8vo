import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk
from tkinter.ttk import Combobox

from mods.detalle_factura.model.detalle_factura_entity import DetalleFactura
from mods.detalle_factura.service.detalle_factura_service import DetalleFacturaService
from mods.entidad.service.entidad_service import EntidadService
from mods.factura.model.factura_entity import Factura
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

        # Retrieve the business RUC from entidad with ID 2
        self.business_ruc = self.get_business_ruc()

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

        # Delete Button
        self.delete_button = tk.Button(button_frame, text="Borrar Seleccionado", command=self.delete_selected_factura,
                                       font=("Arial", 12), bg="#d9534f", fg="white")
        self.delete_button.pack(side="left", padx=10)

        # Load all facturas into the treeview
        self.load_all_facturas()

    def get_business_ruc(self):
        """Get the RUC of the business using entidad ID 2."""
        business_entidad = self.entidad_service.get_entidad_by_id(2)  # Assuming ID 2 is the business
        if business_entidad:
            return business_entidad[2]  # 'ruc' is at index 2 in the tuple
        else:
            messagebox.showerror("Error", "No se pudo encontrar la entidad del negocio con ID 2.")
            return None

    def load_all_facturas(self):
        """Load all facturas into the treeview."""
        self.tree.delete(*self.tree.get_children())  # Clear the table
        facturas = self.factura_service.get_all_facturas()
        for factura in facturas:
            # Fetch entidad and timbrado
            entidad = self.entidad_service.get_entidad_by_id(factura[2])
            timbrado = self.timbrado_service.get_timbrado_by_id(factura[3])

            # Ensure both entidad and timbrado exist
            entidad_name = entidad[1] if entidad else "Entidad no encontrada"
            timbrado_number = timbrado[2] if timbrado else "Timbrado no encontrado"

            try:
                nro_documento = int(timbrado[5])  # Convert to int if it's numeric
            except ValueError:
                nro_documento = "Número inválido"  # Handle non-numeric values

            timbrado_str = f"{timbrado_number}-{nro_documento}"

            self.tree.insert('', 'end',
                             values=(factura[0], factura[1], entidad_name, timbrado_str, factura[4], factura[5]))

    def open_add_window(self):
        """Open a new window to add a new factura."""
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Agregar Factura")

        # Input fields for Factura
        labels = ["Fecha Emisión", "Entidad", "Timbrado", "Total", "IVA 10%", "Subtotal", "Estado"]
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
                if label_text in ["Total", "IVA 10%", "Subtotal"]:
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
                entidad_id = tree.item(selected_item)["values"][1]
                self.factura_entries["entidad"].delete(0, tk.END)
                self.factura_entries["entidad"].insert(0, entidad_id)
                entidad_window.destroy()

        select_button = tk.Button(entidad_window, text="Seleccionar", command=select_entidad)
        select_button.pack(pady=10)

    def search_timbrado(self):
        """Open a window to select a Timbrado."""
        timbrado_window = tk.Toplevel(self.root)
        timbrado_window.title("Seleccionar Timbrado")

        # Create Treeview to display Timbrados
        tree = ttk.Treeview(timbrado_window, columns=("ID", "Numero", "Establecimiento", "Numero Documento"),
                            show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Numero", text="Número Timbrado")
        tree.heading("Establecimiento", text="Establecimiento")
        tree.heading("Numero Documento", text="Número Documento")

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        timbrados = self.timbrado_service.get_all_timbrados()
        for timbrado in timbrados:
            # Notice we are using timbrado[0] for ID and timbrado[5] for numero_documento now
            tree.insert("", "end", values=(
                timbrado[0], timbrado[2], timbrado[3], timbrado[5]))  # Add numero_documento as timbrado[5]

        def select_timbrado():
            selected_item = tree.selection()
            if selected_item:
                timbrado_id = tree.item(selected_item)["values"][0]  # Fetch the correct ID (from index 0)
                numero_timbrado = tree.item(selected_item)["values"][1]  # Fetch the numero_timbrado (from index 1)
                numero_documento = tree.item(selected_item)["values"][3]  # Fetch the numero_documento (from index 3)

                self.factura_entries["timbrado"].delete(0, tk.END)
                self.factura_entries["timbrado"].insert(0, numero_timbrado)  # Insert the numero_timbrado in the entry

                # Store the numero_documento if needed elsewhere in the code
                self.factura_entries[
                    "numero_documento"] = numero_documento  # You can access this elsewhere in your logic

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

                # Update total, IVA, and Subtotal fields dynamically
                self.factura_entries["total"].config(state="normal")
                self.factura_entries["iva_10%"].config(state="normal")
                self.factura_entries["subtotal"].config(state="normal")

                self.factura_entries["total"].delete(0, tk.END)
                self.factura_entries["total"].insert(0, str(self.total))

                self.factura_entries["iva_10%"].delete(0, tk.END)
                self.factura_entries["iva_10%"].insert(0, str(self.iva))

                self.factura_entries["subtotal"].delete(0, tk.END)
                self.factura_entries["subtotal"].insert(0, str(subtotal))

                self.factura_entries["total"].config(state="readonly")
                self.factura_entries["iva_10%"].config(state="readonly")
                self.factura_entries["subtotal"].config(state="readonly")

                # Store selected product details
                self.selected_productos.append((producto_id, cantidad, precio_unitario, subtotal))

                messagebox.showinfo("Success", f"Producto {nombre_producto} agregado a la factura.")
                self.detalle_window.destroy()

        # Add selection functionality for the product
        select_button = tk.Button(self.detalle_window, text="Seleccionar Producto", command=select_producto)
        select_button.pack(pady=10)

    def finalizar_factura(self):
        """Finalize the factura by saving it to the database and deducting stock."""
        entidad_id = self.factura_entries["entidad"].get()
        numero_timbrado = self.factura_entries["timbrado"].get()  # Fetch numero_timbrado
        estado = self.factura_entries["estado"].get()

        # Lookup timbrado by numero_timbrado to get the ID
        timbrado = self.timbrado_service.get_timbrado_by_numero(numero_timbrado)
        if not timbrado:
            messagebox.showerror("Error", "Timbrado no encontrado.")
            return

        timbrado_id = timbrado[0]  # ID is at index 0

        # Ensure numero_documento is fetched correctly (index 5)
        try:
            nro_documento_actual = int(timbrado[5])  # Correct index for 'numero_documento' is 5
            print(f"Numero Documento fetched: {nro_documento_actual}")  # Debug print
            nuevo_numero_documento = nro_documento_actual + 1
        except ValueError:
            # Handle cases where the value is not an integer
            print(f"Invalid conversion attempt for numero_documento: {timbrado[5]}")  # Print what's causing the error
            messagebox.showerror("Error", f"El número de documento '{timbrado[5]}' no es válido.")  # Corrected index
            return

        # Additional debug to ensure correct field update
        print(f"Updating timbrado with new numero_documento: {nuevo_numero_documento}")

        # Validate required fields
        if not entidad_id or not timbrado_id or not self.selected_productos:
            messagebox.showerror("Error", "Complete todos los campos y agregue productos.")
            return

        # Create the factura object
        factura = Factura(datetime.now().strftime("%Y-%m-%d"), entidad_id, timbrado_id, self.total, estado)

        # Prepare the list of DetalleFactura objects
        detalles = []
        for producto_id, cantidad, precio_unitario, subtotal in self.selected_productos:
            detalle_factura = DetalleFactura(None, producto_id, cantidad, precio_unitario, subtotal)
            detalles.append(detalle_factura)

        try:
            # Save factura and its details using a transaction
            self.current_factura_id = self.factura_service.create_factura_with_detalles(factura, detalles)

            # Update timbrado with incremented numero_documento
            # Remove str() to keep numero_documento as an integer
            self.timbrado_service.update_timbrado(
                timbrado_id,
                timbrado[1],  # tipo_de_documento (Factura)
                timbrado[2],  # numero_timbrado (001-001)
                timbrado[3],  # establecimiento (M)
                timbrado[4],  # punto_expedicion (A)
                nuevo_numero_documento,  # Keep numero_documento as an integer
                timbrado[6]  # fecha_inicio
            )

            # Deduct stock for each product
            for producto_id, cantidad, precio_unitario, subtotal in self.selected_productos:
                producto = self.producto_service.get_producto_by_id(producto_id)
                new_stock = producto[5] - cantidad  # Assuming stock is at index 5

                # Update product stock
                self.producto_service.update_producto(
                    producto_id,
                    producto[1],  # codigo_interno
                    producto[2],  # nombre
                    producto[3],  # descripcion
                    producto[4],  # precio
                    new_stock  # updated stock
                )

            messagebox.showinfo("Success", "Factura finalizada y guardada exitosamente.")
            self.new_window.destroy()
            self.load_all_facturas()

        except Exception as e:
            print(f"Transaction Error: {str(e)}")  # More details in debug log
            messagebox.showerror("Error", f"Ocurrió un error al finalizar la factura: {str(e)}")

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
