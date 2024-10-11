from mods.producto.model.producto_entity import Producto
from mods.producto.repository.producto_repository import ProductoRepository


class ProductoService:
    def __init__(self, connection):
        self.repository = ProductoRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_producto(self, codigo_interno_med, nombre_med, descripcion_med, precio_med, stock_med):
        producto = Producto(codigo_interno_med, nombre_med, descripcion_med, precio_med, stock_med)
        self.repository.insert(producto)

    def get_all_productos(self):
        return self.repository.get_all()

    def get_producto_by_id(self, producto_id_med):
        return self.repository.get_by_id(producto_id_med)

    def update_producto(self, producto_id_med, codigo_interno_med, nombre_med, descripcion_med, precio_med, stock_med):
        producto = Producto(codigo_interno_med, nombre_med, descripcion_med, precio_med, stock_med)
        self.repository.update(producto_id_med, producto)

    def delete_producto(self, producto_id_med):
        self.repository.delete(producto_id_med)
