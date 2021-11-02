from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.wrappers import response

#Estructuras
from Registro import *

avl = Avl()

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
                    "bandera":True
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
        
        
    
    

app.run(host='0.0.0.0', port=3000, debug=True)