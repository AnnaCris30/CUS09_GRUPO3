from marshmallow import Schema, fields
from schemas.predioSchema import PredioSchema
from schemas.casaEstadoSchema import CasaEstadoSchema


class CasaSchema(Schema):
    id_casa = fields.Integer()
    id_predio = fields.Integer()
    id_estado = fields.Integer()
    numero = fields.Integer()
    piso = fields.Integer()
    area = fields.Decimal()
    participacion = fields.Decimal()
    
    predio = fields.Nested(PredioSchema)
    casa_estado = fields.Nested(CasaEstadoSchema)