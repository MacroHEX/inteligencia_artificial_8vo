class DetalleFactura:
    def __init__(self, factura_id, producto_id, cantidad, precio_unitario, subtotal):
        self.factura_id = factura_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal
