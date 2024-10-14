from mods.entidad.model.entidad_entity import Entidad
from mods.entidad.repository.entidad_repository import EntidadRepository


class EntidadService:
    def __init__(self, connection):
        self.repository = EntidadRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_entidad(self, nombre_med, tipo_med, ruc_med=None, direccion_med=None, telefono_med=None, email_med=None, cedula_med=None):
        entidad = Entidad(nombre_med, tipo_med, ruc_med, direccion_med, telefono_med, email_med, cedula_med)
        self.repository.insert(entidad)

    def get_all_entidades(self):
        return self.repository.get_all()

    def get_entidad_by_id(self, entidad_id_med):
        return self.repository.get_by_id(entidad_id_med)

    def update_entidad(self, entidad_id_med, nombre_med, tipo_med, ruc_med=None, direccion_med=None, telefono_med=None, email_med=None,
                       cedula_med=None):
        entidad = Entidad(nombre_med, tipo_med, ruc_med, direccion_med, telefono_med, email_med, cedula_med)
        self.repository.update(entidad_id_med, entidad)

    def delete_entidad(self, entidad_id_med):
        self.repository.delete(entidad_id_med)
