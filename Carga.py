from analizador.sintactico import parser

def cargaDatos(tipo,path):
    #path = "C:\\Users\\Magdiel\\Desktop\\Archivos de prueba\\Estudiantes.txt"
    f = open(path,"r", encoding="utf-8")
    mensaje = f.read()
    f.close()
    
    resultado_analisis= parser.parse(mensaje)

    if(tipo == "estudiante"):
        for item in resultado_analisis:

            if(item["type"] == "user"):
                atributos = item["atributos"]
                carnet = int(atributos[0]["Carnet"].replace("\"",""))
                dpi = int(atributos[1]["DPI"].replace("\"",""))
                nombre = atributos[2]["Nombre"].replace("\"","")
                carrera = atributos[3]["Carrera"].replace("\"","")
                correo = atributos[4]["Correo"].replace("\"","")
                password = atributos[5]["Password"].replace("\"","")
                creditos = int(atributos[6]["Creditos"])
                edad = int(atributos[7]["Edad"])
               #Insercion en avl estudiantes
                #avl.insertar(carnet,dpi,nombre,carrera,correo,password,creditos,edad)
            elif(item["type"] == "task"):
                atributos = item["atributos"]
                carnet = int(atributos[0]["Carnet"].replace("\"",""))
                nombre = atributos[1]["Nombre"].replace("\"","")
                descripcion = atributos[2]["Descripcion"].replace("\"","")
                materia = atributos[3]["Materia"].replace("\"","")
                fecha = atributos[4]["Fecha"].replace("\"","").split("/")
                hora = atributos[5]["Hora"].replace("\"","")
                estado = atributos[6]["Estado"].replace("\"","")
                print(carnet)
                #Insercion de tareas y años, meses
                #auxEstudiante = avl.buscar(carnet)
                #auxEstudiante.lista_año.agregar(fecha[2]) #se manda el año a agregar
                #auxAnio = auxEstudiante.lista_año.buscar(fecha[2])
               # auxAnio.lista_mes.buscarAgregar(fecha[1]) #se manda el mes a agregar


    elif(tipo=="curso"):
        print('hola')

