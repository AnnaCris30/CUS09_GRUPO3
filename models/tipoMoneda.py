from utils.db import db

class TipoMoneda(db.Model):
    id_tipo_moneda = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(10))
    etiqueta = db.Column(db.String(4))
    
    def __init__(self, id_banco, descripcion):
        self.id_banco = id_banco
        self.descripcion = descripcion