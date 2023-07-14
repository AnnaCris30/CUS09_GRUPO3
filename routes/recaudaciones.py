from flask import Blueprint, render_template as rt, request, url_for, redirect
from flask import flash
from models.persona import Persona
from models.cuenta import Cuenta
from models.recaudacion import Recaudacion
from schemas.recaudacionSchema import RecaudacionSchema
from models.mantRecibo import MantRecibo
from flask import jsonify
from models.mantRecibo import MantRecibo
from schemas.mantReciboSchema import MantReciboSchema


bp = Blueprint('recaudaciones', __name__)

@bp.route('/', methods=['POST','GET'])
def recaudaciones():
    #Obtener todas las recaudaciones
    recaudaciones= Recaudacion.query.all()
    recibos = MantRecibo.query.all()
    # Serializar los objetos por medio de schemas
    recaudaciones_serializadas=RecaudacionSchema(many=True).dump(recaudaciones)
    recibos_serializados=MantReciboSchema(many=True).dump(recibos)
    
    return rt("recaudacion.html",recaudaciones=recaudaciones_serializadas, 
        recibos=recibos_serializados)
    
 
## ------------BUSCAR POR NUMERO DE DOCUMENTO---------------
@bp.route('/buscar', methods=['POST'])
def buscar_numDocumento():
    num_documento = request.form['num_documento']

    # Lógica para buscar el número de documento en la base de datos y obtener los valores correspondientes
    persona = Persona.query.filter_by(ndocumento=num_documento).first()
    
    if persona:
        # Si se encuentra el número de documento, obtener los valores correspondientes        
        nombres = persona.nombres
        id_persona=persona.id_persona
        cuenta = Cuenta.query.filter_by(id_persona=id_persona).first()  ##como la llave foranea
        banco=cuenta.banco.descripcion
        moneda = cuenta.tipo_moneda.descripcion
        ncuenta = cuenta.ncuenta
        
        # Devolver la respuesta al cliente en formato JSON con los valores obtenidos
        response = {
            'success': True,
            'data': {
                'nombres': nombres,
                'banco' : banco,
                'moneda' : moneda,
                'ncuenta': ncuenta
            }
        }
        return jsonify(response)
    else:
         
        # Si no se encuentra el número de documento, redirigir a la página inicial con un mensaje de error
        flash('Número de documento no encontrado', 'error')
        return redirect(url_for('recaudaciones'))



##------------BUSCAR POR NUMERO RECIBO---------------
@bp.route('/buscarRecibo', methods=['POST'])
def buscar_nroRecibo():
    num_recibo = request.form['num_recibo']

    # Lógica para buscar el número de recibo en la base de datos y obtener los valores correspondientes
    mantRecibo = MantRecibo.query.filter_by(n_recibo=num_recibo).first()
    
    if mantRecibo:
        # Si se encuentra el número de documento, obtener los valores correspondientes        
        recibo_estado = mantRecibo.recibo_estado.descripcion
        importe = mantRecibo.importe
        
        
        # Devolver la respuesta al cliente en formato JSON con los valores obtenidos
        response = {
            'success': True,
            'data': {
                'recibo_estado': recibo_estado,
                'importe' : importe
            }
        }
        return jsonify(response)
    else:
         
        # Si no se encuentra el número de documento, redirigir a la página inicial con un mensaje de error
        flash('Número de recibo no encontrado', 'error')
        return redirect(url_for('recaudaciones'))
      