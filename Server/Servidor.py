import json

from flask import Flask, request
from analizador.sintactico import parser
from Fase2_Estructuras.AvlEstudiantes import *
from Fase2_Estructuras.ArbolPensum import *
import flask

# Estrutura
arbol = Avl()
arbolCursos = ArbolPensum()

# definir
app = Flask(__name__)
#@app.route('/cursoEstudiante',methods=['post'])
#def cursoEstudiante():
@app.route('/cursosPensum',methods=['post'])
def cursosPensum():
    json_entrada = request.get_json()
    if request.method == 'POST':
        try:
            for item in json_entrada['Cursos']:
                codigo = item['Codigo']
                nombre = item['Nombre']
                creditos = item['Creditos']
                preRe = item['Prerequisitos']
                obligatorio = item['Obligatorio']
                arbolCursos.insertar(int(codigo),nombre,creditos,preRe,obligatorio)

            return {
                "estado":200,
                "mensaje":"Cursos pensum agregados exitosamente"
            }
        except:
            return {
                "estado":400,
                "mensaje":"Fallo agregar cursos pensum"
            }

@app.route('/cursosEstudiante',methods=['post'])
def cursosEstudiante():
    json_entrada = request.get_json()

    if request.method == "POST":
        try:
            if 'Estudiantes' in json_entrada.keys():
                for item_estudiante in json_entrada['Estudiantes']:
                    for item_anio in item_estudiante['Años']:
                        for item_semestre in item_anio['Semestres']:
                            for item_curso in item_semestre['Cursos']:
                                carnet = item_estudiante['Carnet']
                                year = item_anio['Año']
                                semestre = item_semestre['Semestre']
                                codigo = item_curso['Codigo']
                                nombre = item_curso['Nombre']
                                creditos = item_curso['Creditos']
                                prerrequisitos = item_curso['Prerequisitos']
                                obligatorio = item_curso['Obligatorio']

                                aux = arbol.buscar(int(carnet))
                                aux.lista_anio.buscarAgregar(year)
                                auxYear = aux.lista_anio.buscar(year)
                                auxYear.lista_semestre.buscarAgregar(int(semestre))
                                auxB = auxYear.lista_semestre.buscar(int(semestre))
                                auxB.arbol_curso.insertar(int(codigo),nombre,creditos,prerrequisitos,obligatorio)
            return {
                "estado": 200,
                "mensaje": "Cursos estudiante agregado exitosamente"
            }
        except:
            return {
                "estado": 400,
                "mensaje": "Fallo al agregar cursos estudiante"
            }




@app.route('/recordatorios',methods=['post','update','get','delete'])
def recordatorios():
    json_entrada = request.get_json()
    if request.method == 'POST':
        carnet = json_entrada['Carnet']
        nombre = json_entrada['Nombre']
        descripcion = json_entrada['Descripcion']
        materia = json_entrada['Materia']
        fecha = json_entrada['Fecha']
        hora = json_entrada['Hora']
        estado = json_entrada['Estado']

        auxCarnet = int(carnet)
        auxHora = int(hora.replace(":00",""))
        auxFecha = fecha.split("/")
        aux = arbol.buscar(auxCarnet)
        aux.lista_anio.buscarAgregar(auxFecha[2])
        auxAnio = aux.lista_anio.buscar(auxFecha[2])
        auxAnio.lista_mes.buscarAgregar(auxFecha[1])
        auxMes = auxAnio.lista_mes.buscar(auxFecha[1])
        auxMes.matriz_tarea.buscarAgregar(int(auxFecha[0]), auxHora)
        auxMatriz = auxMes.matriz_tarea.buscarNodoMatriz(int(auxFecha[0]),auxHora)
        try:
            auxMatriz.lista_tarea.agregar(auxCarnet, nombre, descripcion, materia, fecha, hora, estado)
            return {
                "estado":200,
                "mensaje":"Se ingreso recordatorio"
            }
        except:
            return {
                "estado":400,
                "mensaje":"No se ingreso recordatorio"
            }
    elif request.method == "UPDATE":
        carnet = json_entrada['Carnet']
        nombre = json_entrada['Nombre']
        descripcion = json_entrada['Descripcion']
        materia = json_entrada['Materia']
        fecha = json_entrada['Fecha']
        hora = json_entrada['Hora']
        estado = json_entrada['Estado']
        id = json_entrada['Id']
        auxCarnet = int(carnet)
        auxHora = int(hora.replace(":00", ""))
        auxFecha = fecha.split("/")
        auxId = int(id)

        auxCarnet = int(carnet)
        auxHora = int(hora.replace(":00", ""))
        auxFecha = fecha.split("/")
        aux = arbol.buscar(auxCarnet)
        aux.lista_anio.buscarAgregar(auxFecha[2])
        auxAnio = aux.lista_anio.buscar(auxFecha[2])
        auxAnio.lista_mes.buscarAgregar(auxFecha[1])
        auxMes = auxAnio.lista_mes.buscar(auxFecha[1])
        auxMes.matriz_tarea.buscarAgregar(int(auxFecha[0]), auxHora)
        auxMatriz = auxMes.matriz_tarea.buscarNodoMatriz(int(auxFecha[0]), auxHora)

        try:
            auxLista = auxMatriz.lista_tarea.buscar(auxId)
            auxLista.nombre = nombre
            auxLista.descripcion = descripcion
            auxLista.materia = materia
            auxLista.estado = estado
            return {
                "estado":200,
                "mensaje":"Se modifico recordatorio"
            }
        except:
            return {
                "estado":400,
                "mensaje":"No se modifico recordatorio"
            }
    elif request.method == "GET":
        carnet = json_entrada['Carnet']
        fecha = json_entrada['Fecha'].split("/")
        hora = json_entrada['Hora']
        id = json_entrada['Id']

        auxCarnet = int(carnet)
        auxId = int(id)
        auxDia = int(fecha[0])
        auxHora = int(hora.replace(":00",""))

        aux = arbol.buscar(auxCarnet)
        auxAnio = aux.lista_anio.buscar(str(fecha[2]))
        auxMes = auxAnio.lista_mes.buscar(str(fecha[1]))
        auxMatriz = auxMes.matriz_tarea.buscarNodoMatriz(auxDia, auxHora)

        try:
            auxLista = auxMatriz.lista_tarea.buscar(auxId)
            return {
                "Estado":200,
                "carnet":str(auxLista.carnet),
                "nombre":str(auxLista.nombre),
                "descripcion":str(auxLista.descripcion),
                "materia":str(auxLista.materia),
                "fecha":str(auxLista.fecha),
                "hora":str(auxLista.hora),
                "estado":str(auxLista.estado)
            }
        except:
            return {
                "estado":400,
                "mensaje":"No se obtuvo informacion de recodatorio"
            }
    elif request.method == 'DELETE':
        carnet = json_entrada['Carnet']
        fecha = json_entrada['Fecha'].split("/")
        hora = json_entrada['Hora']

        auxCarnet = int(carnet)
        auxHora = int(hora.replace(":00", ""))

        aux = arbol.buscar(auxCarnet)
        auxAnio = aux.lista_anio.buscar(str(fecha[2]))
        auxMes = auxAnio.lista_mes.buscar(str(fecha[1]))

        try:
            auxMes.matriz_tarea.eliminar(int(fecha[0]),auxHora)
            return {
                "estado":200,
                "mensaje":"Se ha eliminado el recodatorio"
            }
        except:
            return {
                "estado": 400,
                "mensaje": "No se ha eliminado el recodatorio"
            }

# rutas
@app.route('/estudiante',methods=['post','update','delete','get'])
def estudiante():
    json_entrada = request.get_json()

    if request.method == "POST":
        carnet = json_entrada['carnet']
        dpi = json_entrada['DPI']
        nombre = json_entrada['nombre']
        carrera = json_entrada['carrera']
        correo = json_entrada['correo']
        password = json_entrada['password']
        creditos = json_entrada['creditos']
        edad = json_entrada['edad']
        auxCarnet = int(carnet)
        auxCred = int(creditos)
        auxEdad = int(edad)
        try:
            arbol.insertar(auxCarnet,dpi,nombre,carrera,correo,password,auxCred,auxEdad)
            return {
                "estado": 200,
                "mensaje": "Se ingreso estudiante"
            }
        except:
            return {
                "estado": 400,
                "mensaje": "No se ingreso estudiante"
            }
    elif request.method == 'UPDATE':
        carnet = json_entrada['carnet']
        dpi = json_entrada['DPI']
        nombre = json_entrada['nombre']
        carrera = json_entrada['carrera']
        correo = json_entrada['correo']
        password = json_entrada['password']
        creditos = json_entrada['creditos']
        edad = json_entrada['edad']
        auxCarnet = int(carnet)
        auxCred = int(creditos)
        auxEdad = int(edad)
        try:
            arbol.modificar(auxCarnet,dpi,nombre,carrera,correo,password,auxCred,auxEdad)
            return {
                "estado": 200,
                "mensaje": "Se modifico estudiante"
            }
        except:
            return {
                "estado": 400,
                "mensaje": "No se modifico estudiante"
            }
    elif request.method == "DELETE":
        carnet = json_entrada['carnet']
        auxCarnet = int(carnet)
        try:
            arbol.eliminar(auxCarnet)
            return {
                "estado": 200,
                "mensaje": "Se elimino estudiante"
            }
        except:
            return {
                "estado": 400,
                "mensaje": "No se elimino estudiante"
            }
    elif request.method == "GET":
        carnet = json_entrada['carnet']
        auxCarnet = int(carnet)

        try:
            aux = arbol.buscar(auxCarnet)
            return {
                "Estado": 200,
                "carnet": str(aux.carnet),
                "dpi":str(aux.dpi),
                "nombre":str(aux.nombre),
                "carrera":str(aux.carrera),
                "correo":str(aux.correo),
                "password":str(aux.password),
                "creditos":str(aux.creditos),
                "edad":str(aux.edad)
            }
        except:
            return {
                "estado": 400,
                "mensaje": "No se obtuvo informacion"
            }

@app.route('/reporte',methods=['get'])
def reporte():
    if request.method == "GET":
        json_entrada = request.get_json()
        tipo = json_entrada['tipo']

        if tipo == 0:
            try:
                print("alv")
                arbol.generadorGrafica()
                return {
                    "estado":200,
                    "mensaje":"Se genero la grafica avl"
                }
            except:
                return {
                    "estado":400,
                    "mensaje":"No se genero la grafica avl"
                }
        elif(tipo == 1):
            carnet = json_entrada['carnet']
            year = json_entrada["anio"]
            mes = json_entrada['mes']
            try:

                auxCarnet = int(carnet)
                auxMes = str(mes)
                aux = arbol.buscar(auxCarnet)
                aux2 = aux.lista_anio.buscar(str(year))
                aux3 = aux2.lista_mes.buscar(str(auxMes))
                aux3.matriz_tarea.graficar()

                return {
                    "estado":200,
                    "mensaje":"Se genero la grafica matriz"
                }
            except:
                return {
                    "estado":400,
                    "mensaje":"No se genero la grafica matriz"
                }
        elif(tipo == 2):
            carnet = json_entrada['carnet']
            year = json_entrada["anio"]
            mes = json_entrada['mes']
            dia = json_entrada['dia']
            hora = json_entrada['hora']
            try:
                auxCarnet = int(carnet)
                auxDia = int(dia)
                auxHora = int(hora)
                auxMes = str(mes)
                aux = arbol.buscar(auxCarnet)
                aux2 = aux.lista_anio.buscar(str(year))
                aux3 = aux2.lista_mes.buscar(auxMes)
                aux4 = aux3.matriz_tarea.buscarNodoMatriz(auxDia,auxHora)
                aux4.lista_tarea.graficar()

                return {
                    "estado":200,
                    "mensaje":"Se genero la grafica lista tareas"
                }
            except:
                return {
                    "estado":400,
                    "mensaje":"No se genere la grafica lista tareas"
                }
        elif tipo == 3:
            try:
                arbolCursos.graficar()
                return {
                    "estado":200,
                    "mensaje":"Grafica cursos pensum generado exitosamente"
                }
            except:
                return {
                    "estado":400,
                    "mensaje":"Grafica de cursos pensum fallido"
                }
        elif (tipo == 4):
            carnet = json_entrada['carnet']
            year = json_entrada['año']
            semestre = json_entrada['semestre']

            aux = arbol.buscar(int(carnet))
            auxAnio = aux.lista_anio.buscar(year)
            auxSemestre = auxAnio.lista_semestre.buscar(int(semestre))
            try:
                auxSemestre.arbol_curso.graficar()
                return {
                    "estado":200,
                    "mensaje":"Grafica de semestre exitoso"
                }
            except:
                return {
                    "estado":400,
                    "mensaje":"Grafica de semestre fallido"
                }

@app.route('/carga', methods=['post'])
def carga():
    if request.method == "POST":
        json_entrada = request.get_json()
        tipo = json_entrada['tipo']
        path = json_entrada['path']
        print(path)
        if tipo == "estudiantes":
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
                            auxMes.matriz_tarea.buscarAgregar(int(fecha[0]),int(hora))
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

        elif tipo == "cursos estudiantes":

            archivo = open(path, "r", encoding="utf-8")
            datos = json.load(archivo)
            try:
                if 'Estudiantes' in datos.keys():
                    for item_student in datos['Estudiantes']:
                        for item_anio in item_student['Años']:
                            for item_semestre in item_anio['Semestres']:
                                for item_curso in item_semestre['Cursos']:
                                    carnet = item_student['Carnet']
                                    year = item_anio['Año']
                                    semestre = item_semestre['Semestre']
                                    codigo = item_curso['Codigo']
                                    nombre = item_curso['Nombre']
                                    creditos = item_curso['Creditos']
                                    cursoPre = item_curso['Prerequisitos']
                                    obligatorio = item_curso['Obligatorio']

                                    aux = arbol.buscar(int(carnet))
                                    aux.lista_anio.buscarAgregar(year)
                                    auxYear = aux.lista_anio.buscar(year)
                                    auxYear.lista_semestre.buscarAgregar(int(semestre))
                                    auxB = auxYear.lista_semestre.buscar(int(semestre))
                                    auxB.arbol_curso.insertar(int(codigo),nombre,creditos,cursoPre,obligatorio)

                return {
                    "estado":200,
                    "mensaje":"Carga de cursos estudiantes exitoso"
                }
            except:
                return {
                    "estado":400,
                    "mensaje":"Carga de cursos estudiantes fallido"
                }
        elif tipo == "cursos pensum":
            archivo = open(path, "r", encoding="utf-8")
            datos = json.load(archivo)

            try:
                for item in datos['Cursos']:
                    codigo = item['Codigo']
                    nombre = item['Nombre']
                    creditos = item['Creditos']
                    pre = item['Prerequisitos']
                    obligatorio = item['Obligatorio']
                    arbolCursos.insertar(int(codigo),nombre,creditos,pre,obligatorio)

                return {
                    "estado":200,
                    "mensaje":"Carga de cursos pensum exitoso"
                }
            except:
                return {
                    "estado":400,
                    "mensaje":"Carga de cursos pensum fallido"
                }
# ejecutar
app.run(host='0.0.0.0', port=3000, debug=True)
