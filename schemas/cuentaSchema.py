from marshmallow import Schema, fields
from schemas.personaSchema import PersonaSchema
from schemas.bancoSchema import BancoSchema
from schemas.tipoMonedaSchema import TipoMonedaSchema


class CuentaSchema(Schema):
    id_cuenta = fields.Integer()
    id_persona = fields.Integer()
    id_banco = fields.Integer()
    id_tipo_moneda = fields.Integer()
    ncuenta = fields.Integer()

    persona = fields.Nested(PersonaSchema)
    banco = fields.Nested(BancoSchema)
    tipo_moneda = fields.Nested(TipoMonedaSchema)