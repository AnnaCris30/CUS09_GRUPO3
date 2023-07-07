from marshmallow import Schema, fields

class BancoSchema(Schema):
    id_banco = fields.Integer()
    descripcion = fields.String()
