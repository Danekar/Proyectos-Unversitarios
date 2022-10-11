from flask_login import current_user
from wtforms import PasswordField
from werkzeug.security import generate_password_hash
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla.view import ModelView, func
from app import app
from models import db, RegistroEmpresa, Charlas,PresentacionDeProyectos, SpeedMeeting

'''
CLASE ESPECIAL DEL ADMINISTRADOR
'''

'''
VISTA DEL ADMINISTRADOR
'''
class AdminView(AdminIndexView):
  def is_accessible(self):
    if current_user.is_authenticated and current_user.type_user == 1:
      return True
    return False


admin = Admin(index_view=AdminView())
admin.init_app(app)

'''
VISTA PRIVADA DEL ADMINISTRADOR
'''
class ProtectedViewRegistroDeEmpresas(ModelView):
  def is_accessible(self):
    if current_user.is_authenticated and current_user.type_user == 1:
      return True
    return False

class ProtectedViewCharlas(ModelView):
  def is_accessible(self):
    if current_user.is_authenticated and current_user.type_user == 1:
      return True
    return False

class ProtectedViewPresentacionDeProyectos(ModelView):
  def is_accessible(self):
    if current_user.is_authenticated and current_user.type_user == 1:
      return True
    return False

class ProtectedViewSpeedMeeting(ModelView):
  def is_accessible(self):
    if current_user.is_authenticated and current_user.type_user == 1:
      return True
    return False

'''
CONFIGURACION DE USUARIO ADMINISTRADOR
'''

'''
class UserAdmin(ProtectedView):
column_exclude_list = ('password')
  form_excluded_columns = ('password')
  column_auto_select_related = True

  def scaffold_form(self):
    form_class = super(UserAdmin, self).scaffold_form()
    form_class.password2 = PasswordField('New Password')
    return form_class
  def on_model_change(self, form, model, is_created):
    if len(model.password2):
      model.password = generate_password_hash(model.password2,method='sha256')
  def is_accessible(self):
    return current_user.is_authenticated and current_user.type_user == 0'''



class UserView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.type_user == 0:
            return True
        return False
    def after_model_change(self, form, model, is_created):
        model.ID_Actividad=current_user.id
        db.session.commit()
    def get_query(self):
        return db.session.query(self.model).filter(self.model.ID_Actividad==current_user.id)
    def get_count_query(self):
        return db.session.query(db.func.count('*')).filter(self.model.ID_Actividad==current_user.id)



class UserViewPresentacion(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.type_user == 0:
            return True
        return False
    def after_model_change(self, form, model, is_created):
        model.ID_Actividad=current_user.id
        db.session.commit()
    def get_query(self):
        return db.session.query(self.model).filter(self.model.ID_Actividad==current_user.id)
    def get_count_query(self):
        return db.session.query(db.func.count('*')).filter(self.model.ID_Actividad==current_user.id)


class UserViewSpeedMeeting(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.type_user == 0:
            return True
        return False
    def after_model_change(self, form, model, is_created):
        model.ID_Actividad=current_user.id
        db.session.commit()
    def get_query(self):
        return db.session.query(self.model).filter(self.model.ID_Actividad==current_user.id)
    def get_count_query(self):
        return db.session.query(db.func.count('*')).filter(self.model.ID_Actividad==current_user.id)


class UserViewRegistroDeEmpresas(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and current_user.type_user == 0:
            return True
        return False
    def get_query(self):
        return db.session.query(self.model).filter(self.model.id==current_user.id)
    def get_count_query(self):
        return db.session.query(db.func.count('*')).filter(self.model.id==current_user.id)



admin.add_view(ProtectedViewRegistroDeEmpresas(RegistroEmpresa, db.session))
admin.add_view(ProtectedViewCharlas(Charlas, db.session,endpoint='CharlasAdmin'))
admin.add_view(ProtectedViewPresentacionDeProyectos(PresentacionDeProyectos, db.session,endpoint='PresentacionDeProyectosAdmin'))
admin.add_view(ProtectedViewSpeedMeeting(SpeedMeeting, db.session,endpoint='SpeedMeetingAdmin'))

admin.add_view(UserView(Charlas, db.session, endpoint='Charlas'))
admin.add_view(UserViewPresentacion(PresentacionDeProyectos, db.session, endpoint='PresentacionDeProyectos'))
admin.add_view(UserViewSpeedMeeting(SpeedMeeting, db.session, endpoint='SpeedMeeting'))
admin.add_view(UserViewRegistroDeEmpresas(RegistroEmpresa, db.session, endpoint='User'))



'''
LOGOUT DE USUARIO ADMINISTRADOR
'''
from flask_admin.menu import MenuLink
admin.add_link(MenuLink(name='Logout',category="", url='../moduleLoginPass/logout'))
admin.add_link(MenuLink(name='Go back',category="", url='/'))
