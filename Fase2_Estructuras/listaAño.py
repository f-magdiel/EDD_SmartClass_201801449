import os
import sys
from Fase2_Estructuras.ListaSemestre import *
from Fase2_Estructuras.ListaMes import *
class Nodo:
    def __init__(self,_year):
        self.year = _year
        self.siguiente = None
        self.anterior = None
        self.lista_semestre = listaSemestre()
        self.lista_mes = listaMes()


class listaAño:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contGen = 0

    def agregar(self,_year):
        nuevoNodo = Nodo(_year)
        if(self.cabeza==None):
            self.cabeza = nuevoNodo

        else:
            actual = self.cabeza
            while(actual.siguiente!=None):
                actual = actual.siguiente

            actual.siguiente = nuevoNodo
            nuevoNodo.anterior = actual
            self.cola = nuevoNodo

    def buscar(self,_year):
        actual = self.cabeza
        while(actual!=None):
            if(_year == actual.year):
                return actual.year
            
            actual = actual.siguiente

        return None


    def buscarAgregar(self,_year):
        actual = self.cabeza
        banderaRepetido = False
        while(actual!=None):
            if(_year==actual.year):
                banderaRepetido = True
                break

            actual = actual.siguiente

        if(banderaRepetido == True):
            print("Dato ya existe")
        else:
            self.agregar(_year) #en este metodo se agrega si no hay repeat en la lista

    def actualizar(self,_year,_sustituto):
        actual = self.cabeza
        while(actual!=None):
            if(_year == actual.year):
                actual.year = _sustituto
                break
            actual = actual.siguiente

    def eliminar(self,_year):
        actual = self.cabeza
        encontrado = False

        while((actual!=None) and (encontrado == False)):
            encontrado = (actual.year == _year)
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
        name = "lista_año"+str(self.contGen)
        file = open("Graficas/"+name+".dot","w",encoding="UTF-8")
        file.write("digraph G{\n")
        file.write("rankdir=LR;\n")
        file.write('node[shape = record,style="rounded,filled",fillcolor=lightblue2];\n')
        aux = self.cabeza
        while(aux!=None):
            file.write(str(aux.year)+"[label=\"{*|"+"Año:"+str(aux.year)+"|*}\"];\n")
            aux = aux.siguiente

        edge = self.cabeza
        while(edge!=None):
            if(edge.siguiente!=None):
                aux = edge
                aux = aux.siguiente
                file.write(str(edge.year)+"->"+str(aux.year)+";\n")
                file.write(str(aux.year)+"->"+str(edge.year)+";\n")
            edge = edge.siguiente

        file.write("\n}")
        file.close()
        os.system("dot -Tsvg Graficas/"+name+".dot -o Graficas/"+name+".svg")

lista = listaAño()
'''
lista.buscarAgregar(2012)
lista.buscarAgregar(2013)
lista.buscarAgregar(2014)
lista.buscarAgregar(2015)
lista.buscarAgregar(2016)
lista.graficar()
lista.eliminar(2012)
lista.graficar()
print("Fin")
'''