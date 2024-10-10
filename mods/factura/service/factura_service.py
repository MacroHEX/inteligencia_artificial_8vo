from mods.detalle_factura.service.detalle_factura_service import DetalleFacturaService
from mods.factura.model.factura_entity import Factura
from mods.factura.repository.factura_repository import FacturaRepository
from mods.timbrado.service.timbrado_service import TimbradoService


class FacturaService:
    def __init__(self, connection):
        self.detalle_factura_service = DetalleFacturaService(connection)
        self.repository = FacturaRepository(connection)
        self.timbrado_service = TimbradoService(connection)
        self.connection = connection  # Store the connection for transaction handling

    def create_table(self):
        self.repository.create_table()

    def create_factura_with_detalles(self, factura, detalles):
        """Creates a factura and its detalles in a single transaction."""
        try:
            # Start a transaction
            with self.connection:
                # Increment nro_documento for timbrado
                nro_documento = self.timbrado_service.increment_nro_documento(factura.timbrado_id)

                # Create the factura and get the factura_id
                factura_id = self.repository.insert(factura)

                # Now create each detalle_factura using the generated factura_id
                for detalle in detalles:
                    detalle.factura_id = factura_id  # Ensure that factura_id is assigned
                    self.detalle_factura_service.create_detalle_factura(
                        factura_id, detalle.producto_id, detalle.cantidad, detalle.precio_unitario, detalle.subtotal
                    )
            return factura_id
        except Exception as e:
            print(f"Error during transaction: {e}")
            raise

    def get_all_facturas(self):
        return self.repository.get_all()

    def get_factura_by_id(self, factura_id):
        return self.repository.get_by_id(factura_id)

    def update_factura(self, factura_id, fecha_emision, entidad_id, timbrado_id, total, estado):
        factura = Factura(fecha_emision, entidad_id, timbrado_id, total, estado)
        self.repository.update(factura_id, factura)

    def delete_factura(self, factura_id):
        self.repository.delete(factura_id)
