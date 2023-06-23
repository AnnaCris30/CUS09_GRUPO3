from flask import Flask, render_template, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)

DB_HOST = "137.184.120.127"
DB_NAME = "sigcon"
DB_USER = "modulo4"
DB_PASS = "modulo4"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

@app.route('/')
def Index():
    cur.execute("""
    SELECT r.id_recaudacion, r.id_cuenta, r.id_mant_recibo, r.n_operacion, r.fecha_operacion, tm.etiqueta||' '||r.importe, rs.descripcion, r.id_cuenta_predio, r.observacion
    FROM recaudacion AS r
    JOIN tipo_moneda AS tm ON r.moneda = tm.id_tipo_moneda
    JOIN recaudacion_estado AS rs ON r.id_recaudacion_estado = rs.id_recaudacion_estado
    """)
    datos = cur.fetchall()

    cur.execute("""
    SELECT id_cuenta
    FROM cuenta
    """)
    cuenta = cur.fetchall()

    cur.execute("""
    SELECT id_mant_recibo
    FROM mant_recibo
    """)
    recibo = cur.fetchall()
    datos_con_indices = [(indice+1, dato) for indice, dato in enumerate(datos)]

    return render_template('index.html', datos=datos_con_indices, cuenta=cuenta,recibo=recibo)

if __name__ == "__main__":
    app.run(debug=True)