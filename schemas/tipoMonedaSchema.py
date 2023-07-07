from marshmallow import Schema, fields

class TipoMonedaSchema(Schema):
    id_tipo_moneda = fields.Integer()
    descripcion = fields.String()
    etiqueta = fields.String()