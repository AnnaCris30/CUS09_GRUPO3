from flask import Blueprint, render_template as rt, request, url_for, redirect

bp = Blueprint('recaudaciones', __name__)

@bp.route('/', methods=['POST','GET'])
def cotizaciones():



    return rt("recaudacion.html")