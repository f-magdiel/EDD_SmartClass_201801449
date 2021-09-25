from flask import Flask, request
from analizador.sintactico import parser
from Fase2_Estructuras.AvlEstudiantes import *
import flask

# Estrutura
arbol = Avl()

# definir
app = Flask(__name__)


# rutas
@app.route('/ejemplo')
def ejemplo():
    return "ejemplo servidor"


@app.route('/carga', methods=['post'])
def carga():
    if request.method == "POST":
        json_entrada = request.get_json()
        tipo = json_entrada['tipo']
        path = json_entrada['path']
        if tipo == "estudiante":
            f = open(path, "r", encoding="utf-8")
            mensaje = f.read()
            f.close()
            resultado_analisis = parser.parse(mensaje)
            try:
                for item in resultado_analisis:
                    if item["type"] == "user":
                        atributos = item["atributos"]
                        carnet = int(atributos[0]["Carnet"].replace("\"", ""))
                        dpi = int(atributos[1]["DPI"].replace("\"", ""))
                        nombre = str(atributos[2]["Nombre"].replace("\"", ""))
                        carrera = str(atributos[3]["Carrera"].replace("\"", ""))
                        correo = str(atributos[4]["Correo"].replace("\"", ""))
                        password = str(atributos[5]["Password"].replace("\"", ""))
                        creditos = int(atributos[6]["Creditos"])
                        edad = int(atributos[7]["Edad"])
                        # Insercion en avl estudiantes
                        arbol.insertar(carnet,dpi,nombre,carrera,correo,password,creditos,edad)

                for item in resultado_analisis:
                    if item["type"] == "task":
                        atributos = item["atributos"]
                        carnet = int(atributos[0]["Carnet"].replace("\"", ""))
                        nombre = atributos[1]["Nombre"].replace("\"", "")
                        descripcion = atributos[2]["Descripcion"].replace("\"", "")
                        materia = atributos[3]["Materia"].replace("\"", "")
                        fecha = atributos[4]["Fecha"].replace("\"", "").split("/")
                        hora = atributos[5]["Hora"].replace("\"", "").replace(":00","")
                        estado = atributos[6]["Estado"].replace("\"", "")
                        auxAvl = arbol.buscar(carnet)
                        if auxAvl != None :
                            auxAvl.lista_anio.buscarAgregar(fecha[2])
                            auxAnio = auxAvl.lista_anio.buscar(fecha[2])
                            auxAnio.lista_mes.buscarAgregar(fecha[1])
                            auxMes = auxAnio.lista_mes.buscar(fecha[1])
                            auxMes.matriz_tarea.insertar("Tarea",int(fecha[0]),int(hora))
                            auxMatriz = auxMes.matriz_tarea.buscarNodoMatriz(int(fecha[0]),int(hora))
                            _fecha = ""
                            cont=0
                            for f in fecha:
                                cont+=1

                                if(cont==3):
                                    _fecha += f
                                else:
                                    _fecha += f + "/"
                            print(_fecha)
                            auxMatriz.lista_tarea.agregar(carnet,nombre,descripcion,materia,_fecha,hora,estado)
                        else:
                            print("No existe carnet")
                return {
                    "estado": 200,
                    "mensaje": "Se ingreso en avl"
                }
            except:
                return {
                    "estado": 400,
                    "mensaje": "No se ingreso en avl"
                }


        elif tipo == "curso estudiante":
            print("")
        elif tipo == "curso pensum":
            print("")


# ejecutar
app.run(host='0.0.0.0', port=3000, debug=True)
