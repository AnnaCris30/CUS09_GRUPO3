from utils.db import db

class Casa(db.Model):
    id_casa = db.Column(db.Integer, primary_key=True)
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'))
    id_estado = db.Column(db.Integer, db.ForeignKey('casa_estado.id_estado'))
    numero = db.Column(db.Integer)
    piso = db.Column(db.Integer)
    area = db.Column(db.DECIMAL)
    participacion = db.Column(db.DECIMAL(6, 2))
  

    predio = db.relationship('Predio', backref='casa')
    casa_estado = db.relationship('CasaEstado', backref='casa')

    def __init__(self, id_casa, id_predio, id_estado, numero, piso,
                 area,participacion):
        self.id_casa = id_casa
        self.id_predio = id_predio
        self.id_estado = id_estado
        self.numero = numero
        self.piso = piso
        self.area = area
        self.participacion = participacion