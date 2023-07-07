from marshmallow import Schema, fields

class EstadoRecaudacionSchema(Schema):
    id_estado = fields.Integer()
    descripcion = fields.String()
