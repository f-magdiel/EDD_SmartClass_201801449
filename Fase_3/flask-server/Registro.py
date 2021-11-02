import os
import sys

class Nodo:
    def __init__(self,_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad):
        self.carnet = _carnet
        self.dpi = _dpi
        self.nombre = _nombre
        self.carrera = _carrera
        self.correo = _correo
        self.password = _password
        self.edad = _edad
        self.izquierdo = None
        self.derecho = None
        self.altura = 0


class Avl:
    def __init__(self):
        self.raiz = None
        self.listaLabel = []
        self.listaNo = []
        self.conexion = ""
        self.contGen = 0

    def maximo(self,v1,v2):
        if(v1>v2):
            return v1
        else:
            return v2

    def altura(self,nodo):
        if(nodo!=None):
            return nodo.altura
        
        return -1
            
    
    def insertar(self,_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad):
        print("Ingreso al avl")
        self.raiz = self.add(_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad,self.raiz)

    def add(self,_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad,nodo):
        if (nodo == None):
            nuevo = Nodo(_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad)
            return nuevo
        else:
            if (_carnet < nodo.carnet):
                nodo.izquierdo = self.add(_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad,nodo.izquierdo)
                alt1 = self.altura(nodo.derecho)
                alt2 = self.altura(nodo.izquierdo)
                if(self.altura(nodo.derecho)-self.altura(nodo.izquierdo) == -2):
                    if(_carnet < nodo.izquierdo.carnet):
                        nodo = self.RotIzquierda(nodo)
                    else:
                        nodo = self.RotDobIzquierda(nodo)
            elif (_carnet > nodo.carnet):
                nodo.derecho = self.add(_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad,nodo.derecho)
                alt1 = self.altura(nodo.derecho)
                alt2 = self.altura(nodo.izquierdo)
                if(self.altura(nodo.derecho)-self.altura(nodo.izquierdo) == 2):
                    if(_carnet > nodo.derecho.carnet):
                        nodo = self.RotDerecha(nodo)
                    else:
                        nodo = self.RotDobDerecha(nodo)
            else:
                nodo.carnet = _carnet
        alt1 = self.altura(nodo.derecho)
        alt2 = self.altura(nodo.izquierdo)
        nodo.altura = self.maximo(self.altura(nodo.izquierdo),self.altura(nodo.derecho)) +1
        return nodo


    def RotIzquierda(self,nodo):
        aux = nodo.izquierdo
        nodo.izquierdo = aux.derecho
        aux.derecho = nodo
        nodo.altura = self.maximo(self.altura(nodo.derecho),self.altura(nodo.izquierdo)) +1
        aux.altura = self.maximo(self.altura(aux.izquierdo),nodo.altura) +1
        return aux

    def RotDobIzquierda(self,nodo):
        nodo.izquierdo = self.RotDerecha(nodo.izquierdo)
        return self.RotIzquierda(nodo)

    def RotDerecha(self,nodo):
        aux = nodo.derecho  
        nodo.derecho = aux.izquierdo
        aux.izquierdo = nodo
        nodo.altura = self.maximo(self.altura(nodo.derecho),self.altura(nodo.izquierdo)) +1
        aux.altura = self.maximo(self.altura(aux.derecho),nodo.altura) +1
        return aux

    def RotDobDerecha(self,nodo):
        nodo.derecho = self.RotIzquierda(nodo.derecho)
        return self.RotDerecha(nodo)

    def buscar(self,_carnet):
        actual = self.raiz
        while(actual!=None):
            if(_carnet > actual.carnet):
                actual = actual.derecho
            elif (_carnet < actual.carnet):
                actual = actual.izquierdo
            elif (_carnet == actual.carnet):
                return actual

    def actualizar(self,_datoCarnet,_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad):
        actual = self.raiz
        while(actual!=None):
            if(_datoCarnet > actual.carnet):
                actual = actual.derecho
            elif (_datoCarnet < actual.carnet):
                actual = actual.izquierdo
            elif (_datoCarnet == actual.carnet):
                actual.carnet = _carnet
                actual.dpi = _dpi
                actual.nombre = _nombre
                actual.carrera = _carrera
                actual.correo = _correo
                actual.password = _password
                actual.edad = _edad
                break
    
    def modificar(self,_carnet,_dpi,_nombre,_carrera,_correo,_password,_edad):
        actual = self.raiz
        while(actual!=None):
            if(_carnet > actual.carnet):
                actual = actual.derecho
            elif(_carnet < actual.carnet):
                actual = actual.izquierdo
            elif(_carnet == actual.carnet):
                actual.dpi = _dpi
                actual.nombre = _nombre
                actual.carrera = _carrera
                actual.correo = _correo
                actual.password = _password
                actual.edad = _edad
                break             

    def eliminar(self,_carnet):
        if(self.raiz !=None):
            self.raiz = self.borrado(_carnet,self.raiz)
        
    def borrado(self,_carnet,nodo):
        #eliminar nodos
        if(_carnet < nodo.carnet): # <- izquierdo
            nodo.izquierdo = self.borrado(_carnet,nodo.izquierdo)
        elif(_carnet > nodo.carnet): # -> derecho
            nodo.derecho = self.borrado(_carnet,nodo.derecho)
        elif(_carnet == nodo.carnet): #Es igual
            #Eliminar nodos
            if(nodo.izquierdo == None and nodo.derecho == None):
                return None #es hoja - > directo 
            elif(nodo.izquierdo != None and nodo.derecho == None):
                nodo = nodo.izquierdo #
                return nodo            
            elif(nodo.derecho != None and nodo.izquierdo == None):
                nodo = nodo.derecho
                return nodo
            else:
                carnetB = nodo.carnet
                aux = self.IzqMayor(nodo.izquierdo)
                nodo = self.borrado(aux.carnet,nodo)
                self.actualizar(carnetB,aux.carnet,aux.dpi,aux.nombre,aux.carrera,aux.correo,aux.password,aux.edad)
                
        nodo = self.equilibrar(nodo)
        nodo.altura = self.maximo(self.altura(nodo.izquierdo),self.altura(nodo.derecho)) +1
        return nodo

    def IzqMayor(self,nodo):
        while(nodo.derecho!=None):
            nodo = nodo.derecho

        return nodo


    def equilibrar(self,raiz):
        if(self.altura(raiz.derecho)-self.altura(raiz.izquierdo) == -2):
            if(self.altura(raiz.izquierdo.derecho)-self.altura(raiz.izquierdo.izquierdo)==1):
                raiz = self.RotDobIzquierda(raiz)
            elif(self.altura(raiz.izquierdo.derecho)-self.altura(raiz.izquierdo.izquierdo)==0):
                raiz = self.RotIzquierda(raiz)
            elif(self.altura(raiz.izquierdo.derecho)-self.altura(raiz.izquierdo.izquierdo)==-1):
                raiz = self.RotIzquierda(raiz)

        elif(self.altura(raiz.derecho)-self.altura(raiz.izquierdo) == 2):
            if(self.altura(raiz.derecho.derecho)-self.altura(raiz.derecho.izquierdo)==1):
                raiz = self.RotDerecha(raiz)
            elif(self.altura(raiz.derecho.derecho)-self.altura(raiz.derecho.izquierdo)==0):
                raiz = self.RotDerecha(raiz)
            elif(self.altura(raiz.derecho.derecho)-self.altura(raiz.derecho.izquierdo)==-1):
                raiz = self.RotDobDerecha(raiz)
            

        return raiz 
    
    

    
