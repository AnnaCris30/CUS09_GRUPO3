from utils.db import db

class MantRecibo(db.Model):
    id_mant_recibo = db.Column(db.Integer, primary_key=True)
    id_casa = db.Column(db.Integer, db.ForeignKey('casa.id_casa'))
    n_recibo = db.Column(db.String(8))
    periodo = db.Column(db.String(8))
    fecha_emision = db.Column(db.Date)
    fecha_vencimiento = db.Column(db.Date)
    importe = db.Column(db.DECIMAL)
    ajuste = db.Column(db.DECIMAL(6, 2))
    observacion = db.Column(db.String(100))
    id_recibo_estado = db.Column(db.Integer, db.ForeignKey('recibo_estado.id_recibo_estado'))

    casa = db.relationship('Casa', backref='mantRecibo')
    recibo_estado = db.relationship('ReciboEstado', backref='mantRecibo')

    def __init__(self, id_casa, id_predio, id_estado, numero, piso,
                 area,participacion):
        self.id_casa = id_casa
        self.id_predio = id_predio
        self.id_estado = id_estado
        self.numero = numero
        self.piso = piso
        self.area = area
        self.participacion = participacion