from marshmallow import Schema, fields

class EstadoRecaudacionSchema(Schema):
    id_recaudacion_estado = fields.Integer()
    descripcion = fields.String()
