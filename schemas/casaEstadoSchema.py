from marshmallow import Schema, fields

class CasaEstadoSchema(Schema):
    id_estado = fields.Integer()
    descripcion = fields.String()