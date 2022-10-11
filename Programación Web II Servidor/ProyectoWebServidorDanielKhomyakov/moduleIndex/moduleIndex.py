from flask import Blueprint, render_template
'''
CLASE INDICE QUE GESTIONA LAS DISTINTAS LLAMADAS
'''
moduleIndex = Blueprint("moduleIndex", __name__,static_folder="static",template_folder="templates")

'''
VISTA PAGINA PRINCIPAL
'''
@moduleIndex.route('/', methods=['GET','POST'])
#@login_required
def index():
    return render_template("Pepe.html")

'''
VISTA PAGINA INFORMACION
'''
@moduleIndex.route('/about', methods=['GET','POST'])
#@login_required
def about():
    return render_template("About.html")

'''
VISTA MENU CHARLAS
'''
@moduleIndex.route('/MenuCharlas', methods=['GET','POST'])
#@login_required
def M_charlas():
    return render_template("Menu_Charlas.html")

'''
VISTA MENU PRESENTACION PROYECTOS
'''
@moduleIndex.route('/MenuPresentacionDeProyectos', methods=['GET','POST'])
#@login_required
def M_PresentacionDeProyectos():
    return render_template("Menu_Presentacion_De_Proyectos.html")

'''
VISTA MENU SPEED MEETING
'''
@moduleIndex.route('/MenuSpeedMeeting')
#@login_required
def M_MenuSpeedMeeting():
    return render_template("Menu_Speed_Meeting.html")

'''
CLASE TEST
'''
@moduleIndex.route('/test')
def moduleLoginPass_test():
    return "OK", 200

'''
VISTA PAGINA PRUEBA
'''
@moduleIndex.route('/prueba')
def prueba():
    return render_template("prueba.html")