from mods.timbrado.model.timbrado_entity import Timbrado
from mods.timbrado.repository.timbrado_repository import TimbradoRepository


class TimbradoService:
    def __init__(self, connection):
        self.repository = TimbradoRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_timbrado(self, tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med, numero_documento_med,
                        fecha_inicio_med):
        timbrado = Timbrado(tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med, numero_documento_med,
                            fecha_inicio_med)
        self.repository.insert(timbrado)

    def get_all_timbrados(self):
        return self.repository.get_all()

    def get_timbrado_by_id(self, timbrado_id_med):
        """Fetch timbrado by its ID."""
        return self.repository.get_by_id(timbrado_id_med)

    def get_timbrado_by_numero(self, numero_timbrado_med):
        """Fetch a timbrado by its numero_timbrado_med."""
        cursor = self.repository.connection.execute('SELECT * FROM timbrado WHERE numero_timbrado_med = ?',
                                                    (numero_timbrado_med,))
        return cursor.fetchone()

    def update_timbrado(self, timbrado_id_med, tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med,
                        numero_documento_med, fecha_inicio_med):
        timbrado = Timbrado(tipo_de_documento_med, numero_timbrado_med, establecimiento_med, punto_expedicion_med, numero_documento_med,
                            fecha_inicio_med)
        self.repository.update(
            timbrado_id_med,
            timbrado.tipo_de_documento_med,
            timbrado.numero_timbrado_med,
            timbrado.establecimiento_med,
            timbrado.punto_expedicion_med,
            timbrado.numero_documento_med,
            timbrado.fecha_inicio_med
        )

    def delete_timbrado(self, timbrado_id_med):
        self.repository.delete(timbrado_id_med)

    def increment_nro_documento(self, timbrado_id_med):
        """Increment `numero_documento_med` for the given timbrado."""
        timbrado = self.get_timbrado_by_id(timbrado_id_med)
        if timbrado:
            nuevo_numero_documento = int(timbrado[5]) + 1  # `numero_documento_med` is at index 5
            self.repository.update(
                timbrado_id_med,
                timbrado[1],  # tipo_de_documento_med
                timbrado[2],  # numero_timbrado_med
                timbrado[3],  # establecimiento_med
                timbrado[4],  # punto_expedicion_med
                nuevo_numero_documento,  # Incremented numero_documento_med
                timbrado[6]  # fecha_inicio_med
            )
            return nuevo_numero_documento
        else:
            raise Exception(f"Timbrado with ID {timbrado_id_med} not found.")
