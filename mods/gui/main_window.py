import tkinter as tk

from PIL import Image, ImageTk

from mods.gui.entidad_window import EntidadWindow
from mods.gui.factura_window import FacturaWindow
from mods.gui.producto_window import ProductoWindow
from mods.gui.timbrado_window import TimbradoWindow


def open_entidad_module(entidad_service):
    """Opens the Entidad module window."""
    entidad_window = tk.Toplevel()  # Create a new Toplevel window for Entidades
    EntidadWindow(entidad_window, entidad_service)  # Pass the EntidadService to the EntidadWindow


def open_timbrado_module(timbrado_service):
    """Opens the Timbrado module window."""
    timbrado_window = tk.Toplevel()  # Create a new Toplevel window for Timbrado
    TimbradoWindow(timbrado_window, timbrado_service)  # Pass the TimbradoService to the TimbradoWindow


def open_factura_module(factura_service, detalle_factura_service, producto_service, entidad_service, timbrado_service):
    """Opens the Factura module window."""
    factura_window = tk.Toplevel()  # Create a new Toplevel window for Factura
    FacturaWindow(factura_window, factura_service, detalle_factura_service, producto_service, entidad_service,
                  timbrado_service)  # Pass all the required services


def open_producto_module(producto_service):
    timbrado_window = tk.Toplevel()  # Create a new Toplevel window for Producto
    ProductoWindow(timbrado_window, producto_service)  # Pass the ProductoService to the ProductoWindow


class MainWindow:
    def __init__(self, root, entidad_service, timbrado_service, producto_service, factura_service,
                 detalle_factura_service):
        self.root = root
        self.root.title("Factura Martin Medina")
        self.root.geometry("950x800")
        self.root.resizable(False, False)
        self.root.configure(bg="lightgray")

        self.create_custom_title()

        self.entidad_service = entidad_service  # Store the EntidadService instance
        self.timbrado_service = timbrado_service  # Store the TimbradoService instance
        self.producto_service = producto_service  # Store the ProductoService instance
        self.factura_service = factura_service
        self.detalle_factura_service = detalle_factura_service

        # Load and resize images for buttons
        self.entidad_image = self.resize_image("assets/imgs/entities.png", 256, 256)
        self.timbrado_image = self.resize_image("assets/imgs/timbrado.png", 256, 256)
        self.factura_image = self.resize_image("assets/imgs/invoice.png", 256, 256)
        self.producto_image = self.resize_image("assets/imgs/product.png", 256, 256)
        self.exit_image = self.resize_image("assets/imgs/exit.png", 256, 256)

        # Frame to hold the buttons in a grid layout
        self.button_frame = tk.Frame(self.root, bg="lightgray")
        self.button_frame.pack(pady=20)

        # Create buttons with images in a 2x3 grid
        self.entidad_button = tk.Button(self.button_frame, text="Entidades", image=self.entidad_image,
                                        compound="top", command=lambda: open_entidad_module(self.entidad_service))
        self.entidad_button.grid(row=0, column=0, padx=10, pady=10)

        self.timbrado_button = tk.Button(self.button_frame, text="Timbrado", image=self.timbrado_image,
                                         compound="top", command=lambda: open_timbrado_module(self.timbrado_service))
        self.timbrado_button.grid(row=0, column=1, padx=10, pady=10)

        self.factura_button = tk.Button(self.button_frame, text="Factura", image=self.factura_image,
                                        compound="top", command=lambda: open_factura_module(
                self.factura_service, self.detalle_factura_service,
                self.producto_service, self.entidad_service, self.timbrado_service))
        self.factura_button.grid(row=0, column=2, padx=10, pady=10)

        self.producto_button = tk.Button(self.button_frame, text="Productos", image=self.producto_image,
                                         compound="top", command=lambda: open_producto_module(self.producto_service))
        self.producto_button.grid(row=1, column=0, padx=10, pady=10)

        self.exit_button = tk.Button(self.button_frame, text="Salir", image=self.exit_image, compound="top",
                                     command=self.root.quit)
        self.exit_button.grid(row=1, column=1, padx=10, pady=10)

    def resize_image(self, image_path, width, height):
        """
        Resizes the image to fit within the buttons.
        :param image_path: Path to the image file.
        :param width: Desired width.
        :param height: Desired height.
        :return: Resized PhotoImage.
        """
        image = Image.open(image_path)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def create_custom_title(self):
        # Create a frame for the title
        title_frame = tk.Frame(self.root, bg="lightgray")
        title_frame.pack(fill="x", padx=10, pady=10)

        # Create the label for 'Martin Medina' aligned to the right
        right_title = tk.Label(title_frame, text="Martin Medina", font=("Arial", 20), bg="lightgray")
        right_title.pack(side="right", anchor="e")  # Align to the right
