import math
import os
import sys
import json

class Nodo:
    def __init__(self, indice):
        self.indice = indice
        self.lista = []

class Llave:
    def __init__(self,carnet, titulo, contenido):
        self.carnet = carnet
        self.titulo = titulo
        self.contenido = contenido
    def print(self):
        return "titulo:"+self.titulo + ", contenido:"+ self.contenido

class Hash:
    def __init__(self, contenido=7):
        self.vector = []
        self.elementos = 0
        self.factorCarga = 0
        self.tamano = contenido

        for i in range(contenido):
            self.vector.append(None)

    def insertar(self, id, titulo, contenido):
        posicion = self.funcion_hash(id)
        
        if self.vector[posicion] != None: #cuando ya existe el nodo principal
            listas = self.vector[posicion].lista
            _carnet = listas[0].carnet
            if _carnet == id: #si el carnet es igual al ingresado
                nuevo_contenido = Llave(id,titulo,contenido)
                self.vector[posicion].lista.append(nuevo_contenido)
            else:#si el carnet es nuevo pero se colisiona, pues exploracion
                nueva_posicion = self.exploracion(posicion)
                nuevo = Nodo(nueva_posicion)
                nuevo.lista.append(Llave(id,titulo, contenido))
                self.vector[nueva_posicion] = nuevo
                self.elementos+=1
                self.factorCarga = self.elementos/self.tamano
        else: #cuando se crea el nodo principal
            nuevo = Nodo(id)
            nuevo.lista.append(Llave(id,titulo, contenido))
            self.vector[posicion] = nuevo
            self.elementos+=1
            self.factorCarga = self.elementos/self.tamano

        if self.factorCarga > 0.5:
            self.rehashing()

    def esPrimo(self,num):
        if num < 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True  

    def exploracion(self,id):
        indice=0
        i =0
        disponible = False
        while(disponible==False):
            indice = id + int(pow(i,2))
            if(indice>= self.tamano):
                indice = indice - self.tamano

            if(self.vector[indice]==None):
                disponible = True

            i+=1

        return indice

    def rehashing(self):
        siguiente = self.tamano
        bandera = False

        while(bandera==False):
            siguiente+=1
            bandera = self.esPrimo(siguiente)
            

        temporal = []
        self.elementos = 0
        
        for i in range(siguiente):
            temporal.append(None)

        aux_vector = self.vector

        self.vector = temporal
        self.tamano = siguiente

        print("Nuevo tamano", siguiente, "Tamano:", len(temporal))
        for i in aux_vector:
            if i:
                for j in i.lista:
                    self.insertar(j.carnet, j.titulo, j.contenido)


    def funcion_hash(self, id):
        posicion = id % self.tamano
        return posicion

    def buscar(self,carnet):
        auxList = []
        dic ={}
        for i in self.vector:
            if i:
                if carnet == i.indice:
                    for j in i.lista:
                        dic["titulo"] = str(j.titulo)
                        dic["contenido"] = str(j.contenido)
                        dic_copy = dic.copy()
                        auxList.append(dic_copy)

        
        return auxList

    def print(self):
        contador = 0
        for i in self.vector:
            if i:
                print("indice:",contador, "contenido:", [j.print() for j in i.lista] )
            else:
                print("indice:", contador, "contenido", i)

            contador+=1

    def graficar(self):
        file = open("C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\hash.dot","w",encoding="UTF-8")
        file.write("digraph G{\n")
        file.write("rankdir=LR;\n")
        file.write("splines=line;\n")
        file.write('node[shape = record,style="filled",fillcolor=lightblue2,height=0];\n')

        #recorro primero el vector, enlisto los carnet
        contador=0
        claves = ""
        for i in self.vector:
            contador+=1
            if contador != len(self.vector):
                if i !=None:
                    aux = i
                    claves+= '<c'+str(aux.indice)+'> '+str(aux.indice)+"|"
                else:
                    claves+= "|"
                
        
        file.write('"hash"[label="'+claves+'"];\n')

        #luego recorro la lista, de la lista
        count = 0
        bandeNodo = True
        anterior = ""
        for m in self.vector:
            bandeNodo = True
            if m!=None:
                for n in m.lista:
                    if bandeNodo == True:
                        file.write('"'+str(n.titulo)+'"[label="'+str(n.titulo)+'"];\n')
                        file.write('"hash":c'+str(m.indice)+"->"+str(n.titulo)+';\n')
                        anterior = n.titulo
                        bandeNodo = False
                    else:
                        file.write('"'+str(n.titulo)+'"[label="'+str(n.titulo)+'"];\n')
                        file.write(str(anterior)+"->"+str(n.titulo)+";\n")
                        anterior = n.titulo
        file.write("}\n")
        file.close()
        os.system("dot -Tpng C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\hash.dot -o C:\\Users\\Magdiel\\Desktop\\EDD_SmartClass_201801449\\Fase_3\\Reportes\\hash.png")

""" tabla = Hash()
tabla.insertar(2,"primero","ocupado")
tabla.insertar(9,"casa","colision")
tabla.insertar(16,"saca","colision")
tabla.insertar(23,"saca1","colision")
tabla.insertar(2,"saca2","no hay colision")
tabla.insertar(2,"saca3","1")
tabla.insertar(16,"sacaasd","colision")
tabla.insertar(16,"sacafdsf","colision")
#tabla.graficar()
aux = tabla.buscar(2)
print(json.dumps(aux)) """