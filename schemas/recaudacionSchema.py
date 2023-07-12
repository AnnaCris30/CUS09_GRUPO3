from marshmallow import Schema, fields
from schemas.estadoRecaudacionSchema import EstadoRecaudacionSchema
from schemas.tipoMonedaSchema import TipoMonedaSchema
from schemas.cuentaSchema import CuentaSchema
from schemas.mantReciboSchema import MantReciboSchema
from schemas.cuentaPredioSchema import CuentaPredioSchema

class RecaudacionSchema(Schema):
    id_recaudacion = fields.Integer()
    id_cuenta = fields.Integer()
    id_mant_recibo = fields.Integer()
    n_operacion = fields.Number()
    importe = fields.Number()
    id_tipo_moneda  = fields.Integer()
    fecha_operacion = fields.Date()
    importe = fields.Integer()
    id_recaudacion_estado = fields.Integer()
    id_cuenta_predio = fields.Integer()
    observacion = fields.String()

    cuenta = fields.Nested(CuentaSchema)
    tipo_moneda = fields.Nested(TipoMonedaSchema)
    recaudacion_estado = fields.Nested(EstadoRecaudacionSchema)
    mant_recibo = fields.Nested(MantReciboSchema) 
    cuenta_predio = fields.Nested(CuentaPredioSchema)
