import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
#Estructuras
from Registro import *
from Hash import *
from Grafo import *

avl = Avl() #avl para login y registro
tabla = Hash() #tabla hash
grafo = Grafo() #grafo para los cursos del pensum


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
    
@app.route('/graficaHash',methods=['post'])
def graficaHash():
    if request.method == 'POST':
        tabla.graficar()
        base_64 = ""
        with open("C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\hash.png","rb") as img_file:
            base_64 = base64.b64encode(img_file.read())

        return jsonify({
            "estado":"200",
            "img":str(base_64.decode("utf-8"))
        })


@app.route('/cargaEstudiantes',methods=['post'])
def cargaEstudiantes():
    json_entrada = request.get_json()
    datos = json.loads(json_entrada)
    if request.method == 'POST':
        try:
            for item in datos['estudiantes']:
                carnet = item['carnet']
                dpi = item['DPI']
                nombre = item['nombre']
                carrera = item['carrera']
                correo = item['correo']
                password = item['password']
                edad = item['edad']
                avl.insertar(int(carnet),dpi,nombre,carrera,correo,password,edad)

            return jsonify({
                "estado":"200"
            })
        except:
            return jsonify({
                "estado":"400"
            })

@app.route('/cargaCursos',methods=['post'])
def cargaCursos():
    json_entada = request.get_json();
    datos = json.loads(json_entada)
    if request.method=='POST':
        try:
            #para crear nodo de cursos
            for item in datos['Cursos']:
                codigo = item['Codigo']
                nombre = item['Nombre']
                creditos = item['Creditos']
                prerequisitos = item['Prerequisitos']
                obligatorio = item['Obligatorio']
                grafo.insercion_Grafo(int(codigo),nombre,creditos,prerequisitos,obligatorio)

            #para crear conexion(ady)
            for elem in datos['Cursos']:
                cod = elem['Codigo']
                prere = elem['Prerequisitos']
                arrayPre = prere.split(",")
                print(arrayPre)
                print(len(arrayPre))
                if len(arrayPre)==1:        
                    if arrayPre[0]!="":
                        grafo.insertar_adya(int(arrayPre[0]),int(cod))

                elif len(arrayPre)>1:
                    for i in arrayPre:
                        grafo.insertar_adya(int(i),int(cod))

            
            return jsonify({
                "estado":"200"
            })
        except:
            return({
                "estado":"400"
            })

@app.route('/cargaApuntes',methods=['post'])
def cargaApuntes():
    json_entrada = request.get_json();
    datos = json.loads(json_entrada)
    
    if request.method=='POST':
        try:
            #recorrer usuarios
            for item in datos['usuarios']:
                carnet = item['carnet']
                #recorrer apuntes
                for elemento in item['apuntes']:
                    titulo = str(elemento['Título']).replace("-","").replace("/","").replace(" ","_")
                    contenido = str(elemento['Contenido'])
                    tabla.insertar(int(carnet),titulo,contenido)
                    print("se inserto "+str(carnet)+" "+str(titulo))

            return jsonify({
                "estado":"200"
            })
        except:
            return jsonify({
                "estado":"400"
            })

@app.route('/graficaGrafo',methods=['post'])
def graficaGrafo():

    if request.method == 'POST':
        grafo.graficar();
        base_64 = ""
        with open("C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\grafo_pensum.png","rb") as img_file:
            base_64 = base64.b64encode(img_file.read())

        return jsonify({
            "estado":"200",
            "img":str(base_64.decode("utf-8"))
        })

@app.route('/graficaCodigo', methods=['post'])
def graficaCodigo():
    codigo = request.json['codigo']
    if request.method == 'POST':
        grafo.graficarCodigo(int(codigo))
        base_64 = ""
        with open("C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\grafo_pensum_estudiante.png","rb") as img_file:
            base_64 = base64.b64encode(img_file.read())

        return jsonify({
            "estado":"200",
            "img":str(base_64.decode("utf-8"))
        })

app.run(host='0.0.0.0', port=3000, debug=True)