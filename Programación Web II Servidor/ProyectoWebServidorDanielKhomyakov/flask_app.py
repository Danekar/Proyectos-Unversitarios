from app import app

'''
USAMOS EL ARCHIVO DE CONFIGURACION EL CUAL TENDRÁ DATOS PARA REALIZAR LA CONEXION CON LA BASE DE DATOS
Y LUEGO CON EL CORREO
'''
import json
with open('configuration.json') as json_file:
    configuration = json.load(json_file)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'rf¡0jpetfgñksdjngoie6543tg9DWR5ERSDKFH09Rñçã3q4'

'''
PARA QUE SE PUEDA REALIZAR LA CONEXION, ES IMPORTANTE INIDCARLE EL USUARIO, SU CONTRASEÑA,
EL HOSTNAME Y EL NOMBRE DE LA BASE DE DATOS.
'''

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}?auth_plugin=mysql_native_password".format(

    username=configuration["MYSQL_USERNAME"],
    password=configuration["MYSQL_PASSWORD"],
    hostname=configuration["MYSQL_HOSTNAME"],
    databasename=configuration["MYSQL_DATABASENAME"]

  )

'''
PARA LA CONFIGURACION DEL EMAIL ES IMPORTANTE INDICARLE EL SERVICIO QUE SE VA A ESTAR
UTILIZANDO COMO ES EL PUERTO. ADICIONALMENTE HARÁ FALTA INDICARLE EL CORREO DESDE EL CUAL
SE ESTARÁ ENVIANDO LOS MENSAJES Y POR ÚLTIMO LA CONTRASEÑA DE ESTA MISMA PARA QUE SE PUEDA
VERIFICAR EL CORREO
'''

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = configuration["gmail_username"]
app.config['MAIL_PASSWORD'] = configuration["gmail_password"]
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Company Day]'
app.config['FLASKY_MAIL_SENDER'] = 'Recepción Company Day'

from flask_bootstrap import Bootstrap
Bootstrap(app)


# VIEWS - START
from views import *

'''
IMPORTAMOS LOS MODULOS QUE TENEMOS PARA QUE ESTOS LUEGO FUNCIONEN Y TODO LO QUE TENGAMOS BAJO SU
NOMBRE SE PUEDA VER. COMO POR EJEMPLO PARA VER LA PAGINA DE INDICE, NO PUEDE SER SOLO INDEX SINO
QUE MODULEINDEX/INDICE.
'''

from moduleIndex.moduleIndex import moduleIndex
from moduleLoginPass.moduleLoginPass import moduleLoginPass
app.register_blueprint(moduleIndex, url_prefix="/moduleIndex") # Indice con paginas informativas
app.register_blueprint(moduleLoginPass, url_prefix="/moduleLoginPass") # Todo el tema del login con las contraseñas
# VIEWS - END


# ERRORS - START
from errors import *
# ERROS - END



# ADMIN - START
from admin import *
# ADMIN - END
