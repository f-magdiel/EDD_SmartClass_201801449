import os
import sys
from Fase2_Estructuras.ListaTarea import *
class Nodo:
    def __init__(self, valor, x,y):
        self.valor = valor
        self.pos_x = x
        self.pos_y = y

        #apuntadores
        self.ant = None
        self.sig = None

        self.arriba = None
        self.abajo = None

        self.lista_tarea = listatarea()

class Lista:
    def __init__(self):
        self.primero = None

    def insertar_x(self, valor, x,y):
        nuevo = Nodo(valor,x,y)

        if self.primero:
            if nuevo.pos_y < self.primero.pos_y:
                nuevo.sig = self.primero
                self.primero.ant = nuevo
                self.primero = nuevo
            else:
                aux = self.primero
                while aux:
                    if nuevo.pos_y < aux.pos_y:
                        nuevo.sig = aux
                        nuevo.ant = aux.ant
                        aux.ant.sig = nuevo
                        aux.ant = nuevo
                        break
                    elif nuevo.pos_x == aux.pos_x and nuevo.pos_y == aux.pos_y:
                        print("ya esta ocupada esa posicion")
                        break
                    else: 
                        if aux.sig == None:
                            aux.sig = nuevo
                            nuevo.ant = aux
                            break
                        else:
                            aux = aux.sig
        else: #si esta vacia se asigna nuevo al primero
            self.primero = nuevo
    
    def insertar_y(self, valor, x,y):
        nuevo = Nodo(valor,x,y)

        if self.primero:
            if nuevo.pos_x < self.primero.pos_x:
                nuevo.abajo = self.primero
                self.primero.arriba = nuevo
                self.primero = nuevo
            else:
                aux = self.primero
                while aux:
                    if nuevo.pos_x < aux.pos_x:
                        nuevo.abajo = aux
                        nuevo.arriba = aux.ant
                        aux.arriba.abajo = nuevo
                        aux.arriba = nuevo
                        break
                    elif nuevo.pos_x == aux.pos_x and nuevo.pos_y == aux.pos_y:
                        print("ya esta ocupada esa posicion")
                        break
                    else: 
                        if aux.abajo == None:
                            aux.abajo = nuevo
                            nuevo.arriba = aux
                            break
                        else:
                            aux = aux.abajo
        else: #si esta vacia se asigna nuevo al primero
            self.primero = nuevo

    def recorrer(self):
        aux = self.primero
        while aux:
            print("valor =",aux.valor," - x = ",aux.pos_x , " y = ",aux.pos_y)
            aux = aux.sig              

    def buscarNodo(self,x,y):
        aux = self.primero
        while aux:
            if(aux.pos_x == x and aux.pos_y == y):
                return aux
            aux = aux.sig
            print("No se encontro")
            return None

#lista cabeceras
class NodoCabecera:
    def __init__(self, pos):
        self.posicion = pos
        self.sig = None
        self.ant = None
        self.lista_interna = Lista()

class ListaCabecera:
    def __init__(self):
        self.primero = None
    
    def insertar(self, nuevo):
        if self.primero:
            if nuevo.posicion < self.primero.posicion:
                nuevo.sig = self.primero
                self.primero.ant = nuevo
                self.primero = nuevo
            else:
                aux = self.primero
                while aux:
                    if nuevo.posicion < aux.posicion:
                        nuevo.sig = aux
                        nuevo.ant = aux.ant
                        aux.ant.sig = nuevo
                        aux.ant = nuevo
                        break
                    else: 
                        if aux.sig == None:
                            aux.sig = nuevo
                            nuevo.ant = aux
                            break
                        else:
                            aux = aux.sig
        else: #si esta vacia se asigna nuevo al primero
            self.primero = nuevo

    def buscarCabecera(self,dato):
        aux = self.primero
        while aux:
            if aux.posicion == dato:
                return aux
            else:
                aux = aux.sig
        return None

    def recorrer(self):
        aux = self.primero
        while aux:
            print(aux.posicion)
            aux = aux.sig
        

class matriz:
    def __init__(self, mes):
        self.mes = mes
        self.cabeceras_X= ListaCabecera()
        self.cabeceras_y = ListaCabecera()
        self.contMat = 0

    def insertar(self, valor,posx,posy):
        nodo_cabecera_x=None 
        nodo_cabecera_y=None

        if self.cabeceras_X and self.cabeceras_y:
            nodo_cabecera_x = self.cabeceras_X.buscarCabecera(posx)
            nodo_cabecera_y = self.cabeceras_y.buscarCabecera(posy)

        if nodo_cabecera_x == None:
            nodo_cabecera_x = NodoCabecera(posx)
            self.cabeceras_X.insertar(nodo_cabecera_x)
        
        if nodo_cabecera_y == None:
            nodo_cabecera_y = NodoCabecera(posy)
            self.cabeceras_y.insertar(nodo_cabecera_y)

        #ya que nos aseguramos que tengamos las cabeceras necesarias, procedemos a insertar el nodo interno
        #insertamos en X
        nodo_cabecera_x.lista_interna.insertar_x(valor,posx,posy)
        #insertar en Y
        nodo_cabecera_y.lista_interna.insertar_y(valor,posx,posy)

    def recorrer_matriz(self):
        print("#cabeceras en x")
        aux = self.cabeceras_X.primero
        while aux:
            print("     pos-> ",aux.posicion) 
            aux2 = aux.lista_interna.primero
            while aux2:
                print("         -", aux2.valor)
                aux2 = aux2.sig

            aux = aux.sig

        print("#cabeceras en Y")
        aux = self.cabeceras_y.primero
        while aux:
            print("     pos-> ",aux.posicion) 
            aux2 = aux.lista_interna.primero
            while aux2:
                print("         -", aux2.valor)
                aux2 = aux2.abajo
                
            aux = aux.sig

    def buscarNodoMatriz(self,posx,posy):
        aux1 = self.cabeceras_X.buscarCabecera(posx)
        if(aux1 != None):
            aux2 = aux1.lista_interna.buscarNodo(posx,posy)
            if(aux2!=None):
                return aux2.valor
            else:
                return None
        else:
            return None

    def graficar(self):
        self.contMat += 1
        name = "Matriz"+str(self.contMat)
        file = open("Graficas/"+name+".dot", "w", encoding="UTF-8")
        file.write("digraph G{\n")
        file.write("rankdir=TB  \n")
        file.write("node[shape = box,color=\"lightblue2\" style=\"filled\"];\n")
        file.write("edge[style = \"bold\"]; \n")

        inicio = self.cabeceras_X.primero
        posx = 0
        while (inicio != None):
            file.write("\n\tnode[label = \"C:"+str(inicio.posicion)+"\" fillcolor=\" dodgerblue4\" pos = \""+str(posx)+",1!\" shape = box]X"+str(inicio.posicion)+";"+"\n")
            inicio = inicio.sig
            posx += 1
        
        aux2 = self.cabeceras_X.primero
        while (aux2.sig!=None):
            file.write("X"+str(aux2.posicion)+" -> "+"X"+str(aux2.sig.posicion)+"\n")
            file.write("X" + str(aux2.sig.posicion) + " -> " + "X" + str(aux2.posicion)+"\n")
            aux2 = aux2.sig


        inicioy = self.cabeceras_y.primero
        posy = 0
        while (inicioy != None):
            file.write("\n\tnode[label = \"F:" + str(inicioy.posicion) + "\" fillcolor=\" dodgerblue4\" pos = \""+"-1,-" + str(posy) +"!\" shape = box]Y" + str(inicioy.posicion) + ";" + "\n")
            inicioy = inicioy.sig
            posy+=1
        inicioy = self.cabeceras_y.primero
        while (inicioy.sig != None):
            file.write("Y" + str(inicioy.posicion) + " -> " + "Y" + str(inicioy.sig.posicion)+"\n")
            file.write("Y" + str(inicioy.sig.posicion) + " -> " + "Y" + str(inicioy.posicion)+"\n")
            inicioy = inicioy.sig

        #----------- DATOS INTERNOS -------------------
        inicio = self.cabeceras_X.primero
        posx = 0
        while(inicio!=None):
            inicio_interno = inicio.lista_interna.primero
            while(inicio_interno!=None):
                inicioy = self.cabeceras_y.primero
                posy_interno = 0
                while(inicioy!=None):
                    if(inicioy.posicion==inicio_interno.pos_y):
                        break
                    posy_interno+=1
                    inicioy=inicioy.sig

                file.write("\n\tnode[label = \""+str(inicio_interno.pos_x)+ ","+str(inicio_interno.pos_y)+"\n"+"T: "+str(inicio_interno.valor)+" \n \" fillcolor=\" azure2\" pos = \"" + str(posx) + ",-" + str(posy_interno) + "!\" shape = box]\"i" + str(inicio_interno.pos_x) + "-" + str(inicio_interno.pos_y) + "\";")
                inicio_interno = inicio_interno.sig
            inicio_interno = inicio.lista_interna.primero

            while (inicio_interno != None):
                if (inicio_interno.sig != None):#           0                        0                                                    0                           1
                    file.write("\n \"i" + str(inicio_interno.pos_x) + "-" + str(inicio_interno.pos_y) + "\" -> \"i" + str(inicio_interno.sig.pos_x) + "-" + str(inicio_interno.sig.pos_y) + "\";\n")
                    file.write("\"i" + str(inicio_interno.sig.pos_x) + "-" + str(inicio_interno.sig.pos_y) + "\" -> \"i" + str(inicio_interno.pos_x) + "-" + str(inicio_interno.pos_y) + "\";\n")
                inicio_interno = inicio_interno.sig                                                                                                                 #quitare el .sig
            file.write("\n X" + str(inicio.posicion) + " -> \"i" + str(inicio.lista_interna.primero.pos_x) + "-" + str(inicio.lista_interna.primero.pos_y) + "\" \n")
            file.write("\n \"i" + str(inicio.lista_interna.primero.pos_x) + "-" + str(inicio.lista_interna.primero.pos_y) + "\"-> X" + str(inicio.posicion) + "  \n")
            inicio = inicio.sig
            posx+=1

        inicio=self.cabeceras_y.primero
        while(inicio!=None):
            inicio_interno=inicio.lista_interna.primero
            while(inicio_interno!=None):
                if(inicio_interno.abajo!=None):
                    file.write("\n \"i" + str(inicio_interno.pos_x) + "-" + str(inicio_interno.pos_y) + "\" -> \"i" + str(inicio_interno.abajo.pos_x) + "-" + str(inicio_interno.abajo.pos_y) + "\";\n")
                    file.write("\"i"+str(inicio_interno.abajo.pos_x)+"-"+str(inicio_interno.abajo.pos_y)+"\" -> \"i"+str(inicio_interno.pos_x)+"-"+str(inicio_interno.pos_y)+"\";\n")
                inicio_interno = inicio_interno.abajo
            file.write(("\n Y"+str(inicio.posicion)+" -> \"i"+str(inicio.lista_interna.primero.pos_x)+"-"+str(inicio.lista_interna.primero.pos_y)+"\" \n"))
            file.write("\n \"i"+str(inicio.lista_interna.primero.pos_x)+"-"+str(inicio.lista_interna.primero.pos_y)+"\" -> Y"+str(inicio.posicion)+" \n")
            inicio = inicio.sig

                   
        file.write("} \n")
        file.close()
        
        os.system("neato dot -Tsvg Graficas/"+name+".dot -o Graficas/"+name+".svg")
        #os.startfile("..Graficas//Matriz.svg")  No jala XD

#La matriz se crea
matriz1 = matriz("junio")
'''
#(valor, x,y)
matriz1.insertar(1,5,2)
matriz1.insertar(2,1,1)
matriz1.insertar(3,4,1)
matriz1.insertar(4,4,2)
print(matriz1.buscarNodoMatriz(1,1))
matriz1.graficar()
matriz1.graficar()
matriz1.recorrer_matriz()
'''