import os
import sys

class Nodo:
    def __init__(self,_codigo,_nombre,_noCreditos,_codPrerrequisito,_obligatorio):
        self.codigo = _codigo
        self.nombre = _nombre
        self.noCreditos = _noCreditos
        self.codPrerrequisito = _codPrerrequisito
        self.obligatorio = _obligatorio
        self.anterior = None
        self.siguiente = None
        self.derecho = None
        self.izquierdo = None


class Rama:
    def __init__(self):
        self.contador = 0 #contador de elementos insertados
        self.hoja = True
        self.raiz = None

    def insertar(self,nodo):
        if(self.raiz == None):
            self.raiz = nodo
            self.contador +=1
        else:
            actual = self.raiz
            while True:
                if(nodo.codigo <= actual.codigo):
                    self.contador +=1
                    if(actual==self.raiz):
                        nodo.siguiente = self.raiz
                        self.raiz.anterior = nodo
                        self.raiz = nodo
                        break
                    else:
                        nodo.anterior = actual.anterior
                        nodo.siguiente = actual
                        actual.anterior.siguiente = nodo
                        actual.anterior.derecho = nodo.izquierdo
                        actual.anterior = nodo
                        actual.izquierdo = nodo.derecho
                        break
                elif(actual.siguiente == None):
                    self.contador +=1
                    actual.siguiente = nodo
                    actual.derecho = nodo.izquierdo
                    nodo.anterior = actual
                    nodo.siguiente = None
                    break
                    
                actual = actual.siguiente
                if(actual==None):
                    break
                

class ArbolPensum:
    def __init__(self):
        self.raiz = None
        self.orden = 5
        self.contGen = 0

    def insertar(self,_codigo,_nombre,_noCreditos,_codPrerrequisito,_obligatorio):
        _codigo = int(_codigo)
        nodo = Nodo(_codigo,_nombre,_noCreditos,_codPrerrequisito,_obligatorio)
        if(self.raiz == None):
            self.raiz = Rama()
            self.raiz.insertar(nodo)
            return
        else:
            actual = self.add(nodo,self.raiz)
            if(isinstance(actual,Nodo)):
                self.raiz = Rama()
                self.raiz.insertar(actual)
                self.raiz.hoja = False

    def add(self,nodo,rama):
        if(rama.hoja):
            rama.insertar(nodo)
            if(rama.contador == self.orden):
                return self.dividirRama(rama)
            else:
                return rama
        else:
            actual = rama.raiz
            while True:
                if(nodo.codigo == actual.codigo):
                    return rama

                elif(nodo.codigo < actual.codigo):
                    aux = self.add(nodo,actual.izquierdo)
                    if(isinstance(aux,Nodo)):
                        rama.insertar(aux)
                        if(rama.contador == self.orden):
                            return  self.dividirRama(rama)
                    
                    return rama
                elif(actual.siguiente == None):
                    aux = self.add(nodo,actual.derecho)
                    if(isinstance(aux,Nodo)):
                        rama.insertar(aux)
                        if(rama.contador == self.orden):
                            return self.dividirRama(rama)
                    
                    return rama

                actual = actual.siguiente

                if(actual==None):
                    break
            
            return rama

    def dividirRama(self,rama):
        derecha = Rama()
        izquierda = Rama()
        medio = None
        actual = rama.raiz
        inicio = 1
        valorMedio =int((self.orden/2)+1)
        final = self.orden
        
        for i in range(self.orden+1):
            i+=1
            if(i<self.orden+1):
                nodo = Nodo(actual.codigo,actual.nombre,actual.noCreditos,actual.codPrerrequisito,actual.obligatorio)
                nodo.izquierdo = actual.izquierdo
                nodo.derecho = actual.derecho

                if(nodo.derecho !=None and nodo.izquierdo !=None):
                    izquierda.hoja = False
                    derecha.hoja = False

                if(i >= inicio and i < valorMedio):
                    izquierda.insertar(nodo)
                    actual = actual.siguiente
                
                elif(i == valorMedio):
                    medio = nodo
                    actual = actual.siguiente
             
                elif(i <= final and i>valorMedio):
                    derecha.insertar(nodo)
                    actual = actual.siguiente
            

        medio.izquierdo = izquierda
        medio.derecho = derecha
       
        return medio
        
    def buscarNodo(self,_codigo):
        try:
            _codigo = int(_codigo)
            aux = self.buscar(_codigo,self.raiz)
            if(aux!=None):
                 print("encontrado")
    
        except AttributeError:
            print("No encontrado")
        

    def buscar(self,_codigo,actual):
        
        if(isinstance( actual,Rama)):
           actual = actual.raiz

        if(_codigo == actual.codigo):
            print(actual.codigo)
            
        elif(_codigo < actual.codigo):
            actual = actual.izquierdo
            self.buscar(_codigo,actual)
        elif(_codigo > actual.codigo):
            if(actual.siguiente == None):
                actual = actual.derecho
                self.buscar(_codigo,actual)
            else:
                actual = actual.siguiente
                self.buscar(_codigo,actual)
       
        return actual

    def graficar(self):
        self.contGen +=1
        name = "arbolpensum"+str(self.contGen)
        file = open("Graficas/"+name+".dot","w",encoding="UTF-8")
        file.write("digraph G{\n")
        file.write("rankdor = TB;\n")
        file.write("splines=line;\n")
        file.write('node[shape = record,style="rounded,filled",fillcolor=lightblue2];\n')
        #los nodos
        file.write(self.graficarNodos(self.raiz))
        file.write(self.graficarEnlaces(self.raiz))
        file.write("\n")
        file.write("}\n")
        file.close()
        os.system("dot -Tsvg Graficas/"+name+".dot -o Graficas/"+name+".svg")

    def graficarNodos(self,raiz_actual):
        grafo =""
        if(raiz_actual.hoja):
            grafo+='node[label="<C0>'
            cont = 0
            pivote = raiz_actual.raiz
            while(pivote!=None):
                cont+=1
                grafo += "|{"+str(pivote.codigo)+"\\n"+str(pivote.nombre)+"}|<C"+str(cont)+">"
                pivote = pivote.siguiente
            
            grafo += '"]'+str(raiz_actual.raiz.codigo)+";\n"
            return grafo
        else:
            grafo+="node[label=\"<C0>"
            cont = 0
            pivote = raiz_actual.raiz

            while(pivote!=None):
                cont+=1
                grafo+="|{"+str(pivote.codigo)+"\\n"+str(pivote.nombre)+"}|<C"+str(cont)+">"
                pivote = pivote.siguiente
             
            grafo+="\"]"+str(raiz_actual.raiz.codigo)+";\n"

            pivote = raiz_actual.raiz
            cont = 0
            llave = False
            while(pivote!=None):
                if(pivote.siguiente==None):
                    llave = True
                aux = ""
                aux+=self.graficarNodos(pivote.izquierdo)
                grafo += aux
                cont+=1
                
                if(llave == True):
                    grafo += self.graficarNodos(pivote.derecho)
                
                pivote = pivote.siguiente

            
            return grafo 

    def graficarEnlaces(self,raiz_actual):
        grafo = ""
        if(raiz_actual.hoja):
            return ""+str(raiz_actual.raiz.codigo)+";"
        else:
            grafo += ""+str(raiz_actual.raiz.codigo)+";"
            pivote = raiz_actual.raiz
            cont = 0
            actual = ""+str(raiz_actual.raiz.codigo)
            llave = False
            while(pivote!=None):
                if(pivote.siguiente==None):
                    llave = True
                grafo+="\n"+actual+":C"+str(cont)+"->"+self.graficarEnlaces(pivote.izquierdo)
                cont+=1
                if(llave == True):
                    grafo += "\n"+actual+":C"+str(cont)+"->"+self.graficarEnlaces(pivote.derecho)
                pivote = pivote.siguiente

            #grafo += "\n"+actual+":C"+str(cont)+"->"+self.graficarEnlaces(raiz_actual.raiz.derecho)
            return grafo 
 
b = ArbolPensum()
'''
b.insertar(101,"Matematica Basica 1",7,"",True)
b.insertar(39,"Deportes 1",1,"",False)
b.insertar(348,"Quimica General 1",3,"",True)
b.insertar(103,"Matematica Basica 2",7,"101",True)
b.insertar(5,"Tecnias de Estudio e Investigacion",3,"",True)
b.insertar(960,"Matematica Computo 1",5,"103",True)
b.insertar(107,"Metematica Intermedia 1",10,"103",True)
b.insertar(770,"Introduccion a la Programacion y Computacion 1",4,"103",True)
b.insertar(796,"Lenguajes Formales y de Programación",3,"770,795,960",True)
b.insertar(772,"Estructuras de Datos",5,"771,796,962",True)
b.insertar(777,"Organización de Lenguajes y Compiladores 1",4,"771,796,962",True)
b.insertar(18,"Filosofia de la Ciencia",3,"019",False)
b.insertar(774,"Sistemas de Bases de Datos 1",5,"773",True)
b.insertar(281,"Sistemas Operativos 1",4,"781,778",True)
b.insertar(2036,"Practica Intermedia",0,"778,777,773,2025",True)
b.buscarNodo(2033)
b.graficar()
#b.buscarNodo(26)
'''

                

