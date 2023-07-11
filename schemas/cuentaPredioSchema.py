
from marshmallow import Schema, fields
from schemas.predioSchema import PredioSchema
from schemas.estadoSchema import EstadoSchema
from schemas.tipoAutorizacionSchema import TipoAutorizacionSchema
from schemas.tipoMonedaSchema import TipoMonedaSchema
from schemas.bancoSchema import BancoSchema
class CuentaPredioSchema(Schema):

        id_cuenta_predio  = fields.Integer()
        id_predio = fields.Integer()
        id_estado = fields.Integer()
        id_tipo_autorizacion = fields.Integer()
        id_banco = fields.Integer()
        id_tipo_moneda = fields.Integer()
        ncuenta = fields.Integer()
        ntarjeta = fields.Integer()
        fecha_apertura = fields.Date()
        fecha_autorizacion = fields.Date()
        fecha_cierre = fields.Date()
        correo_autorizado = fields.String()

        predio = fields.Nested(PredioSchema)
        estado = fields.Nested(EstadoSchema)
        tipo_autorizacion = fields.Nested(TipoAutorizacionSchema)
        banco = fields.Nested(BancoSchema)
        tipo_moneda = fields.Nested(TipoMonedaSchema)