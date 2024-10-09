class Factura:
    def __init__(self, fecha_emision, entidad_id, timbrado_id, total, estado):
        self.fecha_emision = fecha_emision
        self.entidad_id = entidad_id
        self.timbrado_id = timbrado_id
        self.total = total
        self.estado = estado
