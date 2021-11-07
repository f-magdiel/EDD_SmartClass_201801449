import os
import sys
class Nodo:
    def __init__(self, indice,nombre,creditos,prerrequisitos,obligatorio):
        self.indice = indice
        self.nombre = nombre
        self.creditos = creditos
        self.prerrequisitos = prerrequisitos 
        self.obligatorio = obligatorio
        self.siguiente = None
        self.lista_ad = lista_ady()

class lista_ady:
    def __init__(self):
        self.Inicio = None
        self.Ultimo = None

    def insercion_Grafo(self, indice,nombre,creditos,prerrequisitos,obligatorio):
        # crear nuevo nodo
        nuevo = Nodo(indice,nombre,creditos,prerrequisitos,obligatorio)

        if self.Inicio == None:
            self.Inicio = nuevo
            self.Ultimo = nuevo
        else:
            self.Ultimo.siguiente = nuevo
            self.Ultimo = nuevo


class Grafo:
    def __init__(self):
        self.Inicio = None
        self.Ultimo = None

    def insercion_Grafo(self, indice,nombre,creditos,prerrequisitos,obligatorio):
        # crear nuevo nodo
        nuevo = Nodo(indice,nombre,creditos,prerrequisitos,obligatorio)

        if self.Inicio == None:
            self.Inicio = nuevo
            self.Ultimo = nuevo
        else:
            self.Ultimo.siguiente = nuevo
            self.Ultimo = nuevo

    def buscar(self, indice):
        aux = self.Inicio
        while aux:
            if aux.indice == indice:
                return aux
            else:
                aux = aux.siguiente
        return None

    def insertar_adya(self, indice_nodo, adyasente):
        nodo_principal = self.buscar(indice_nodo)
        nodo_ad = self.buscar(adyasente)
        if nodo_ad == None:
            self.insercion_Grafo(nodo_ad.indice,nodo_ad.nombre,nodo_ad.creditos,nodo_ad.prerrequisitos,nodo_ad.obligatorio)
        if nodo_principal:
            lista_ad = nodo_principal.lista_ad
            lista_ad.insercion_Grafo(nodo_ad.indice,nodo_ad.nombre,nodo_ad.creditos,nodo_ad.prerrequisitos,nodo_ad.obligatorio)
            print("se agrego el adyasente")
        else:
            print("no se encontro el nodo origen")

    def mostrar_Grafo(self):
        aux = self.Inicio
        while aux:

            lista_ad = aux.lista_ad
            info = ""
            if lista_ad.Inicio:
                aux2 = lista_ad.Inicio
                while aux2 != None:
                    info += "-> " + str(aux2.indice)
                    aux2 = aux2.siguiente

            print("-", aux.indice, info)
            aux = aux.siguiente

    def graficar(self):
        cadena = "digraph pensum {\n rankdir=\"LR\";\n"
        cadena+= 'node[shape = box,style="rounded,filled",fillcolor=lightblue2];\n'
        # recorer los nodos para imprimirlos
        aux = self.Inicio
        while aux:
            cadena += "n" + str(aux.indice) + "[label= \"" + str(aux.indice) +"\\n"+str(aux.nombre)+ "\"];\n"
            aux = aux.siguiente

        # gaficar enlaces
        aux = self.Inicio
        while aux:
            aux2 = aux.lista_ad.Inicio
            while aux2:
                cadena += "n" + str(aux.indice) + " -> n" + str(aux2.indice) + ";\n"
                aux2 = aux2.siguiente
            aux = aux.siguiente
        cadena += "}"
        Archivo = open("C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\grafo_pensum.dot","w",encoding="UTF-8")
        Archivo.write(cadena)
        Archivo.close()
        os.system("dot -Tpng C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\grafo_pensum.dot -o C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\grafo_pensum.png")

    def graficarCodigo(self,codigo):
        nodo_nuevo = self.Inicio
        cadena = "digraph pensum {\n rankdir=\"LR\";\n"
        cadena+= 'node[shape = box,style="rounded,filled",fillcolor=lightblue2];\n'
        # recorer los nodos para imprimirlos
        aux = nodo_nuevo
        while aux:
            
            if codigo ==aux.indice:
                cadena += "n" + str(aux.indice) + "[label= \"" + str(aux.indice) +"\\n"+str(aux.nombre)+"\""+",fillcolor=brown1" +"];\n"
                aux = aux.siguiente
            else:
                cadena += "n" + str(aux.indice) + "[label= \"" + str(aux.indice) +"\\n"+str(aux.nombre)+ "\"];\n"
                aux = aux.siguiente
        
        # gaficar enlaces
        aux = nodo_nuevo
        while aux:
            aux2 = aux.lista_ad.Inicio
            while aux2:
                cadena += "n" + str(aux.indice) + " -> n" + str(aux2.indice) + ";\n"
                aux2 = aux2.siguiente
            aux = aux.siguiente
        cadena += "}"
        Archivo = open("C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\grafo_pensum_estudiante.dot","w",encoding="UTF-8")
        Archivo.write(cadena)
        Archivo.close()
        os.system("dot -Tpng C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\grafo_pensum_estudiante.dot -o C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\grafo_pensum_estudiante.png")


""" graph = Grafo()
graph.insercion_Grafo(20,"magdiel",10,"11,12",True)
graph.insercion_Grafo(10,"uno",13,"11,12",True)
graph.insercion_Grafo(21,"dos",14,"11,12",True)
graph.insercion_Grafo(23,"tres",9,"11,12",True)
graph.insertar_adya(20,10)
graph.insertar_adya(10,21)
graph.insertar_adya(20,23)
graph.graficar()
graph.graficarCodigo(10) """