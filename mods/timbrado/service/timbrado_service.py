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
        """Fetch timbrado by its ID."""
        return self.repository.get_by_id(timbrado_id)

    def get_timbrado_by_numero(self, numero_timbrado):
        """Fetch a timbrado by its numero_timbrado."""
        cursor = self.repository.connection.execute('SELECT * FROM timbrado WHERE numero_timbrado = ?',
                                                    (numero_timbrado,))
        return cursor.fetchone()

    def update_timbrado(self, timbrado_id, tipo_de_documento, numero_timbrado, establecimiento, punto_expedicion,
                        numero_documento, fecha_inicio):
        timbrado = Timbrado(tipo_de_documento, numero_timbrado, establecimiento, punto_expedicion, numero_documento,
                            fecha_inicio)
        self.repository.update(
            timbrado_id,
            timbrado.tipo_de_documento,
            timbrado.numero_timbrado,
            timbrado.establecimiento,
            timbrado.punto_expedicion,
            timbrado.numero_documento,
            timbrado.fecha_inicio
        )

    def delete_timbrado(self, timbrado_id):
        self.repository.delete(timbrado_id)

    def increment_nro_documento(self, timbrado_id):
        """Increment `numero_documento` for the given timbrado."""
        timbrado = self.get_timbrado_by_id(timbrado_id)
        if timbrado:
            nuevo_numero_documento = int(timbrado[5]) + 1  # `numero_documento` is at index 5
            self.repository.update(
                timbrado_id,
                timbrado[1],  # tipo_de_documento
                timbrado[2],  # numero_timbrado
                timbrado[3],  # establecimiento
                timbrado[4],  # punto_expedicion
                nuevo_numero_documento,  # Incremented numero_documento
                timbrado[6]  # fecha_inicio
            )
            return nuevo_numero_documento
        else:
            raise Exception(f"Timbrado with ID {timbrado_id} not found.")
