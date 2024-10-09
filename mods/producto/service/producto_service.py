from mods.producto.model.productos_entity import Producto
from mods.producto.repository.productos_repository import ProductoRepository


class ProductoService:
    def __init__(self, connection):
        self.repository = ProductoRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_producto(self, codigo_interno, nombre, descripcion, precio, stock):
        producto = Producto(codigo_interno, nombre, descripcion, precio, stock)
        self.repository.insert(producto)

    def get_all_productos(self):
        return self.repository.get_all()

    def get_producto_by_id(self, producto_id):
        return self.repository.get_by_id(producto_id)

    def update_producto(self, producto_id, codigo_interno, nombre, descripcion, precio, stock):
        producto = Producto(codigo_interno, nombre, descripcion, precio, stock)
        self.repository.update(producto_id, producto)

    def delete_producto(self, producto_id):
        self.repository.delete(producto_id)
