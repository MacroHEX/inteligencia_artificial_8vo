from mods.qr.model.qr_entity import QRCode
from mods.qr.repository.qr_repository import QRCodeRepository


class QRCodeService:
    def __init__(self, connection):
        self.repository = QRCodeRepository(connection)

    def create_table(self):
        self.repository.create_table()

    def create_qr_code(self, factura_id, qr_url):
        qr_code = QRCode(factura_id, qr_url)
        self.repository.insert(qr_code)

    def get_all_qr_codes(self):
        return self.repository.get_all()

    def get_qr_code_by_id(self, qr_code_id):
        return self.repository.get_by_id(qr_code_id)

    def update_qr_code(self, qr_code_id, factura_id, qr_url):
        qr_code = QRCode(factura_id, qr_url)
        self.repository.update(qr_code_id, qr_code)

    def delete_qr_code(self, qr_code_id):
        self.repository.delete(qr_code_id)
