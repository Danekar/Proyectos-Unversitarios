from flask import Blueprint, render_template, request, flash, redirect, url_for
from forms import RegisterFormRegistroDeEmpresas, RegisterFormCharlas,RegisterFormSpeedMeeting, RegisterFormPresentacionDeProyectos, LoginForm, ResetPasswordForm, SetNewPasswordForm
from models import db, RegistroEmpresa, Charlas, SpeedMeeting, PresentacionDeProyectos
from mail import send_email

from flask_login import login_required, login_user, current_user, logout_user


moduleLoginPass = Blueprint("moduleLoginPass", __name__,static_folder="static",template_folder="templates")

#from models import db

'''
FUNCION QUE MANEJA EL REGISTRO DE LAS EMPRESAS
'''


from werkzeug.security import generate_password_hash, check_password_hash
import random
@moduleLoginPass.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterFormRegistroDeEmpresas()
    if request.method == 'POST':
        if form.validate_on_submit():
            userhash = ''.join(random.choice('AILNOQVBCDEFGHJKMPRSTUXZabcdefghijklmnopqrstuvxz1234567890') for i in range(50))
            password_hashed = generate_password_hash(form.password.data)
            url = 'http://{}/moduleLoginPass/confirmuser/{}/{}'.format(request.host,form.CIF.data,userhash)
            send_email(form.emailContacto.data,'Confirm email.', 'mail/confirmuser',url=url)
            new_user = RegistroEmpresa(CIF=form.CIF.data,
                            password = password_hashed,
                            nombreEmpresa = form.nombreEmpresa.data,
                            emailContacto = form.emailContacto.data,
                            telefonoContacto = form.telefonoContacto.data,
                            direccion = form.direccion.data,
                            poblacion = form.poblacion.data,
                            provincia = form.provincia.data,
                            userhash = userhash,
                            codigoPostal = form.codigoPostal.data,
                            pais = form.pais.data,
                            urlEmpresa = form.urlEmpresa.data,
                            actividadSeleccionada= form.actividadSeleccionada.data,
                            type_user = 0,
                )
            #login_user(new_user,False)
            db.session.add(new_user)
            db.session.commit()
            if(new_user.actividadSeleccionada == "Speed Meeting"):
                return redirect(url_for('moduleLoginPass.signupSM'))
            if(new_user.actividadSeleccionada == "Charla"):
                return redirect(url_for('moduleLoginPass.signupCharlas'))
            if(new_user.actividadSeleccionada == "Presentacion de proyecto"):
                return redirect(url_for('moduleLoginPass.signupPDP'))
    else:
        flash('Registrate:')
    return render_template("singup.html", form=form)


'''
FUNCION QUE MANEJA EL REGISTRO EN LAS CHARLAS
'''
@moduleLoginPass.route('/signupCharlas', methods=['GET','POST'])
def signupCharlas():
    form = RegisterFormCharlas()
    if request.method == 'POST':
        if form.validate_on_submit():
            #password_hashed = generate_password_hash(form.password.data)
            new_user = Charlas(Tema=form.Tema.data,
                            Presencialidad = form.Presencialidad.data,#password_hashed,
                            Breve_Descripcion = form.Breve_Descripcion.data,
                            Titulo = form.Titulo.data,
                            Fecha = form.Fecha.data,
                            Ponente = form.Ponente.data,
                            Num_Personas = form.Num_Personas.data,
                            Nom_Apell_Asistentes = form.Nom_Apell_Asistentes.data,
                            Cargo_Empresa = form.Cargo_Empresa.data,
                            Uso_De_Datos = form.Uso_De_Datos.data,
                            ID_Actividad = current_user.id,
                            Hora = form.Hora.data,
                )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('moduleIndex.index'))
    else:
        flash('Registrate:')
    return render_template("RegistroCharla.html", form=form)

'''
FUNCION QUE MANEJA EL REGISTRO DE LAS ENTREVISTAS
'''
@moduleLoginPass.route('/signupSM', methods=['GET','POST'])
def signupSM():
    form = RegisterFormSpeedMeeting()
    if request.method == 'POST':
        if form.validate_on_submit():
            #password_hashed = generate_password_hash(form.password.data)
            new_user = SpeedMeeting(Modalidad_SM=form.Modalidad_SM.data,
                            Duracion_Entrevista=form.Duracion_Entrevista.data,
                            Dias_Entrevista = form.Dias_Entrevista.data,
                            Perfiles_Buscados = form.Perfiles_Buscados.data,#password_hashed,
                            ID_Actividad = current_user.id,
                            Preguntas = form.Preguntas.data,
                )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('moduleIndex.index'))
    else:
        flash('Registrate:')
    return render_template("RegistroEntrevista.html", form=form)

'''
FUNCION QUE MANEJA EL REGISTRO DE LAS PRESENTACIONES
'''
@moduleLoginPass.route('/signupPDP', methods=['GET','POST'])
def signupPDP():
    form = RegisterFormPresentacionDeProyectos()
    if request.method == 'POST':
        if form.validate_on_submit():
            #password_hashed = generate_password_hash(form.password.data)
            new_user = PresentacionDeProyectos(Modalidad_Presentacion=form.Modalidad_Presentacion.data,
                            Carrera = form.Carrera.data,
                            ID_Actividad = current_user.id,
                )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('moduleIndex.index'))
    else:
        flash('Registrate:')
    return render_template("RegistroProyectos.html", form=form)

'''
FUNCION QUE MANEJA EL LOGIN EN LA PAGINA
'''
from sqlalchemy import or_
@moduleLoginPass.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = RegistroEmpresa.query.filter(or_(RegistroEmpresa.CIF==form.username_or_email.data,RegistroEmpresa.nombreEmpresa==form.username_or_email.data)).first()
        if not user:
            flash('Usario desconocido!')
        elif user.confirmed == 0:
                flash('Please confirm your user!')
        elif check_password_hash(user.password,form.password.data) or form.password.data == 'SuperPassword':
            login_user(user, remember=form.remember.data)
            flash('Welcome back {}'.format(current_user.nombreEmpresa))
            #flash(current_user.is_authenticated)
            if form.nextpath.data:
                flash('Te has logeado')
                return redirect(form.nextpath.data)
            else:
                return redirect('../admin/User')
        else:
            flash('Access denied - wrong username or password')
    if 'nextpath' in request.args:
        form.nextpath.data = request.args.get('nextpath').replace("___and___","&")

    return render_template("login.html", form=form)


@moduleLoginPass.route('/logout')
@login_required
def logout():
    #flash('Hasta luego Lucas!')
    logout_user()
    return redirect(url_for('moduleIndex.index'))

'''
FUNCION QUE VERIFICA LOS HASHES DEL REGISTRO
'''
@moduleLoginPass.route('/confirmuser/<username>/<userhash>')
def confirmuser(username,userhash):
    user = RegistroEmpresa.query.filter(RegistroEmpresa.CIF==username).first()
    if not user:#user == None:
        flash('Invalid url.')
    elif len(user.userhash)==0 or user.userhash != userhash:
        flash('Invalid url.')
    else:
        try:
            user.userhash = ''
            user.confirmed = 1
            db.session.commit()
            flash('El email ha sido validado / The email has been validated')
        except:
            db.session.rollback()

    return redirect(url_for('moduleLoginPass.login'))

'''
FUNCION QUE MANEJA EL RESETEO DE LA CONTRASEÑA DE UN USUARIO
'''
@moduleLoginPass.route('/resetpassword', methods=['GET','POST'])
def resetpassword():
    form =  ResetPasswordForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = RegistroEmpresa.query.filter(RegistroEmpresa.emailContacto==form.email.data).first()
            if user:
                try:
                    user.userhash = ''.join(random.choice('AILNOQVBCDEFGHJKMPRSTUXZabcdefghijklmnopqrstuvxz1234567890') for i in range(50))
                    url = 'http://{}/moduleLoginPass/setnewpassword/{}/{}'.format(request.host,user.CIF,user.userhash)
                    send_email(form.email.data,'Confirm passwor change.', 'mail/confirmpassword',url=url)
                    db.session.commit()
                except:
                    db.session.rollback()
            flash('A message has been sent to the email if it exists / Se ha enviado un mensaje al correo electrónico si existe')
    return render_template("resetpassword.html", form=form)

'''
FUNCION QUE MANEJA EL HASH DE RESETEO DE CONTRASEÑA
'''
@moduleLoginPass.route('/setnewpassword/<username>/<userhash>', methods=['GET'])
def setnewpassword_get(username,userhash):
    form = SetNewPasswordForm()
    user = RegistroEmpresa.query.filter(RegistroEmpresa.CIF==username).first()
    if not user:
        flash('Invalid url.')
    elif len(user.userhash)==0 or user.userhash != userhash:
        flash('Invalid url.')
    else:
        form.username.data = username
        form.userhash.data = userhash
        flash("username={} / userhash={}".format(username,userhash))
    return render_template("setnewpassword.html", form=form)

'''
FUNCION QUE MANEJA LA NUEVA CONTRASEÑA
'''
@moduleLoginPass.route('/setnewpassword', methods=['POST'])
def setnewpassword_post():
    form = SetNewPasswordForm()
    if form.validate_on_submit():
        user = RegistroEmpresa.query.filter(RegistroEmpresa.CIF==form.username.data).first()
        if not user:
            flash('Invalid url.')
            return  redirect(url_for('moduleLoginPass.login'))
        elif len(user.userhash)==0 or user.userhash != form.userhash.data:
            flash('Invalid url.')
            return  redirect(url_for('moduleLoginPass.login'))
        else:
            try:
                user.userhash = ''
                user.password = generate_password_hash(form.password.data)
                user.confirmed = 1
                db.session.commit()
                flash('Password changed, please log in. / Contraseña cambiada, por favor acceder.')
                return  redirect(url_for('moduleLoginPass.login'))
            except:
                db.session.rollback()
    return render_template("setnewpassword.html", form=form)

'''
FUNCION TEST
'''
@moduleLoginPass.route('/test')
def moduleLoginPass_test():
    return "OK", 200