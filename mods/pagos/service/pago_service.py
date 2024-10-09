from mods.pagos.model.pago_entity import Pago
from mods.pagos.repository.pago_repository import PagoRepository


class PagoService:
    def __init__(self, connection):
        self.repository = PagoRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_pago(self, factura_id, fecha_pago, monto, metodo_pago):
        pago = Pago(factura_id, fecha_pago, monto, metodo_pago)
        self.repository.insert(pago)

    def get_all_pagos(self):
        return self.repository.get_all()

    def get_pago_by_id(self, pago_id):
        return self.repository.get_by_id(pago_id)

    def update_pago(self, pago_id, factura_id, fecha_pago, monto, metodo_pago):
        pago = Pago(factura_id, fecha_pago, monto, metodo_pago)
        self.repository.update(pago_id, pago)

    def delete_pago(self, pago_id):
        self.repository.delete(pago_id)
