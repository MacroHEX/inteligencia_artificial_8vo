import sqlite3

from mods.detalle_factura.repository.detalle_factura_repository import DetalleFacturaRepository
from mods.entidad.repository.entidad_repository import EntidadRepository
from mods.factura.repository.factura_repository import FacturaRepository
from mods.impuesto.repository.impuesto_repository import ImpuestoRepository
from mods.pagos.repository.pago_repository import PagoRepository
from mods.producto.repository.productos_repository import ProductoRepository
from mods.qr.repository.qr_repository import QRCodeRepository
from mods.timbrado.repository.timbrado_repository import TimbradoRepository


def initialize_db(db_path='facturacion.db'):
    """
    Initializes and returns a SQLite database connection, and creates all necessary tables.
    :param db_path: The path to the SQLite database file (default is 'facturacion.db').
    :return: SQLite connection object.
    """
    try:
        # Establish connection to the SQLite database
        connection = sqlite3.connect(db_path)
        print(f"Connected to database at {db_path}")

        # Initialize repositories
        entidad_repo = EntidadRepository(connection)
        timbrado_repo = TimbradoRepository(connection)
        factura_repo = FacturaRepository(connection)
        detalle_factura_repo = DetalleFacturaRepository(connection)
        impuesto_repo = ImpuestoRepository(connection)
        pago_repo = PagoRepository(connection)
        producto_repo = ProductoRepository(connection)
        qr_code_repo = QRCodeRepository(connection)

        # Create tables for all entities
        entidad_repo.create_table()
        timbrado_repo.create_table()
        factura_repo.create_table()
        detalle_factura_repo.create_table()
        impuesto_repo.create_table()
        pago_repo.create_table()
        producto_repo.create_table()
        qr_code_repo.create_table()

        print("All tables initialized successfully.")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database or initializing tables: {e}")
        return None


def close_db(connection):
    """
    Closes the database connection.
    :param connection: SQLite connection object to be closed.
    """
    if connection:
        connection.close()
        print("Database connection closed.")
