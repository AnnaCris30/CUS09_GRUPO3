from marshmallow import Schema, fields
from schemas.casaSchema import CasaSchema
from schemas.reciboEstadoSchema import ReciboEstadoSchema


class MantReciboSchema(Schema):
    id_mant_recibo = fields.Integer()
    id_casa = fields.Integer()
    n_recibo = fields.String()
    periodo = fields.String()
    fecha_emision = fields.Date()
    fecha_vencimiento = fields.Date()
    importe = fields.Decimal()
    ajuste = fields.Decimal()
    observacion = fields.String()
    id_recibo_estado = fields.Integer()
    
    casa = fields.Nested(CasaSchema)
    recibo_estado = fields.Nested(ReciboEstadoSchema)