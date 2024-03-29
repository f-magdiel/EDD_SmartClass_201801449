import os
import sys
from Fase2_Estructuras.ArbolCursos import *
class Nodo:
    def __init__(self,_semestre):
        self.semestre = _semestre
        self.siguiente = None
        self.anterior = None
        self.arbol_curso = Arbolb()


class listaSemestre:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.posicion = 0
        self.contGen = 0

    def agregar(self,_semetre):
        self.posicion +=1 
        nuevoNodo = Nodo(_semetre)
        if(self.cabeza==None):
            self.cabeza = nuevoNodo

        else:
            actual = self.cabeza
            while(actual.siguiente!=None):
                actual = actual.siguiente

            actual.siguiente = nuevoNodo
            nuevoNodo.anterior = actual
            self.cola = nuevoNodo

    def buscar(self,_semestre):
        actual = self.cabeza
        while(actual!=None):
            if(_semestre == actual.semestre):
                return actual
            
            actual = actual.siguiente

        return None


    def buscarAgregar(self,_semestre):
        actual = self.cabeza
        banderaRepetido = False
        while(actual!=None):
            if(_semestre==actual.semestre):
                banderaRepetido = True
                break

            actual = actual.siguiente

        if(banderaRepetido == True):
            print("Semestre ya existe")
            return actual
        else:
            if(self.posicion == 2):
                print("Posiciones ocupadas")
            else:
                self.agregar(_semestre) #en este metodo se agrega si no hay repeat y posiciones disponibles

    def actualizar(self,_semestre,_sustituto):
        actual = self.cabeza
        while(actual!=None):
            if(_semestre == actual.semestre):
                actual.semestre = _sustituto
                break
            actual = actual.siguiente

    def eliminar(self,_semestre):
        actual = self.cabeza
        encontrado = False

        while((actual!=None) and (encontrado == False)):
            encontrado = (actual.semestre == _semestre)
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
        name = "lista_semestre"+str(self.contGen)
        file = open("C:\\Users\\Magdiel\\Desktop\\Reportes_F2\\"+name+".dot","w",encoding="UTF-8")
        file.write("digraph G{\n")
        file.write("rankdir=LR;\n")
        file.write('node[shape = record,style="rounded,filled",fillcolor=lightblue2];\n')
        aux = self.cabeza
        num = 0
        while(aux!=None):
            num+=1
            file.write("S"+str(num)+"[label=\"{*|"+str(aux.semestre)+"|*}\"];\n")
            aux = aux.siguiente

        file.write("S1->S2;\n")
        file.write("S2->S1;\n")
        file.write("\n}")
        file.close()
        os.system("dot -Tsvg C:\\Users\\Magdiel\\Desktop\\Reportes_F2\\"+name+".dot -o C:\\Users\\Magdiel\\Desktop\\Reportes_F2\\"+name+".svg")
'''
lista = listaSemestre()

lista.buscarAgregar("Semestre 1")
lista.buscarAgregar("Semestre 2")
lista.graficar()
print("Fin")
'''