class Nodo:
    def __init__(self,_carnet,_dpi,_nombre,_carrera,_correo,_password,_creditos,_edad):
        self.carnet = _carnet
        self.dpi = _dpi
        self.nombre = _nombre
        self.carrera = _carrera
        self.correo = _correo
        self.password = _password
        self.creditos = _creditos
        self.edad = _edad
        self.izquierdo = None
        self.derecho = None
        self.altura = 0
        #lista de años


class Avl:

    def __init__(self):
        self.raiz = None

    def maximo(self,v1,v2):
        if(v1>v2):
            return v1
        else:
            return v2

    def altura(self,nodo):
        if(nodo==None):
            return -1
        else:
            return nodo.altura
    
    def insertar(self,_carnet,_dpi,_nombre,_carrera,_correo,_password,_creditos,_edad):
        self.raiz = self.add(_carnet,_dpi,_nombre,_carrera,_correo,_password,_creditos,_edad,self.raiz)

    def add(self,_carnet,_dpi,_nombre,_carrera,_correo,_password,_creditos,_edad,nodo):
        if (nodo == None):
            nuevo = Nodo(_carnet,_dpi,_nombre,_carrera,_correo,_password,_creditos,_edad)
            return nuevo
        else:
            if (_carnet < nodo.carnet):
                nodo.izquierdo = self.add(_carnet,_dpi,_nombre,_carrera,_correo,_password,_creditos,_edad,nodo.izquierdo)
                
                if(self.altura(nodo.derecho)-self.altura(nodo.izquierdo) == -2):
                    if(_carnet < nodo.izquierdo.carnet):
                        nodo = self.RotIzquierda(nodo)
                    else:
                        nodo = self.RotDobIzquierda(nodo)
            elif (_carnet > nodo.carnet):
                nodo.derecho = self.add(_carnet,_dpi,_nombre,_carrera,_correo,_password,_creditos,_edad,nodo.derecho)
                if(self.altura(nodo.derecho)-self.altura(nodo.izquierdo) == 2):
                    if(_carnet > nodo.derecho.carnet):
                        nodo = self.RotDerecha(nodo)
                    else:
                        nodo = self.RotDobDerecha(nodo)
            else:
                nodo.carnet = _carnet

        nodo.altura = self.maximo(self.altura(nodo.izquierdo),self.altura(nodo.derecho)) +1
        return nodo


    def RotIzquierda(self,nodo):
        aux = nodo.izquierdo
        nodo.izquierdo = aux.derecho
        aux.derecho = nodo
        nodo.altura = self.maximo(self.altura(nodo.derecho),self.altura(nodo.izquierdo)) +1
        aux.altura = self.maximo(self.altura(nodo.izquierdo),nodo.altura) +1
        return aux

    def RotDobIzquierda(self,nodo):
        nodo.izquierdo = self.RotDerecha(nodo.izquierdo)
        return self.RotIzquierda(nodo)

    def RotDerecha(self,nodo):
        aux = nodo.derecho
        nodo.derecho = aux.izquierdo
        aux.izquierdo = nodo
        nodo.altura = self.maximo(self.altura(nodo.derecho),self.altura(nodo.izquierdo)) +1
        aux.altura = self.maximo(self.altura(nodo.derecho),nodo.altura) +1
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
                return actual.carnet

    def actualizar(self,_datoCarnet,_carnet,_dpi,_nombre,_carrera,_correo,_password,_creditos,_edad):
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
                actual.creditos = _creditos
                actual.edad = _edad
                break

    def eliminar(self,_carnet):
        if(self.raiz !=None):
            self.raiz = self.borrado(_carnet,self.raiz)
        
    def borrado(self,_carnet,raiz):
        if(_carnet < raiz.carnet):
            raiz.izquierdo = self.borrado(_carnet,raiz.izquierdo)
        elif(_carnet > raiz.carnet):
            raiz.derecho = self.borrado(_carnet,raiz.derecho)
        elif(_carnet == raiz.carnet):
            if(raiz.izquierdo == None and raiz.derecho == None):
                return None
            elif(raiz.izquierdo!= None and raiz.derecho == None):
                raiz = raiz.izquierdo
            elif(raiz.izquierdo == None and raiz.derecho != None):
                raiz = raiz.derecho
            else:
                aux = self.IzqMayor(raiz.izquierdo)
                raiz = self.borrado(aux,raiz)
                raiz.carnet = aux

        raiz = self.equilibrar(raiz)
        raiz.altura = self.maximo(self.altura(raiz.izquierdo),self.altura(raiz.derecho)) +1
        return raiz

    def IzqMayor(self,raiz):
        while(raiz.derecho!=None):
            raiz = raiz.derecho

        return raiz.carnet

    def equilibrar(self,raiz):
        if(self.altura(raiz.derecho)-self.altura(raiz.izquierdo) == -2):
            if(self.altura(raiz.izquierdo)==1):
                raiz = self.RotDobDerecha(raiz)
            else:
                raiz = self.RotDerecha(raiz)
        elif(self.altura(raiz.derecho)-self.altura(raiz.izquierdo) == 2):
            if(self.altura(raiz.derecho) == -1):
                raiz = self.RotDobIzquierda(raiz)
            else:
                raiz = self.RotIzquierda(raiz)

        return raiz 

avl = Avl()
avl.insertar(20,2014,"juan","sistema","juan@gmail.com",1234,20,23)
avl.insertar(10,2012,"pedro","sistema","ped@gmail.com",1143,21,17)
avl.insertar(30,2011,"lucas","sistema","luc@gmail.com",1544,23,20)
avl.insertar(5,2014,"pinda","sistema","juan@gmail.com",1234,20,23)
avl.insertar(15,2012,"kaspal","sistema","ped@gmail.com",1143,21,17)
avl.insertar(25,2011,"lolo","sistema","luc@gmail.com",1544,23,20)
#print(avl.buscar(10))
avl.eliminar(20)
print("Fin")

