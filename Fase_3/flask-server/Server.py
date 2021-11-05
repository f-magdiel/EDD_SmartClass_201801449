import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.wrappers import response

#Estructuras
from Registro import *
from Hash import *

avl = Avl() #avl para login y registro
tabla = Hash() #tabla hash

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/login', methods=['post'])
def login():
   
    usuario = request.json['usuario']
    contra = request.json['contraseña']
    if request.method=='POST':
        if usuario == "admin" and contra =="admin":
            return jsonify([{
                "tipo":usuario,
                "bandera":True
            }])
        else:
            try:
                aux = avl.buscar(int(usuario))
                if aux.carnet == int(usuario) and contra == aux.password:
                    print("Si es student")
                    return jsonify([{
                    "tipo":"estudiante",
                    "bandera":True,
                    "dato":usuario
                    }])
                else:
                     return jsonify([{
                    "tipo":"error",
                    "bandera":False
                    }])
            except:
                return jsonify([{
                "tipo":"error",
                "bandera":False
            }])
            
       
            

@app.route('/registro',methods=['post'])
def registro():
    carnet = request.json['carnet']
    dpi = request.json['dpi']
    nombre = request.json['nombre']
    carrera = request.json['carrera']
    correo = request.json['correo']
    password = request.json['password']
    edad = request.json['edad']

    if request.method == 'POST':
        #se crea estructura y se almacena en ella
        try:
            avl.insertar(int(carnet),dpi,nombre,carrera,correo,password,edad)
            return jsonify([{
            "estado":"200",
        }])
        except:
            return jsonify([{
            "estado":"400"
        }])
        
@app.route('/getEstudiantes',methods=['post'])
def getEstudiantes():

    carnet = request.json['carnet']
    resultado = tabla.buscar(int(carnet))
    conver = json.dumps(resultado)
    print(conver)
    if request.method == 'POST':
        return jsonify(conver)       
    
@app.route('/newApunte',methods=['post'])
def newApunte():
    carnet = request.json['carnet']
    titulo = request.json['titulo']
    contenido = request.json['contenido']
    if request.method == 'POST':
        try:
            tabla.insertar(int(carnet),titulo,contenido);
            return jsonify([{
                "estado":"200"
            }])
        except:
            return jsonify([{
                "estado":"400"
            }])
    

app.run(host='0.0.0.0', port=3000, debug=True)