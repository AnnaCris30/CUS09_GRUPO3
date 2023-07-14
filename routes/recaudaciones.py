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
from models.predio import Predio
from models.cuentaPredio import CuentaPredio  
from utils.db import db

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
@bp.route('/buscar/<string:num_documento>', methods=['POST'])
def buscar_numDocumento(num_documento):
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

##------------BUSCAR POR RUC--------------
@bp.route('/buscarpredio', methods=['POST'])
def buscar_numRuc():
    num_ruc= request.form['num_ruc']

    # Lógica para buscar el número de documento en la base de datos y obtener los valores correspondientes
    predio = Predio.query.filter_by(ruc=num_ruc).first()
    
    if predio:
        # Si se encuentra el número de documento, obtener los valores correspondientes        
        descripcion = predio.descripcion
        direccion = predio.direccion
        tipo_predio = predio.tipo_predio.nomre_predio
        id_predio=predio.id_predio
        cuenta_predio = CuentaPredio.query.filter_by(id_predio=id_predio).first()
        ncuenta=cuenta_predio.ncuenta
        tipo_autorizacion=cuenta_predio.tipo_autorizacion.descripcion
        estado=cuenta_predio.estado.descripcion
        
        # Devolver la respuesta al cliente en formato JSON con los valores obtenidos
        response = {
            'success': True,
            'data': {
                'descripcion': descripcion,
                'direccion' : direccion,
                'tipo_predio' : tipo_predio,
                'ncuenta': ncuenta,
                'tipo_autorizacion': tipo_autorizacion,
                'estado': estado,
            }
        }
        return jsonify(response)
    else:
         
        # Si no se encuentra el número de documento, redirigir a la página inicial con un mensaje de error
        flash('Número de ruc no encontrado', 'error')
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

@bp.route('/editar/<int:id_recaudacion>', methods=['GET', 'POST'])
def editar_recaudacion(id_recaudacion):
    recaudacion = Recaudacion.query.get(id_recaudacion)

    if request.method == 'POST':
        # Obtener los datos actualizados del formulario
        # y actualizar la recaudación en la base de datos
        
        recaudacion.fecha_operacion = request.form['fecha-operacion-input']       
        recaudacion.id_recaudacion_estado = request.form['EstadoR-input']        
        recaudacion.observacion = request.form['observacion-input']

        # Guardar los cambios en la base de datos
        db.session.commit()

        # Redirigir a la página principal de recaudaciones
        return redirect(url_for('recaudaciones.recaudaciones'))

    # Renderizar la plantilla de edición con los datos de la recaudación
    return rt("editar_recaudacion.html", recaudacion=recaudacion)

@bp.route('/eliminar/<int:id_recaudacion>', methods=['GET', 'POST'])
def eliminar_recaudacion(id_recaudacion):
    recaudacion = Recaudacion.query.get(id_recaudacion)

    if request.method == 'POST':
        # Eliminar la recaudación de la base de datos
        db.session.delete(recaudacion)
        db.session.commit()

        # Redirigir a la página principal de recaudaciones
        return redirect(url_for('recaudaciones.recaudaciones'))

    # Renderizar la plantilla de confirmación de eliminación
    return rt("eliminar_recaudacion.html", recaudacion=recaudacion)

@bp.route('/agregar', methods=['POST'])
def agregar_datos():
    num_cuenta = request.form['num_cuenta']
    num_recibo = request.form['num_recibo']
    num_cuentaPredio = request.form['num_cuentaPredio']
    # Obtener los datos enviados desde el formulario
    n_operacion = request.form['n_operacion']
    fecha_operacion = request.form['fech_operacion']
    tipo_moneda = request.form['tipo_moneda']
    importe = request.form['importe']
    id_recaudacion_estado = request.form['id_recaudacion_estado']
    observacion= request.form['observacion']

    cuenta = Cuenta.query.filter_by(ncuenta=num_cuenta).first()
    recibo = MantRecibo.query.filter_by( n_recibo=num_recibo).first()
    cuentaPredio = CuentaPredio.query.filter_by(ncuenta=num_cuentaPredio).first()
    # Crear un nuevo o
    # bjeto en la base de datos con los datos proporcionados
    recaudacion = Recaudacion(
        id_cuenta=cuenta.id_cuenta,
        id_mant_recibo=recibo.id_mant_recibo ,
        n_operacion=n_operacion, 
        fecha_operacion=fecha_operacion,
        id_tipo_moneda=tipo_moneda,
        importe=importe,
        id_recaudacion_estado=id_recaudacion_estado,
        id_cuenta_predio=cuentaPredio.id_cuenta_predio,
        observacion=observacion
    )
    db.session.add(recaudacion)
    db.session.commit()
    
    #Devolver una respuesta de éxito al cliente

    response = {
        'success': True,
        'message': 'Datos agregados correctamente'
    }
    return jsonify(response)