from utils.db import db
class TipoPredio(db.Model):
    id_tipo_autorizacion = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))

    def __init__(self, id_tipo_autorizacion, descripcion ):
        self.id_tipo_autorizacion = id_tipo_autorizacion
        self.descripcion  = descripcion 