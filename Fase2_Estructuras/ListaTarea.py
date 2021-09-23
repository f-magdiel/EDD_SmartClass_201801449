import os
import sys
class Nodo:
    def __init__(self,_id,_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado):
        self.id = _id
        self.carnet = _carnet
        self.nombre = _nombre
        self.descripcion = _descripcion
        self.materia = _materia
        self.fecha = _fecha
        self.hora = _hora
        self.estado = _estado
        self.siguiente = None
        self.anterior = None
        #apuntador semestre
        #apuntador mes


class listatarea:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.gentID = 0
        self.contGen = 0
        

    def agregar(self,_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado):
        self.gentID += 1
        nuevoNodo = Nodo(self.gentID,_carnet,_nombre,_descripcion,_materia,_fecha,_hora,_estado)
        if(self.cabeza==None):
            self.cabeza = nuevoNodo

        else:
            actual = self.cabeza
            while(actual.siguiente!=None):
                actual = actual.siguiente

            actual.siguiente = nuevoNodo
            nuevoNodo.anterior = actual
            self.cola = nuevoNodo

    def buscar(self,_id):
        actual = self.cabeza
        while(actual!=None):
            if(_id == actual.id):
                return actual.id
            
            actual = actual.siguiente

        return None



    def actualizar(self,_id,_carnet,_nombre,_descripcion,_materia,_estado):
        actual = self.cabeza
        while(actual!=None):
            if(_id == actual.id):
                actual.carnet = _carnet
                actual.nombre = _nombre
                actual.descripcion = _descripcion
                actual.materia = _materia
                actual.estado = _estado
                break
            actual = actual.siguiente

    def eliminar(self,_id):
        actual = self.cabeza
        encontrado = False

        while((actual!=None) and (encontrado == False)):
            encontrado = (actual.id == _id)
            if(encontrado == False):
                actual = actual.siguiente

        if(actual!=None):
            if(actual == self.cabeza):
                self.cabeza = actual.siguiente
                if(actual.siguiente!=None):
                    actual.siguiente.anterior = None
            elif(actual.siguiente!=None):
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
            else:
                actual.anterior.siguiente = None
                self.cola = actual.anterior
                actual = None

    def graficar(self):
        self.contGen +=1
        name = "Lista_Tarea"+str(self.contGen)
        file = open("Graficas/"+name+".dot","w",encoding="UTF-8")
        file.write("digraph G{\n")
        file.write("rankdir=LR;")
        file.write('node[shape = record,style="rounded,filled",fillcolor=lightblue2];\n')
        aux = self.cabeza
        while(aux!=None):
            file.write(str(aux.id)+"[label =\"{*|"+"ID:"+str(aux.id)+"\\n Carnet:"+str(aux.carnet)+"\\n Nombre:"+str(aux.nombre)+"\\n Descripcion:"+str(aux.descripcion)+"\\n Materia:"+str(aux.materia)+"\\n Fecha:"+str(aux.fecha)+"\\n Hora:"+str(aux.hora)+"\\n Estado:"+str(aux.estado)+"|*}\"];\n")
            aux = aux.siguiente

        edge = self.cabeza
        while(edge!=None):
            if(edge.siguiente!=None):
                file.write(str(edge.id)+"->"+str(edge.id+1)+";\n")
                file.write(str(edge.id+1)+"->"+str(edge.id)+";\n")
            
            edge = edge.siguiente

        file.write("\n}")
        file.close()
        os.system("dot -Tsvg Graficas/"+name+".dot -o Graficas/"+name+".svg")

tarea = listatarea()
tarea.agregar(20180149,"Tarea Matematica 1","Realizar","Matematica 1","01/02/2012","8:00","Incumplido")
tarea.agregar(20180149,"Tarea Matematica 2","Realizar","Matematica 2","01/02/2012","8:00","Incumplido")
tarea.agregar(20180149,"Tarea Matematica 3","Realizar","Matematica 3","01/02/2012","8:00","Incumplido")
tarea.agregar(20180149,"Tarea Matematica 4","Realizar","Matematica 4","01/02/2012","8:00","Incumplido")
tarea.agregar(20180149,"Tarea Matematica 5","Realizar","Matematica 5","01/02/2012","8:00","Incumplido")
tarea.graficar()
print(tarea.buscar(2))
tarea.actualizar(1,202101449,"Logica","Realizar","Logica","Incumplido")
tarea.graficar()
tarea.eliminar(1)
tarea.graficar()