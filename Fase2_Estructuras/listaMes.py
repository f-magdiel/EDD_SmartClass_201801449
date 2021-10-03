import os
import sys
from Fase2_Estructuras.MatrizTarea import *
class Nodo:
    def __init__(self,_mes):
        self.mes = _mes
        self.siguiente = None
        self.anterior = None
        self.matriz_tarea = matriz(_mes)


class listaMes:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contGen = 0

    def agregar(self,_mes):
        print("Ingreso en mes")
        nuevoNodo = Nodo(_mes)
        if(self.cabeza==None):
            self.cabeza = nuevoNodo

        else:
            actual = self.cabeza
            while(actual.siguiente!=None):
                actual = actual.siguiente

            actual.siguiente = nuevoNodo
            nuevoNodo.anterior = actual
            self.cola = nuevoNodo

    def buscar(self,_mes):
        actual = self.cabeza
        while(actual!=None):
            if(_mes == actual.mes):
                return actual
            
            actual = actual.siguiente

        return None


    def buscarAgregar(self,_mes):
        actual = self.cabeza
        banderaRepetido = False
        while(actual!=None):
            if(_mes==actual.mes):
                banderaRepetido = True
                break

            actual = actual.siguiente

        if(banderaRepetido == True):
            print("Mes ya existe")
            return actual
        else:
            self.agregar(_mes) #en este metodo se agrega si no hay repeat en la lista

    def actualizar(self,_mes,_sustituto):
        actual = self.cabeza
        while(actual!=None):
            if(_mes == actual.mes):
                actual.mes = _sustituto
                break
            actual = actual.siguiente

    def eliminar(self,_mes):
        actual = self.cabeza
        encontrado = False

        while((actual!=None) and (encontrado == False)):
            encontrado = (actual.mes == _mes)
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
        self.contGen += 1
        name = "lista_mes"+str(self.contGen)
        file = open("C:\\Users\\Magdiel\\Desktop\\Reportes_F2\\"+name+".dot","w",encoding="UTF-8")
        file.write("digraph G{\n")
        file.write("rankdir=LR;\n")
        file.write('node[shape = record,style="rounded,filled",fillcolor=lightblue2];\n')
        aux = self.cabeza
        while(aux!=None):
            file.write(str(aux.mes)+"[label=\"{*|"+"Mes:"+str(aux.mes)+"|*}\"];\n")
            aux = aux.siguiente

        edge = self.cabeza
        while(edge!=None):
            if(edge.siguiente!=None):
                aux = edge
                aux = aux.siguiente
                file.write(str(edge.mes)+"->"+str(aux.mes)+";\n")
                file.write(str(aux.mes)+"->"+str(edge.mes)+";\n")
            edge = edge.siguiente

        file.write("\n}")
        file.close()
        os.system("dot -Tsvg C:\\Users\\Magdiel\\Desktop\\Reportes_F2\\"+name+".dot -o C:\\Users\\Magdiel\\Desktop\\Reportes_F2\\"+name+".svg")
            
'''
lista = listaMes()

lista.buscarAgregar("07")
lista.buscarAgregar("08")
lista.buscarAgregar("09")
lista.buscarAgregar("10")
lista.buscarAgregar("11")
lista.graficar()
lista.eliminar("08")
lista.graficar()
print("Fin")
'''