class Nodo:
    def __init__(self,_semestre):
        self.semestre = _semestre
        self.siguiente = None
        self.anterior = None
        #apuntador arbol b


class listaSemestre:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.posicion = 0

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
                return actual.semestre
            
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


lista = listaSemestre()
lista.buscarAgregar(1)
lista.buscarAgregar(2)
lista.buscarAgregar(3)
print("Fin")