from app import app
from models import db
from flask import render_template
'''
GESTOR DE ERRORES, CON ESTO EN CASO DE QUE ALGUNA PAGINA NOS DEVUELVA ALGUNOS DE LOS SIGUIENTES ERRORES
EN VEZ DE SALIR UNA PESTAÑA POR DEFECTO HACEMOS QUE SALGA UNA DE NUESTRAS PAGINAS
'''
@app.errorhandler(500)
def internal_server_error(e):
    db.session.rollback()
    return render_template("500.html"), 500


@app.errorhandler(404)
def page_not_found(e):
    db.session.rollback()
    return render_template("404.html"), 404

@app.errorhandler(403)
def access_denied(e):
    db.session.rollback()
    return render_template("403.html"), 403
