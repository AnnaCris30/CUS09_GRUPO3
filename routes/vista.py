
from flask import Blueprint, render_template as rt, flash, redirect, url_for, request, jsonify
from models.banco import banco
from models.casa import Casa
from models.casaEstado import casaEstado
from models.cuentaPredio import CuentaPredio
from models.estado import estado
from models.estadoRecaudacion import estadoRecaudacion
from models.mantRecibo import mantRecibo
from models.persona import persona
from models.predio import predio
from models.recaudacion import recaudacion
from models.reciboEstado import reciboEstado
from models.tipoAutorizacion import tipoAutorizacion
from models.tipoDocumento import tipoDocumento
from models.tipoMoneda import tipoMoneda
from models.tipoPredio import tipoPredio
from models.ubigeo import ubigeo

from utils.db import db
from utils.json import model_to_dict

bp = Blueprint('vista', __name__, url_prefix="/vista")

@bp.route('/')
def vista(): #esta función debe coincidir con el url_for del html (base)
    banco =banco.query.all()
    casa =casa.query.all()
    casaEstado=casaEstado.all()
    cuenta = cuenta.query.all()
    cuentaPredio=cuentaPredio.query.all()
    estado =estado.query.all()
    estadoRecaudacion =estadoRecaudacion.query.all()
    mantRecibo =mantRecibo.query.all()
    persona =persona.query.all()
    predio =predio.query.all()
    recaudacion =recaudacion.query.all()
    reciboEstado =reciboEstado.query.all()
    tipoAutorizacion =tipoAutorizacion.query.all()
    tipoDocumento =tipoDocumento.query.all()
    tipoMoneda =tipoMoneda.query.all()
    tipoPredio =tipoPredio.query.all()
    ubigeo =ubigeo.query.all()

    data_banco = []
    data_casa = []
    data_casaEstado = []
    data_cuenta = []
    data_cuentaPredio = []
    data_estado = []
    data_estadoRecaudacion = []
    data_mantRecibo = []
    data_persona = []
    data_predio =[]
    data_recaudacion = []
    data_reciboEstado = []
    data_tipoAutorizacion = []
    data_tipoDocumento = []
    data_tipoMoneda =[]
    data_tipoPredio = []
    data_ubigeo = []

    for obj in banco:
        x = model_to_dict(obj)
        data_banco.append(x)
    for obj in casa:
        x = model_to_dict(obj)
        data_casa.append(x)
    for obj in casaEstado:
        x = model_to_dict(obj)
        data_casaEstado.append(x)
    for obj in cuenta:
        x = model_to_dict(obj)
        data_cuenta.append(x)
    for obj in cuentaPredio:
        x = model_to_dict(obj)
        data_cuentaPredio.append(x)
    for obj in estado:
        x = model_to_dict(obj)
        data_estado.append(x)
    for obj in estadoRecaudacion:
        x = model_to_dict(obj)
        data_estadoRecaudacion.append(x)
    for obj in mantRecibo:
        x = model_to_dict(obj)
        data_mantRecibo.append(x)
    for obj in persona:
        x = model_to_dict(obj)
        data_persona.append(x)
    for obj in predio:
        x = model_to_dict(obj)
        data_predio.append(x)
    for obj in recaudacion:
        x = model_to_dict(obj)
        data_recaudacion.append(x)
    for obj in reciboEstado:
        x = model_to_dict(obj)
        data_reciboEstado.append(x)
    for obj in tipoAutorizacion:
        x = model_to_dict(obj)
        data_tipoAutorizacion.append(x)
    for obj in tipoDocumento:
        x = model_to_dict(obj)
        data_tipoDocumento.append(x)
    for obj in tipoMoneda:
        x = model_to_dict(obj)
        data_tipoMoneda.append(x)
    for obj in tipoPredio:
        x = model_to_dict(obj)
        data_tipoPredio.append(x)
    for obj in ubigeo:
        x=model_to_dict(obj)
        data_ubigeo.append(x)
    
    result = {
        'banco': data_banco,
        'casa': data_casa,
        'casaEstado': data_casaEstado,
        'cuenta': data_cuenta,
        'cuentaPredio': data_cuentaPredio,
        'estado': data_estado,
        'estadoRecaudacion': data_estadoRecaudacion,
        'mantRecibo': data_mantRecibo,
        'persona':data_persona,
        'predio':data_predio,
        'recaudacion':data_recaudacion,
        'reciboEstado':data_reciboEstado,
        'tipoAutorizacion': data_tipoAutorizacion,
        'tipoDocumento': data_tipoDocumento,
        'tipoMoneda':data_tipoMoneda,
        'tipoPredio': data_tipoPredio,
        'ubigeo': data_ubigeo
    }

    return jsonify(result)

@bp.route('/recaudacion')
def vista_predio():
    query =recaudacion.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'recaudacion': data
    }
    return jsonify(result)

@bp.route('/persona')
def vista_predio():
    query =persona.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'persona': data
    }
    return jsonify(result)

@bp.route('/predio')
def vista_predio():
    query =predio.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'predio': data
    }
    return jsonify(result)
