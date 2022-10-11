from app import app

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from flask_login import UserMixin
exit

'''
CLASE MODELO DE LA ESTRUCTURA MVC QUE DEFINE LA ESTRUCTURA DE LOS DISTINTOS REGISTROS EN LA DB
'''

class RegistroEmpresa(UserMixin, db.Model):
    __tablename__ = "RegistroDeEmpresas"
    id = db.Column(db.Integer, primary_key=True)
    CIF = db.Column(db.Integer)
    password = db.Column(db.String(200), unique = True)
    nombreEmpresa = db.Column(db.String(50), unique = True)
    emailContacto = db.Column(db.String(50))
    telefonoContacto = db.Column(db.Integer, unique = True)
    direccion = db.Column(db.String(50))
    poblacion = db.Column(db.String(50))
    provincia = db.Column(db.String(50))
    codigoPostal = db.Column(db.String(6))
    pais = db.Column(db.String(50))
    userhash = db.Column(db.String(50))
    confirmed = db.Column(db.Integer, default=0)
    urlEmpresa = db.Column(db.String(50))
    type_user = db.Column(db.Integer)
    actividadSeleccionada = db.Column(db.String(50))




class Charlas(db.Model):
    __tablename__ ='Charlas'
    ID_Charlas = db.Column(db.Integer, primary_key=True)
    Tema = db.Column(db.String(50))
    Presencialidad  = db.Column(db.String(14))
    Titulo  = db.Column(db.String(20))
    Breve_Descripcion  = db.Column(db.String(150))
    Fecha  = db.Column(db.Date)
    Ponente  = db.Column(db.String(20))
    Num_Personas   = db.Column(db.Integer)
    Nom_Apell_Asistentes  = db.Column(db.String(150))
    Cargo_Empresa  = db.Column(db.String(40))
    Uso_De_Datos  = db.Column(db.String(2))
    ID_Actividad  = db.Column(db.Integer, db.ForeignKey('RegistroDeEmpresas.id'))
    Hora  = db.Column(db.Time)

class SpeedMeeting(UserMixin, db.Model):
    __tablename__ ='SpeedMeeting'
    Id_SpeedMeeting = db.Column(db.Integer, primary_key=True)
    Modalidad_SM = db.Column(db.String(10))
    Dias_Entrevista = db.Column(db.String(9))
    Duracion_Entrevista = db.Column(db.Integer)
    Perfiles_Buscados = db.Column(db.String(100))
    Preguntas = db.Column(db.String(100))
    ID_Actividad = db.Column(db.Integer, db.ForeignKey('RegistroDeEmpresas.id'))

class PresentacionDeProyectos(UserMixin, db.Model):
    __tablename__='PresentacionDeProyectos'
    Id_SpeedMeeting = db.Column(db.Integer, primary_key=True)
    Modalidad_Presentacion = db.Column(db.String(10))
    Carrera = db.Column(db.String(30))
    ID_Actividad = db.Column(db.Integer, db.ForeignKey('RegistroDeEmpresas.id'))