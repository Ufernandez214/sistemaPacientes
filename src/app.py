from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config, constants

# Models:
from models.ModelUser import ModelUser
from models.ModelPaciente import ModelPacientes
from models.ModelPacientesDetalles import ModelPacientesDetalles
from models.ModelConsulta import ModelConsulta

# Entities:
from models.entities.User import User
from models.entities.Paciente import Pacientes
from models.entities.PacientesDetalles import PacientesDetalles
from models.entities.Consulta import Consulta

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('sistema/dashboard.html')

@app.route('/pacientes')
@login_required
def pacientes():
    return render_template('sistema/pacientes.html')

@app.route('/consultas')
@login_required
def consultas():
    return render_template('sistema/consultas.html')

@app.route('/construccion')
@login_required
def construccion():
    return render_template('sistema/construccion.html')

def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return render_template('sistema/dashboard.html')


@app.route('/enviaDatos', methods=['POST'])
def enviaDatos():
    paciente = Pacientes(0, request.form['nombres'], request.form['apellidos'],request.form['edad'],request.form['email'],request.form['telefono'],request.form['tipoPaciente'],request.form['tipoPaciente'],request.form['idHistoriaClinica'])
    insertPaciente = ModelPacientes.save(db, paciente)
    if insertPaciente > 0:

        dieta  = request.form['dieta']
        tiempo_fumador  = request.form['tiempoFumador']
        peso = peso = request.form['peso']
        estatura = request.form['estatura']

        if estatura == "":
            estatura = 0
        if peso == "":
            peso = 0
        if tiempo_fumador == "":
            tiempo_fumador = 0
        if dieta == "":
            dieta = 0

        pacienteDetalles = PacientesDetalles(0, request.form['es_fumador'], tiempo_fumador, dieta,peso,estatura,insertPaciente)
        ModelPacientesDetalles.save(db, pacienteDetalles)
        return "OK"
    else:
        return "Error"

@app.route('/getPacientes', methods=['POST'])    
def getPacientes():
    paciente = ModelPacientes.getPacientes(db)
    return jsonify((paciente))  

@app.route('/getPacientesUrgencia', methods=['POST'])
def getPacientesUrgencia():
   urgencias = ModelPacientes.getPacientesUrgencia(db)
   return jsonify((urgencias)) 

@app.route('/getPacientesNinos', methods=['POST'])
def getPacientesNinos():
    pacientes = ModelPacientes.getPacientesNinos(db)
    return jsonify((pacientes)) 

@app.route('/getPacientesCGI', methods=['POST'])
def getPacientesCGI():
    pacientes = ModelPacientes.getPacientesCGI(db)
    return jsonify((pacientes))   

@app.route('/getPacientesPorConsulta', methods=['POST'])
def getPacientesPorConsulta():
        consulta = ModelConsulta.getPacientesPorConsulta(db,request.form['idConsulta'])
        return jsonify((consulta))

@app.route('/atenderPaciente', methods=['POST'])
def atenderPaciente():
    consulta = request.form['consulta']
    estado = ModelPacientes.updateEstadoPaciente(db,request.form['idPaciente'],request.form['idEstado'])
    estadoPaciente = ModelPacientes.updateTipoPaciente(db,request.form['idPaciente'],consulta)
    return jsonify((estado))


@app.route('/getConsultas', methods=['POST'])
def getConsultas():
    consultas = ModelConsulta.getConsultas(db)
    return jsonify((consultas))

@app.route('/updateEstadoConsulta', methods=['POST'])
def updateEstadoConsulta():
    consulta = request.form['idConsulta']
    estado = request.form['estado']
    consultas = ModelConsulta.updateEstadoConsulta(db, consulta, estado)
    return jsonify((consultas))

@app.route('/getEstadoConsulta', methods=['POST'])
def getEstadoConsulta():
    consulta = request.form['consulta']
    estado = ModelConsulta.getEstadoConsulta(db, consulta)
    return jsonify((estado))

@app.route('/liberarConsulta', methods=['POST'])
def liberarConsulta():
    consulta = request.form['consulta']
    estado = request.form['estado']
    estadoConsulta = ModelConsulta.updateEstadoConsulta(db, consulta, estado)
    ModelConsulta.updatePacienteAtendido(db, consulta)
    return jsonify((estadoConsulta))

if __name__ == '__main__':
    app.config.from_object(config['development'])
    #csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()