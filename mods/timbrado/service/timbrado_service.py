from mods.timbrado.model.timbrado_entity import Timbrado
from mods.timbrado.repository.timbrado_repository import TimbradoRepository


class TimbradoService:
    def __init__(self, connection):
        self.repository = TimbradoRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_timbrado(self, tipo_de_documento, numero_timbrado, establecimiento, punto_expedicion, numero_documento,
                        fecha_inicio):
        timbrado = Timbrado(tipo_de_documento, numero_timbrado, establecimiento, punto_expedicion, numero_documento,
                            fecha_inicio)
        self.repository.insert(timbrado)

    def get_all_timbrados(self):
        return self.repository.get_all()

    def get_timbrado_by_id(self, timbrado_id):
        return self.repository.get_by_id(timbrado_id)

    def update_timbrado(self, timbrado_id, tipo_de_documento, numero_timbrado, establecimiento, punto_expedicion,
                        numero_documento, fecha_inicio):
        timbrado = Timbrado(tipo_de_documento, numero_timbrado, establecimiento, punto_expedicion, numero_documento,
                            fecha_inicio)
        self.repository.update(timbrado_id, timbrado)

    def delete_timbrado(self, timbrado_id):
        self.repository.delete(timbrado_id)
