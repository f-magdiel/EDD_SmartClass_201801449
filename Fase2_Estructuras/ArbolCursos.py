from abc import ABC


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
                        self.raiz.anterior = nodo
                        self.raiz.izquierdo = nodo.derecho
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
                

class Arbolb:
    def __init__(self):
        self.raiz = None
        self.orden = 5

    def insertar(self,_codigo,_nombre,_noCreditos,_codPrerrequisito,_obligatorio):
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
        self.buscar(_codigo,self.raiz)
        

    def buscar(self,_codigo,actual):
        
        if(isinstance( actual,Rama)):
           actual = actual.raiz

        if(_codigo == actual.codigo):
            print(actual.codigo)
            return actual.codigo
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
        





                
b = Arbolb()
b.insertar(10,"Juna",15,125,True)
b.insertar(11,"Pedro",22,126,False)
b.insertar(12,"Kass",32,127,True)
b.insertar(13,"Pina",12,128,False)
b.insertar(14,"Sandia",43,129,True)
b.insertar(15,"Limon",23,130,False)
b.insertar(16,"Mesa",231,131,True)
b.insertar(17,"Mouse",31,132,False)
b.insertar(18,"Lapiz",61,133,True)
b.insertar(19,"PC",33,134,False)
b.insertar(20,"Dell",11,135,True)
b.insertar(21,"Mac",33,134,False)
b.insertar(22,"Hp",11,135,True)
b.insertar(23,"Lis",33,134,False)
b.insertar(24,"Too",11,135,True)
b.insertar(25,"Vig",33,134,False)
b.insertar(26,"Mar",11,135,True)
b.buscarNodo(26)


                

