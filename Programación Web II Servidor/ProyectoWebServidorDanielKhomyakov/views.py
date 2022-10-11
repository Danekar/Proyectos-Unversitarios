from flask import request, redirect, url_for
from app import app
from models import RegistroEmpresa
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

'''
CLASE VISTA DE LA ESTRUCTURA MVC QUE DEFINE LA ESTRUCTURA DE REDIRECCIONES
'''

'''
FUNCIÓN QUE CARGA EL USUARIO
'''
@login_manager.user_loader
def load_user(user_id):
    return RegistroEmpresa.query.get(int(user_id))

'''
GESTOR DE REDIRECCIONES NO AUTORIZADAS
'''

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login?nextpath=' + request.full_path.replace("&","___and___"))

@app.route('/', methods=['GET','POST'])
def index():
    return redirect(url_for('moduleIndex.index'))
