import sqlite3

from mods.detalle_factura.repository.detalle_factura_repository import DetalleFacturaRepository
from mods.entidad.repository.entidad_repository import EntidadRepository
from mods.factura.repository.factura_repository import FacturaRepository
from mods.producto.repository.producto_repository import ProductoRepository
from mods.timbrado.repository.timbrado_repository import TimbradoRepository


def initialize_db(db_path='facturacion.db'):
    """
    Inicializa y devuelve una conexión a una base de datos SQLite, y crea todas las tablas necesarias.
    :param db_path: La ruta al fichero de base de datos SQLite (por defecto es 'facturacion.db').
    :return: Objeto de conexión SQLite.
    """
    try:
        # Establish connection to the SQLite database
        connection = sqlite3.connect(db_path)
        print(f"Conectado a la base de datos: {db_path}")

        # Initialize repositories
        entidad_repo = EntidadRepository(connection)
        timbrado_repo = TimbradoRepository(connection)
        factura_repo = FacturaRepository(connection)
        detalle_factura_repo = DetalleFacturaRepository(connection)
        producto_repo = ProductoRepository(connection)

        # Create tables for all entities
        entidad_repo.create_table()
        timbrado_repo.create_table()
        factura_repo.create_table()
        detalle_factura_repo.crear_tabla()
        producto_repo.create_table()

        print("Todas las tablas fueron inicializadas con éxito")
        return connection
    except sqlite3.Error as e:
        print(f"Error de conexión o al inicializar las tablas: {e}")
        return None


def close_db(connection):
    """
     Cierra la conexión a la base de datos.
    :param connection: Objeto de conexión SQLite a cerrar.
    """
    if connection:
        connection.close()
        print("Conexión a la base de datos cerrada")
