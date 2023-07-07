from marshmallow import Schema, fields

class ReciboEstadoSchema(Schema):
    id_recibo_estado = fields.Integer()
    descripcion = fields.String()