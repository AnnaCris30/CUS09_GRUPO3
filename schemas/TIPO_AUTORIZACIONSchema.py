from marshmallow import Schema, fields

class TIPO_AUTORIZACIONSchema(Schema):
    id_tipo_autorizacion = fields.Integer()
    descripcion = fields.String()