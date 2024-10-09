from mods.entidad.model.entidad_entity import Entidad
from mods.entidad.repository.entidad_repository import EntidadRepository


class EntidadService:
    def __init__(self, connection):
        self.repository = EntidadRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_entidad(self, nombre, tipo, ruc=None, direccion=None, telefono=None, email=None, cedula=None):
        entidad = Entidad(nombre, tipo, ruc, direccion, telefono, email, cedula)
        self.repository.insert(entidad)

    def get_all_entidades(self):
        return self.repository.get_all()

    def get_entidad_by_id(self, entidad_id):
        return self.repository.get_by_id(entidad_id)

    def update_entidad(self, entidad_id, nombre, tipo, ruc=None, direccion=None, telefono=None, email=None,
                       cedula=None):
        entidad = Entidad(nombre, tipo, ruc, direccion, telefono, email, cedula)
        self.repository.update(entidad_id, entidad)

    def delete_entidad(self, entidad_id):
        self.repository.delete(entidad_id)
