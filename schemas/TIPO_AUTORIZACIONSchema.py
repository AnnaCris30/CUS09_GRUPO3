from marshmallow import Schema, fields

class TipoAutorizacionSchema(Schema):
    id_tipo_autorizacion = fields.Integer()
    descripcion = fields.String()