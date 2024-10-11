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
                nro_documento = self.timbrado_service.increment_nro_documento(factura.timbrado_id_med)

                # Create the factura and get the factura_id_med
                factura_id_med = self.repository.insert(factura)

                # Now create each detalle_factura using the generated factura_id_med
                for detalle in detalles:
                    detalle.factura_id_med = factura_id_med  # Ensure that factura_id_med is assigned
                    self.detalle_factura_service.crear_detalle_factura(
                        factura_id_med, detalle.producto_id_med, detalle.cantidad_med, detalle.precio_unitario_med, detalle.subtotal_med
                    )
            return factura_id_med
        except Exception as e:
            print(f"Error during transaction: {e}")
            raise

    def get_all_facturas(self):
        return self.repository.get_all()

    def get_factura_by_id(self, factura_id_med):
        return self.repository.get_by_id(factura_id_med)

    def update_factura(self, factura_id_med, fecha_emision_med, entidad_id_med, timbrado_id_med, total_med, estado_med):
        factura = Factura(fecha_emision_med, entidad_id_med, timbrado_id_med, total_med, estado_med)
        self.repository.update(factura_id_med, factura)

    def delete_factura(self, factura_id_med):
        self.repository.delete(factura_id_med)
