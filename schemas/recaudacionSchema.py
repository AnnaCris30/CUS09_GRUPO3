from marshmallow import Schema, fields
from schemas.estadoRecaudacionSchema import EstadoRecaudacionSchema
from schemas.tipoMonedaSchema import TipoMonedaSchema

class RecaudacionSchema(Schema):
    id_tipo_moneda  = fields.Integer()
    fecha_operacion = fields.Integer()
    importe = fields.Integer()
    id_recaudacion_estado = fields.Integer()


    tipo_moneda = fields.Nested(TipoMonedaSchema)
    recaudacion_estado = fields.Nested(EstadoRecaudacionSchema)