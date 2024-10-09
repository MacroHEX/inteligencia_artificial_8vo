from mods.impuesto.model.impuesto_entity import Impuesto
from mods.impuesto.repository.impuesto_repository import ImpuestoRepository


class ImpuestoService:
    def __init__(self, connection):
        self.repository = ImpuestoRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_impuesto(self, nombre, porcentaje):
        impuesto = Impuesto(nombre, porcentaje)
        self.repository.insert(impuesto)

    def get_all_impuestos(self):
        return self.repository.get_all()

    def get_impuesto_by_id(self, impuesto_id):
        return self.repository.get_by_id(impuesto_id)

    def update_impuesto(self, impuesto_id, nombre, porcentaje):
        impuesto = Impuesto(nombre, porcentaje)
        self.repository.update(impuesto_id, impuesto)

    def delete_impuesto(self, impuesto_id):
        self.repository.delete(impuesto_id)
