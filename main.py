import tkinter as tk

from config.database import initialize_db, close_db
from mods.detalle_factura.service.detalle_factura_service import DetalleFacturaService
from mods.entidad.service.entidad_service import EntidadService
from mods.factura.service.factura_service import FacturaService
from mods.gui.main_window import MainWindow
from mods.producto.service.producto_service import ProductoService
from mods.timbrado.service.timbrado_service import TimbradoService


def main():
    # Initialize the database
    connection = initialize_db()

    if connection:
        # Create an instance of the Services with the existing connection
        entidad_service = EntidadService(connection)
        timbrado_service = TimbradoService(connection)
        producto_service = ProductoService(connection)
        factura_service = FacturaService(connection)
        detalle_factura_service = DetalleFacturaService(connection)

        # Initialize the main window and pass the entidad_service
        root = tk.Tk()
        app = MainWindow(root, entidad_service, timbrado_service, producto_service, factura_service,
                         detalle_factura_service)
        root.mainloop()

        # Close the database connection after the GUI is closed
        close_db(connection)


if __name__ == "__main__":
    main()
