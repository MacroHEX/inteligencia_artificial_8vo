from mods.detalle_factura.model.detalle_factura_entity import DetalleFactura
from mods.detalle_factura.repository.detalle_factura_repository import DetalleFacturaRepository


class DetalleFacturaService:
    def __init__(self, connection):
        self.repository = DetalleFacturaRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_detalle_factura(self, factura_id, producto_id, cantidad, precio_unitario, subtotal):
        detalle_factura = DetalleFactura(factura_id, producto_id, cantidad, precio_unitario, subtotal)
        self.repository.insert(detalle_factura)

    def get_all_detalles(self):
        return self.repository.get_all()

    def get_detalle_by_id(self, detalle_id):
        return self.repository.get_by_id(detalle_id)

    def update_detalle_factura(self, detalle_id, factura_id, producto_id, cantidad, precio_unitario, subtotal):
        detalle_factura = DetalleFactura(factura_id, producto_id, cantidad, precio_unitario, subtotal)
        self.repository.update(detalle_id, detalle_factura)

    def delete_detalle_factura(self, detalle_id):
        self.repository.delete(detalle_id)
