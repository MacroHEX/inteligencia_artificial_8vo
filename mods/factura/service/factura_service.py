from mods.factura.model.factura_entity import Factura
from mods.factura.repository.factura_repository import FacturaRepository


class FacturaService:
    def __init__(self, connection):
        self.repository = FacturaRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_factura(self, fecha_emision, entidad_id, timbrado_id, total, estado):
        factura = Factura(fecha_emision, entidad_id, timbrado_id, total, estado)
        self.repository.insert(factura)

    def get_all_facturas(self):
        return self.repository.get_all()

    def get_factura_by_id(self, factura_id):
        return self.repository.get_by_id(factura_id)

    def update_factura(self, factura_id, fecha_emision, entidad_id, timbrado_id, total, estado):
        factura = Factura(fecha_emision, entidad_id, timbrado_id, total, estado)
        self.repository.update(factura_id, factura)

    def delete_factura(self, factura_id):
        self.repository.delete(factura_id)
