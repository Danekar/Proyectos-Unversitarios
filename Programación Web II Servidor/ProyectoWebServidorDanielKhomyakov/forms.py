from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, HiddenField
from wtforms.validators import InputRequired, Length,EqualTo, Email
from wtforms.fields.html5 import DateField, TimeField
from flask_wtf.file import FileField, FileRequired

'''
FOROS LOS CUALES SE NECESITARÁ QUE SE RELLENEN PARA EL REGISTRO YA SEA DE LA EMPRESA EN SI
O DE SUS EVENTOS. AQUI TAMBIEN APARTE DE ESTOS MISMOS HAY AL FINAL EL LOGIN JUNTO A LAS CONTRASEÑAS PERDIDAS.
'''


class RegisterFormRegistroDeEmpresas(FlaskForm):
    CIF = StringField("Company CIF / CIF de la empresa", validators=[InputRequired(),Length(min=4,max=15)])
    password = PasswordField("Password / Contraseña ",
    validators=[InputRequired(), Length(min=4), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm password / Confirmar contraseña ", validators=[InputRequired()])
    nombreEmpresa = StringField("Company name / Nombre de la empresa", validators=[InputRequired(),Length(min=2,max=15)])
    emailContacto = StringField("E-mail", validators=[InputRequired(), Length(max=50)])
    telefonoContacto = StringField("Phone number / Numero de telefono", validators=[InputRequired(), Length(max=50)])
    direccion = StringField("Address / Direccion ", validators=[InputRequired(), Length(max=50)])
    poblacion = StringField("Population / Poblacion", validators=[InputRequired(), Length(max=50)])
    provincia = StringField("Province / Provincia", validators=[InputRequired(), Length(max=50)])
    codigoPostal = StringField("Postal Code / Codigo Postal", validators=[InputRequired(), Length(max=50)])
    pais = StringField("Country / Pais", validators=[InputRequired(), Length(max=50)])
    urlEmpresa = StringField("URL web page / URL pagina web", validators=[InputRequired(), Length(max=50)])
    actividadSeleccionada = SelectField('Select an activity / Seleccione una actividad',
                               choices=[
                                 ('Speed Meeting', 'Speed Meeting'),
                                 ('Charla', 'Charla'),
                                 ('Presentacion de proyecto', 'Presentacion de proyecto')
                               ])

class RegisterFormSpeedMeeting(FlaskForm):
    Modalidad_SM  = SelectField('Modalidad',
                               choices=[
                                 ('Presencial', 'Presencial'),
                                 ('Telepresencial', 'Telepresencial')
                               ])
    Dias_Entrevista = DateField("Date / Fecha", validators=[InputRequired()])
    Duracion_Entrevista = StringField("Interview duration / Duracion de la Entrevista", validators=[InputRequired(), Length(max=50)])
    Perfiles_Buscados  = SelectField('Modalidad',
                               choices=[
                                 ('Diseño de Productos Interactivos', 'Diseño de Productos Interactivos'),
                                 ('Ingeniería del Software', 'Ingeniería del Software'),
                                 ('Diseño Digital', 'Diseño Digital'),
                                 ('Animación', 'Animación')
                               ])
    Preguntas = StringField("Interview questions / Preguntas para la entrevista", validators=[InputRequired(), Length(max=50)])
    #ID_Actividad no se recoge en el formulario, es un dato interno

class RegisterFormCharlas(FlaskForm):
    Tema = StringField("Theme / Tema", validators=[InputRequired(), Length(max=50)])
    Presencialidad = SelectField('Modalidad',
                               choices=[
                                 ('Presencial', 'Presencial'),
                                 ('Telepresencial', 'Telepresencial')
                               ])
    Titulo = StringField("Title / Titulo", validators=[InputRequired(), Length(max=50)])
    Breve_Descripcion = StringField("Short description / Breve descripcion", validators=[InputRequired(), Length(max=250)])
    Fecha = DateField("Date / Fecha", validators=[InputRequired()])
    Hora = TimeField("Time / Hora", validators=[InputRequired()], format='%H:%M')
    Ponente = StringField("Speaker / Ponente", validators=[InputRequired(), Length(max=50)])
    Num_Personas = StringField("Number of participants / Numero de participantes", validators=[InputRequired(), Length(max=250)])
    Nom_Apell_Asistentes = StringField("Name and surname of the participants / Nombre y apellidos de los participantes", validators=[InputRequired(), Length(max=50)])
    Cargo_Empresa = StringField("Company position / Cargo en la empresa", validators=[InputRequired(), Length(max=50)])
    Uso_De_Datos = BooleanField()

class RegisterFormPresentacionDeProyectos(FlaskForm):
    Modalidad_Presentacion = SelectField('Modalidad',
                               choices=[
                                 ('Presencial', 'Presencial'),
                                 ('Telepresencial', 'Telepresencial')
                               ])
    Carrera = SelectField('Modalidad',
                               choices=[
                                 ('Diseño de Productos Interactivos', 'Diseño de Productos Interactivos'),
                                 ('Ingeniería del Software', 'Ingeniería del Software'),
                                 ('Diseño Digital', 'Diseño Digital'),
                                 ('Animación', 'Animación')
                               ])

class ResetPasswordForm(FlaskForm):
    email = StringField("E-mail", validators=[InputRequired(),Email(message="Email no es válido!"),Length(max=50)])


class SetNewPasswordForm(FlaskForm):
    username = HiddenField('username')
    userhash = HiddenField('userhash')
    password = PasswordField("Password / Contraseña ",validators=[InputRequired(), Length(min=4), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Confirm password / Confirmar contraseña ", validators=[InputRequired()])


class LoginForm(FlaskForm):
    username_or_email = StringField('Introduce the CIF of your company / Introduce el CIF de tu empresa ')
    password = PasswordField('Password / Contraseña', validators=[InputRequired(),Length(min=4,max=80)])
    nextpath = HiddenField('Next Path')
    remember = BooleanField('Remember Me / Recuérdame')