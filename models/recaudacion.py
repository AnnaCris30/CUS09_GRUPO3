from utils.db import db

class Recaudacion(db.Model):
    fecha_operacion= db.Column(db.Date)
    importe = db.Column(db.Double)
    id_tipo_moneda = db.Column(db.Integer, db.ForeignKey('tipo_moneda.id_tipo_moneda'))
    id_recaudacion_estado = db.Column(db.String(150), db.ForeignKey('recaudacion_estado.id_recaudacion_estado'))

    tipo_moneda = db.relationship('TipoMoneda', backref='recaudacion')
    recaudacion_estado = db.relationship('EstadoRecaudacion', backref='recaudacion')
    
    def __init__(self,fecha_operacion, id_tipo_moneda, importe,id_recaudacion_estado):
        self.fecha_operacion= fecha_operacion
        self.id_tipo_moneda = id_tipo_moneda
        self.importe = importe
        self.id_recaudacion_estado = id_recaudacion_estado
