from flask import Blueprint, render_template as rt, request, url_for, redirect
from models.persona import Persona
from models.recaudacion import Recaudacion
from schemas.recaudacionSchema import RecaudacionSchema
from flask import jsonify
bp = Blueprint('recaudaciones', __name__)

@bp.route('/', methods=['POST','GET'])
def recaudaciones():
    #Obtener todas las recaudaciones
    recaudaciones= Recaudacion.query.all()
    
    # Serializar los objetos por medio de schemas
    recaudaciones_serializadas=RecaudacionSchema(many=True).dump(recaudaciones)

    return rt("recaudacion.html",recaudaciones=recaudaciones_serializadas)
 
    

@bp.route('/buscar', methods=['POST'])
def buscar_numDocumento():
    num_documento = request.form['num_documento']

    # Lógica para buscar el número de documento en la base de datos y obtener los valores correspondientes
    persona = Persona.query.filter_by(ndocumento=num_documento).first()

    if persona:
        # Si se encuentra el número de documento, obtener los valores correspondientes
        nombres = persona.nombres
        # Devolver la respuesta al cliente en formato JSON con los valores obtenidos
        response = {
            'success': True,
            'data': {
                'nombres': nombres, 
            }
        }
        return jsonify(response)
    else:
        # Si no se encuentra el número de documento, devolver un mensaje de error al cliente
        response = {
            'success': False,
            'message': 'Número de documento no encontrado'
        }
        return jsonify(response)
