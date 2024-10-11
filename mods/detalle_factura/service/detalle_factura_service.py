from mods.detalle_factura.model.detalle_factura_entity import DetalleFactura
from mods.detalle_factura.repository.detalle_factura_repository import DetalleFacturaRepository


class DetalleFacturaService:
    def __init__(self, connection):
        self.repository = DetalleFacturaRepository(connection)

    def crear_tabla(self):
        self.repository.crear_tabla()

    def crear_detalle_factura(self, factura_id_med, producto_id_med, cantidad_med, precio_unitario_med, subtotal_med):
        detalle_factura = DetalleFactura(factura_id_med, producto_id_med, cantidad_med, precio_unitario_med,
                                         subtotal_med)
        self.repository.insertar(detalle_factura)

    def listar_detalles(self):
        return self.repository.listar_detalles()

    def listar_detalle_por_id(self, detalle_id):
        return self.repository.listar_detalle_por_id(detalle_id)

    def actualizar_detalle_factura(self, detalle_id, factura_id_med, producto_id_med, cantidad_med, precio_unitario_med,
                                   subtotal_med):
        detalle_factura = DetalleFactura(factura_id_med, producto_id_med, cantidad_med, precio_unitario_med,
                                         subtotal_med)
        self.repository.actualizar_detalle_factura(detalle_id, detalle_factura)

    def eliminar_detalle_factura(self, detalle_id):
        self.repository.eliminar_detalle_factura(detalle_id)
